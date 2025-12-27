from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMessageBox

from xcodecleaner.core.runner import get_default_runner
from xcodecleaner.services import disks as svc_disks
from xcodecleaner.services import processes as svc_processes
from xcodecleaner.system import devtools as svc_devtools
from xcodecleaner.gui.threads import FreeRuntimeSpaceWorker, ManualCleanupWorker, NuclearCleanupWorker


class ActionsMixin:
	def _format_bytes_gb(self, n: int) -> str:
		return f"{n / (1024**3):.2f} GB"

	def _check_devtools_available(self, *, allow_manual: bool = False) -> tuple[bool, bool]:
		"""Check if developer tools are available. Returns (simctl_ok, manual_only)."""
		ok, message = svc_devtools.check_devtools(runner=self.runner)
		self._simctl_env = svc_devtools.get_simctl_env(runner=self.runner)
		if ok:
			if message and message != "Developer tools configured correctly":
				self.log(message, "info")
			return True, False

		if allow_manual:
			msg = QMessageBox(self)
			msg.setIcon(QMessageBox.Icon.Warning)
			msg.setWindowTitle("Developer Tools Not Configured")
			msg.setText(
				f"{message}\n\n"
				"Without simctl, this tool cannot permanently delete simulator runtimes.\n"
				"You can still run a manual cleanup to reclaim disk space."
			)
			manual_btn = msg.addButton("Manual Cleanup", QMessageBox.ButtonRole.AcceptRole)
			cancel_btn = msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
			msg.setDefaultButton(cancel_btn)
			msg.exec()
			if msg.clickedButton() == manual_btn:
				self.log(f"Manual cleanup mode: {message}", "warning")
				self._simctl_env = None
				return False, True
			self.log(f"DevTools check failed: {message}", "error")
			return False, False

		QMessageBox.critical(
			self,
			"Developer Tools Not Configured",
			f"{message}\n\n"
			"Without simctl, this tool cannot permanently delete simulator runtimes.\n"
			"It can only temporarily unmount disk images.",
		)
		self.log(f"DevTools check failed: {message}", "error")
		return False, False

	def free_runtime_space_clicked(self):
		"""
		Guided flow to actually reclaim disk space.
		- Always runs simctl delete unavailable
		- User-space only: clears simulator Devices + DerivedData (no admin)
		- Full: additionally removes /Library CoreSimulator Volumes/Cryptex (requires admin)
		"""
		# Check if simctl is available first
		simctl_ok, manual_only = self._check_devtools_available(allow_manual=True)
		if not simctl_ok and not manual_only:
			return
		if manual_only:
			self._start_manual_cleanup_flow()
			return

		# Check if Xcode is running first - warn user strongly
		if self.cleanup_service.is_xcode_running():
			reply = QMessageBox.warning(
				self,
				"Xcode is Running!",
				"Xcode or Simulator is currently running.\n\n"
				"WARNING: If you proceed, Xcode will likely RE-MOUNT\n"
				"the simulator runtimes immediately after cleanup,\n"
				"and you'll see no space freed.\n\n"
				"Quit Xcode and Simulator first for best results.",
				QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Ignore,
			)
			if reply == QMessageBox.StandardButton.Abort:
				return

		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Icon.Warning)
		msg.setWindowTitle("Free Runtime Space")
		msg.setText(
			"This will attempt to reclaim disk space.\n\n"
			"Important: Eject only unmounts; it does not free space.\n"
		)
		msg.setInformativeText(
			"Choose a cleanup mode:\n"
			"• User-space only: removes simulator Devices + DerivedData (no admin)\n"
			"• Full cleanup: UNREGISTERS runtimes from Xcode + deletes backing files (admin)\n"
		)

		user_btn = msg.addButton("User Cleanup", QMessageBox.ButtonRole.AcceptRole)
		cancel_btn = msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
		full_btn = msg.addButton("Full Cleanup", QMessageBox.ButtonRole.DestructiveRole)
		msg.setDefaultButton(cancel_btn)
		msg.exec()

		clicked = msg.clickedButton()
		if clicked == cancel_btn:
			return

		include_system = clicked == full_btn

		# If full cleanup, ensure Xcode/Simulator are stopped before deleting system runtimes
		if include_system:
			if self.cleanup_service.is_xcode_running():
				kill_now = QMessageBox.question(
					self,
					"Xcode is running",
					"Xcode is currently running.\n\n"
					"For safe runtime deletion, Xcode/CoreSimulator should be stopped.\n\n"
					"Close them now automatically?",
					QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
				)
				if kill_now != QMessageBox.StandardButton.Yes:
					self.show_notification("Please close Xcode and try again", "warning")
					return

			# Best-effort stop without password prompt
			try:
				svc_processes.kill_all_simulators_and_xcode(password=None, runner=self.runner)
			except Exception:
				pass

		# Optional: user-space wipes (do NOT force by default)
		wipe_devices = (
			QMessageBox.question(
				self,
				"Delete Simulator Devices",
				"Delete all simulator devices?\n\n"
				"This removes: ~/Library/Developer/CoreSimulator/Devices\n"
				"(You will lose simulator state.)",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)

		wipe_derived = (
			QMessageBox.question(
				self,
				"Delete DerivedData",
				"Delete Xcode DerivedData?\n\n"
				"This removes: ~/Library/Developer/Xcode/DerivedData\n"
				"(Next builds will recompile.)",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)

		self._start_free_runtime_space_worker(
			include_system=include_system,
			wipe_devices=wipe_devices,
			wipe_derived=wipe_derived,
		)

	def _start_free_runtime_space_worker(self, include_system: bool, wipe_devices: bool, wipe_derived: bool):
		# Prevent double-click / re-entry
		if getattr(self, "_free_space_worker", None) is not None and self._free_space_worker.isRunning():
			self.show_notification("Cleanup already running", "warning")
			return

		self.log("Freeing runtime space...", "warning")

		# Show indeterminate progress while long-running commands execute
		try:
			self.progress_bar.setVisible(True)
			self.progress_bar.setRange(0, 0)
		except Exception:
			pass

		try:
			self.free_space_btn.setEnabled(False)
		except Exception:
			pass

		self._free_space_worker = FreeRuntimeSpaceWorker(
			include_system_runtime_files=include_system,
			include_user_space=(wipe_devices or wipe_derived),
			delete_devices=wipe_devices,
			delete_derived_data=wipe_derived,
			stop_processes=True,
			simctl_env=getattr(self, "_simctl_env", None),
			runner=self.runner,
			parent=self,
		)
		self._free_space_worker.done_signal.connect(lambda result: self._on_free_space_done(result, include_system))
		self._free_space_worker.error_signal.connect(self._on_free_space_error)
		self._free_space_worker.start()

	def _start_manual_cleanup_flow(self):
		msg = QMessageBox(self)
		msg.setIcon(QMessageBox.Icon.Warning)
		msg.setWindowTitle("Manual Cleanup (No simctl)")
		msg.setText(
			"This will delete simulator data without simctl.\n\n"
			"Paths may include:\n"
			"• ~/Library/Developer/CoreSimulator\n"
			"• ~/Library/Developer/Xcode/DerivedData\n"
			"• ~/Library/Developer/Xcode/Archives\n"
			"• ~/Library/Caches/com.apple.dt.Xcode\n"
			"• ~/Library/Caches/org.swift.swiftpm"
		)
		proceed_btn = msg.addButton("Continue", QMessageBox.ButtonRole.AcceptRole)
		cancel_btn = msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
		msg.setDefaultButton(cancel_btn)
		msg.exec()
		if msg.clickedButton() != proceed_btn:
			return

		delete_core = (
			QMessageBox.question(
				self,
				"Delete CoreSimulator Data",
				"Delete ~/Library/Developer/CoreSimulator?\n\n"
				"This removes all simulator devices, runtimes, and state.",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)
		delete_derived = (
			QMessageBox.question(
				self,
				"Delete DerivedData",
				"Delete ~/Library/Developer/Xcode/DerivedData?",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)
		delete_archives = (
			QMessageBox.question(
				self,
				"Delete Archives",
				"Delete ~/Library/Developer/Xcode/Archives?",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)
		delete_caches = (
			QMessageBox.question(
				self,
				"Delete Xcode Caches",
				"Delete Xcode caches in ~/Library/Caches?\n\n"
				"This removes com.apple.dt.Xcode and org.swift.swiftpm caches.",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)
		delete_device_support = (
			QMessageBox.question(
				self,
				"Delete iOS DeviceSupport",
				"Delete ~/Library/Developer/Xcode/iOS DeviceSupport?\n\n"
				"This can be large, but will be re-downloaded if needed.",
				QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
			)
			== QMessageBox.StandardButton.Yes
		)

		self._start_manual_cleanup_worker(
			delete_core_simulator=delete_core,
			delete_derived_data=delete_derived,
			delete_archives=delete_archives,
			delete_caches=delete_caches,
			delete_device_support=delete_device_support,
		)

	def _start_manual_cleanup_worker(
		self,
		delete_core_simulator: bool,
		delete_derived_data: bool,
		delete_archives: bool,
		delete_caches: bool,
		delete_device_support: bool,
	):
		if getattr(self, "_manual_worker", None) is not None and self._manual_worker.isRunning():
			self.show_notification("Manual cleanup already running", "warning")
			return

		self.log("Running manual cleanup...", "warning")
		try:
			self.progress_bar.setVisible(True)
			self.progress_bar.setRange(0, 0)
		except Exception:
			pass

		try:
			self.free_space_btn.setEnabled(False)
		except Exception:
			pass

		self._manual_worker = ManualCleanupWorker(
			delete_core_simulator=delete_core_simulator,
			delete_derived_data=delete_derived_data,
			delete_archives=delete_archives,
			delete_caches=delete_caches,
			delete_device_support=delete_device_support,
			stop_processes=True,
			runner=self.runner,
			parent=self,
		)
		self._manual_worker.done_signal.connect(self._on_manual_cleanup_done)
		self._manual_worker.error_signal.connect(self._on_free_space_error)
		self._manual_worker.start()

	def _on_free_space_done(self, result, include_system: bool):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.free_space_btn.setEnabled(True)
		except Exception:
			pass

		if result.space_before is not None:
			self.log(f"Disk available (before): {self._format_bytes_gb(result.space_before)}", "info")

		for step in result.steps:
			level = "success" if step.ok else "warning"
			self.log(f"{step.label} (rc={step.result.returncode})", level)

		if result.space_after is not None:
			self.log(f"Disk available (after): {self._format_bytes_gb(result.space_after)}", "info")

		if not result.commands_ok:
			self.show_notification("Cleanup failed (see log)", "error")
			if result.error:
				self.log(f"Cleanup error: {result.error}", "error")
			return

		if result.space_ok is None or result.space_delta is None:
			self.show_notification("Cleanup finished (space delta unavailable)", "warning")
			return

		if result.space_ok:
			mode = "Full cleanup" if include_system else "User-space cleanup"
			self.show_notification(f"{mode}: reclaimed {self._format_bytes_gb(result.space_delta)}", "success")
		else:
			self.show_notification("Cleanup finished (no increase detected yet)", "warning")

	def _on_manual_cleanup_done(self, result):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.free_space_btn.setEnabled(True)
		except Exception:
			pass

		if result.space_before is not None:
			self.log(f"Disk available (before): {self._format_bytes_gb(result.space_before)}", "info")

		for step in result.steps:
			level = "success" if step.ok else "warning"
			self.log(f"{step.label} (rc={step.result.returncode})", level)

		if result.space_after is not None:
			self.log(f"Disk available (after): {self._format_bytes_gb(result.space_after)}", "info")

		if not result.commands_ok:
			self.show_notification("Manual cleanup failed (see log)", "error")
			if result.error:
				self.log(f"Manual cleanup error: {result.error}", "error")
			return

		if result.space_ok is None or result.space_delta is None:
			self.show_notification("Manual cleanup finished (space delta unavailable)", "warning")
			return

		if result.space_ok:
			self.show_notification(f"Manual cleanup: reclaimed {self._format_bytes_gb(result.space_delta)}", "success")
		else:
			self.show_notification("Manual cleanup finished (no increase detected yet)", "warning")

	def _on_free_space_error(self, msg: str):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.free_space_btn.setEnabled(True)
		except Exception:
			pass
		self.log(f"Free Runtime Space failed: {msg}", "error")
		self.show_notification("Free Runtime Space failed (see log)", "error")

	def eject_selected(self):
		selected_items = self.disk_list.selectedItems()
		if not selected_items:
			self.show_notification("No disks selected", "warning")
			return

		# Kill simulator processes before unmounting (best-effort without prompting for admin)
		try:
			svc_processes.kill_all_simulators_and_xcode(password=None, runner=self.runner)
		except Exception as exc:
			self.log(f"Exception killing simulators: {exc}", level="error")

		self.selected_disks = []
		for item in selected_items:
			disk = item.data(Qt.ItemDataRole.UserRole)
			if isinstance(disk, dict) and "device" in disk:
				self.selected_disks.append(disk)

		if not self.selected_disks:
			self.show_notification("No valid disks selected", "warning")
			return

		self.log(f"Ejecting {len(self.selected_disks)} selected disk(s)...", "info")

		for disk in self.selected_disks:
			timeout_s = int(self.timeout_spin.value())
			success, msg = svc_disks.force_unmount_disk(disk["device"], timeout_seconds=timeout_s, runner=self.runner)
			if success:
				self.log(f"{disk['device']} ejected", level="success")
			else:
				self.log(f"Failed to eject {disk['device']}: {msg}", level="error")

		self.show_notification(f"Eject operation complete for {len(self.selected_disks)} disk(s)", "success")
		self.scan_disks()

	@staticmethod
	def force_unmount_disk(device: str) -> str:
		_, msg = svc_disks.force_unmount_disk(device, runner=get_default_runner())
		return msg

	def eject_disk(self, disk_id: str):
		timeout_s = int(self.timeout_spin.value())
		success, msg = svc_disks.eject_disk(disk_id, timeout_seconds=timeout_s, runner=self.runner)
		self.log(f"{msg}", level="success" if success else "error")

	def nuclear_option(self):
		# Check if simctl is available first
		simctl_ok, manual_only = self._check_devtools_available()
		if not simctl_ok or manual_only:
			return

		reply = QMessageBox.warning(
			self,
			"Nuclear Option",
			"This will:\n• Kill ALL simulator processes\n• Force unmount ALL simulator disks\n• Delete ALL simulator devices and runtimes\n• Clear simulator caches\n\nThis PERMANENTLY removes runtimes. Continue?",
			QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
		)

		if reply != QMessageBox.StandardButton.Yes:
			return

		self._start_nuclear_cleanup_worker()

	def _start_nuclear_cleanup_worker(self):
		if getattr(self, "_nuclear_worker", None) is not None and self._nuclear_worker.isRunning():
			self.show_notification("Nuclear cleanup already running", "warning")
			return

		self.log("Executing nuclear option...", "warning")
		try:
			self.progress_bar.setVisible(True)
			self.progress_bar.setRange(0, 0)
		except Exception:
			pass

		try:
			self.nuclear_btn.setEnabled(False)
		except Exception:
			pass

		self._nuclear_worker = NuclearCleanupWorker(
			simctl_env=getattr(self, "_simctl_env", None),
			runner=self.runner,
			parent=self,
		)
		self._nuclear_worker.done_signal.connect(self._on_nuclear_done)
		self._nuclear_worker.error_signal.connect(self._on_nuclear_error)
		self._nuclear_worker.start()

	def _on_nuclear_done(self, result):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.nuclear_btn.setEnabled(True)
		except Exception:
			pass

		for step in result.steps:
			level = "success" if step.ok else "warning"
			self.log(f"{step.label} (rc={step.result.returncode})", level)

		if result.commands_ok:
			self.show_notification("Nuclear option complete!", "success")
			self.log("Nuclear option completed", "success")
		else:
			self.show_notification("Nuclear option failed (see log)", "error")
			if result.error:
				self.log(f"Nuclear cleanup error: {result.error}", "error")

		QTimer.singleShot(500, self.scan_disks)

	def _on_nuclear_error(self, msg: str):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.nuclear_btn.setEnabled(True)
		except Exception:
			pass
		self.log(f"Nuclear cleanup failed: {msg}", "error")
		self.show_notification("Nuclear cleanup failed (see log)", "error")

	def kill_selected_processes(self):
		selected_pids = []

		for row in range(self.process_table.rowCount()):
			checkbox = self.process_table.cellWidget(row, 0)
			if checkbox and checkbox.isChecked():
				pid = self.process_table.item(row, 1).text()
				selected_pids.append(pid)

		if not selected_pids:
			self.show_notification("No processes selected", "warning")
			return

		for pid in selected_pids:
			if svc_processes.kill_process(str(pid), runner=self.runner):
				self.log(f"Killed process {pid}", "success")
			else:
				self.log(f"Failed to kill process {pid}", "error")

		self.refresh_processes()

	def _do_kill_all_simulators(self):
		"""Internal: kill simulators without showing notification."""
		results = svc_processes.kill_all_simulators_and_xcode(runner=self.runner)
		for result in results:
			level = "info" if result.returncode == 0 else "warning"
			self.log(f"Executed: {' '.join(result.cmd)} (rc={result.returncode})", level)

	def kill_all_simulators(self):
		"""Kill all simulator processes (user action with notification)."""
		self._do_kill_all_simulators()
		self.show_notification("All simulator processes killed", "success")
		self.refresh_processes()

	def clear_simulator_cache(self):
		"""Clear simulator caches (user-space only)."""
		cache_paths = [
			"~/Library/Developer/CoreSimulator/Caches",
			"~/Library/Developer/CoreSimulator/Devices/*/data/Library/Caches",
		]
		result = self.cleanup_service.clear_paths(cache_paths)
		for step in result.steps:
			level = "success" if step.ok else "warning"
			self.log(f"Cleared cache: {step.label.replace('rm -rf ', '')}", level)

	def clear_all_simulator_caches(self):
		self.log("Clearing all simulator caches...", "info")
		result = self.cleanup_service.clear_all_simulator_caches()
		for step in result.steps:
			level = "success" if step.ok else "warning"
			self.log(f"Cleared: {step.label.replace('rm -rf ', '')}" if step.ok else f"Failed to clear: {step.label.replace('rm -rf ', '')}", level)
