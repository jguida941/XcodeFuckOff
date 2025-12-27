import subprocess

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMessageBox

from xcodecleaner.services import cleanup as svc_cleanup
from xcodecleaner.services import disks as svc_disks
from xcodecleaner.services import processes as svc_processes
from xcodecleaner.gui.threads import FreeRuntimeSpaceWorker


class ActionsMixin:
	def _format_bytes_gb(self, n: int) -> str:
		return f"{n / (1024**3):.2f} GB"

	def free_runtime_space_clicked(self):
		"""
		Guided flow to actually reclaim disk space.
		- Always runs simctl delete unavailable
		- User-space only: clears simulator Devices + DerivedData (no admin)
		- Full: additionally removes /Library CoreSimulator Volumes/Cryptex (requires admin)
		"""
		# Check if Xcode is running first - warn user strongly
		if svc_cleanup.is_xcode_running():
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

		cancel_btn = msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)
		user_btn = msg.addButton("User-space only", QMessageBox.ButtonRole.AcceptRole)
		full_btn = msg.addButton("Full cleanup (admin)", QMessageBox.ButtonRole.DestructiveRole)
		msg.setDefaultButton(user_btn)
		msg.exec()

		clicked = msg.clickedButton()
		if clicked == cancel_btn:
			return

		include_system = clicked == full_btn

		# If full cleanup, ensure Xcode/Simulator are stopped before deleting system runtimes
		if include_system:
			try:
				xcode_running = subprocess.run(["pgrep", "-x", "Xcode"], capture_output=True).returncode == 0
			except Exception:
				xcode_running = False

			if xcode_running:
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
				svc_processes.kill_all_simulators_and_xcode(password=None)
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
			parent=self,
		)
		self._free_space_worker.done_signal.connect(lambda result: self._on_free_space_done(result, include_system))
		self._free_space_worker.error_signal.connect(self._on_free_space_error)
		self._free_space_worker.start()

	def _on_free_space_done(self, result: dict, include_system: bool):
		try:
			self.progress_bar.setRange(0, 100)
			self.progress_bar.setVisible(False)
		except Exception:
			pass
		try:
			self.free_space_btn.setEnabled(True)
		except Exception:
			pass

		before = result.get("before")
		after = result.get("after")

		if before:
			self.log(f"Disk available (before): {self._format_bytes_gb(before['available_bytes'])}", "info")

		for cmd, rc in result.get("steps", []):
			level = "success" if rc == 0 else "warning"
			self.log(f"{cmd} (rc={rc})", level)

		if after:
			self.log(f"Disk available (after): {self._format_bytes_gb(after['available_bytes'])}", "info")

		if before and after:
			delta = after["available_bytes"] - before["available_bytes"]
			if delta > 0:
				mode = "Full cleanup" if include_system else "User-space cleanup"
				self.show_notification(f"{mode}: reclaimed {self._format_bytes_gb(delta)}", "success")
			else:
				self.show_notification("Cleanup finished (no increase detected yet)", "warning")

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
			svc_processes.kill_all_simulators_and_xcode(password=None)
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
			success, msg = svc_disks.force_unmount_disk(disk["device"], timeout_seconds=timeout_s)
			if success:
				self.log(f"{disk['device']} ejected", level="success")
			else:
				self.log(f"Failed to eject {disk['device']}: {msg}", level="error")

		self.show_notification(f"Eject operation complete for {len(self.selected_disks)} disk(s)", "success")
		self.scan_disks()

	@staticmethod
	def force_unmount_disk(device: str) -> str:
		_, msg = svc_disks.force_unmount_disk(device)
		return msg

	def eject_disk(self, disk_id: str):
		timeout_s = int(self.timeout_spin.value())
		success, msg = svc_disks.eject_disk(disk_id, timeout_seconds=timeout_s)
		self.log(f"{msg}", level="success" if success else "error")

	def nuclear_option(self):
		reply = QMessageBox.warning(
			self,
			"Nuclear Option",
			"This will:\n• Kill ALL simulator processes\n• Force unmount ALL simulator disks\n• Delete ALL simulator devices and data\n• Clear simulator caches\n\nContinue?",
			QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
		)

		if reply != QMessageBox.StandardButton.Yes:
			return

		self.log("Executing nuclear option...", "warning")
		self.progress_bar.setVisible(True)
		self.progress_bar.setValue(0)

		self.progress_bar.setValue(25)
		self._do_kill_all_simulators()

		self.log("Deleting all simulator devices...", "info")
		self.log("All simulator devices deleted", "success" if svc_cleanup.delete_all_sim_devices() else "error")

		self.log("Removing device directories and profiles...", "info")
		self.log(
			"Device directories and profiles removed",
			"success" if svc_cleanup.remove_device_directories_and_profiles() else "error",
		)

		self.log("Disabling CoreSimulator service...", "info")
		self.log("CoreSimulator service disabled", "success" if svc_cleanup.disable_core_simulator_service() else "error")

		self.progress_bar.setValue(50)
		self.scan_disks()

		QTimer.singleShot(1000, self._nuclear_unmount_all)

	def _nuclear_unmount_all(self):
		self.progress_bar.setValue(75)

		for i in range(self.disk_list.count()):
			item = self.disk_list.item(i)
			disk = item.data(Qt.ItemDataRole.UserRole)
			if disk and "device" in disk:
				timeout_s = int(self.timeout_spin.value())
				success, msg = svc_disks.force_unmount_disk(disk["device"], timeout_seconds=timeout_s)
				self.log(msg, level="success" if success else "error")

		self.clear_all_simulator_caches()

		self.progress_bar.setValue(100)
		self.progress_bar.setVisible(False)

		self.show_notification("Nuclear option complete!", "success")
		self.log("Nuclear option completed", "success")

		QTimer.singleShot(500, self.scan_disks)

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
			if svc_processes.kill_process(str(pid)):
				self.log(f"Killed process {pid}", "success")
			else:
				self.log(f"Failed to kill process {pid}", "error")

		self.refresh_processes()

	def _do_kill_all_simulators(self):
		"""Internal: kill simulators without showing notification."""
		results = svc_processes.kill_all_simulators_and_xcode()
		for cmd, rc in results:
			level = "info" if rc == 0 else "warning"
			self.log(f"Executed: {cmd} (rc={rc})", level)

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

		for path in cache_paths:
			try:
				subprocess.run(["rm", "-rf", path], check=False)
				self.log(f"Cleared cache: {path}", "info")
			except Exception:
				pass

	def clear_all_simulator_caches(self):
		self.log("Clearing all simulator caches...", "info")
		for path, rc in svc_cleanup.clear_all_simulator_caches():
			level = "success" if rc == 0 else "warning"
			self.log(f"Cleared: {path}" if rc == 0 else f"Failed to clear: {path}", level)


