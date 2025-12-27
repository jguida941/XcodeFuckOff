from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QCheckBox, QLabel, QListWidgetItem, QTableWidgetItem


class MonitoringMixin:
	"""Background disk scanning and process monitoring."""

	def _update_scan_timer(self):
		if getattr(self, "scan_timer", None) is None:
			return
		try:
			interval_ms = int(self.scan_interval.value()) * 1000
			self.scan_timer.setInterval(max(1000, interval_ms))
		except Exception:
			self.scan_timer.setInterval(30000)

	def start_monitoring(self):
		# Connect signals
		self.disk_scanner.update_signal.connect(self.update_disk_list)
		self.disk_scanner.progress_signal.connect(self.update_progress)
		self.process_monitor.update_signal.connect(self.update_process_list)

		# Auto-scan timer
		self.scan_timer = QTimer()
		self.scan_timer.timeout.connect(self.auto_scan)
		self._update_scan_timer()
		self.scan_timer.start()

		# Update interval live when user changes the preference
		try:
			self.scan_interval.valueChanged.connect(lambda _v: self._update_scan_timer())
		except Exception:
			pass

		# Initial scan
		if self.auto_scan_check.isChecked():
			self.scan_disks()

		# Automatically populate Process Manager on startup
		self.refresh_processes()

	def scan_disks(self):
		self.log("Scanning for simulator disks...", "info")
		self.progress_bar.setVisible(True)
		self.progress_bar.setValue(0)
		self.status_label.setText("Scanning disks...")

		if not self.disk_scanner.isRunning():
			self.disk_scanner.start()

	def update_disk_list(self, disks):
		self.disk_list.clear()
		total_size = 0

		for disk in disks:
			item = QListWidgetItem(f"{disk['name']} ({disk['device']}) - {disk['size']}")
			item.setData(Qt.ItemDataRole.UserRole, disk)
			self.disk_list.addItem(item)

			try:
				size_gb = float(disk["size"].split()[0])
				total_size += size_gb
			except Exception:
				pass

		self.mounted_stat.findChild(QLabel, "MountedDisksValue").setText(str(len(disks)))
		self.space_stat.findChild(QLabel, "SpaceUsedValue").setText(f"{total_size:.1f} GB")

		self.progress_bar.setVisible(False)
		self.status_label.setText(f"Found {len(disks)} simulator disk(s)")
		self.log(f"Scan complete: {len(disks)} disks found", "info")

	def update_progress(self, value):
		self.progress_bar.setValue(value)

	def refresh_processes(self):
		self.log("Refreshing process list...", "info")
		self.status_label.setText("Scanning processes...")

		if not self.process_monitor.isRunning():
			self.process_monitor.start()

	def update_process_list(self, processes):
		self.process_table.setRowCount(len(processes))

		for i, proc in enumerate(processes):
			checkbox = QCheckBox()
			self.process_table.setCellWidget(i, 0, checkbox)

			self.process_table.setItem(i, 1, QTableWidgetItem(proc["pid"]))
			self.process_table.setItem(i, 2, QTableWidgetItem(f"{proc['cpu']}%"))
			self.process_table.setItem(i, 3, QTableWidgetItem(f"{proc['mem']}%"))
			self.process_table.setItem(i, 4, QTableWidgetItem(proc["name"]))

		self.process_stat.findChild(QLabel, "SimulatorProcessesValue").setText(str(len(processes)))
		self.status_label.setText(f"Found {len(processes)} simulator process(es)")


