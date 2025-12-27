from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
	QFrame,
	QGroupBox,
	QHBoxLayout,
	QLabel,
	QLineEdit,
	QListWidget,
	QMenu,
	QProgressBar,
	QSystemTrayIcon,
	QTabWidget,
	QTextEdit,
	QVBoxLayout,
	QWidget,
	QCheckBox,
	QComboBox,
	QSpinBox,
	QTableWidget,
	QTableWidgetItem,
	QMessageBox,
)
from PyQt6.QtGui import QIcon

from xcodecleaner.gui.widgets import AnimatedButton, AccentButton
from xcodecleaner.gui.styles import get_advanced_stylesheet
from xcodecleaner.system import sip as sys_sip


class TabsMixin:
	def add_sip_status_banner(self):
		# SIP banner removed - it's not useful and takes up space
		pass

	def init_ui(self):
		self.setWindowTitle("Xcode Disk Ejector Utility")
		self.resize(900, 700)
		self.setMinimumSize(700, 550)
		# Use default window flags for proper native macOS chrome

		# Main container with gradient background
		self.container.setObjectName("MainContainer")
		self.container.setGeometry(0, 0, self.width(), self.height())

		# Apply advanced styling
		self.setStyleSheet(get_advanced_stylesheet())

		# Main layout
		main_layout = QVBoxLayout()
		self.setLayout(main_layout)
		main_layout.setContentsMargins(0, 0, 0, 0)
		main_layout.setSpacing(0)
		self.main_layout = main_layout

		# SIP status banner
		self.add_sip_status_banner()

		# Custom title bar
		self.create_title_bar(main_layout)

		# Tab widget for different views
		self.tab_widget.setObjectName("MainTabs")
		main_layout.addWidget(self.tab_widget)

		self.create_dashboard_tab()
		self.create_process_tab()
		self.create_settings_tab()
		self.create_log_tab()
		self.create_status_bar(main_layout)

		# Start monitoring
		self.start_monitoring()

	def create_dashboard_tab(self):
		dashboard = QWidget()
		layout = QVBoxLayout(dashboard)

		# Quick stats
		stats_layout = QHBoxLayout()
		stats_layout.addWidget(self.mounted_stat)
		stats_layout.addWidget(self.process_stat)
		stats_layout.addWidget(self.space_stat)
		layout.addLayout(stats_layout)

		# Control buttons
		controls_layout = QHBoxLayout()
		self.scan_btn.setToolTip("Scan for simulator-related mounted volumes.")
		self.eject_selected_btn.setToolTip("Unmount selected simulator volumes (does not delete runtime files).")
		self.free_space_btn.setToolTip(
			"Reclaim disk space by deleting simulator runtime backing files.\n"
			"User-space cleanup is optional; full cleanup may require admin and will prompt."
		)
		self.nuclear_btn.setToolTip(
			"Aggressive cleanup:\n"
			"- Kills simulator/Xcode processes\n"
			"- Deletes simulator devices\n"
			"- Clears caches\n"
			"Use only if you understand the impact."
		)
		self.scan_btn.clicked.connect(self.scan_disks)
		controls_layout.addWidget(self.scan_btn)
		self.eject_selected_btn.clicked.connect(self.eject_selected)
		controls_layout.addWidget(self.eject_selected_btn)
		self.free_space_btn.clicked.connect(self.free_runtime_space_clicked)
		controls_layout.addWidget(self.free_space_btn)
		self.nuclear_btn.clicked.connect(self.nuclear_option)
		controls_layout.addWidget(self.nuclear_btn)
		layout.addLayout(controls_layout)

		# Progress bar
		self.progress_bar.setVisible(False)
		layout.addWidget(self.progress_bar)

		# Disk list
		disk_group = QGroupBox("Detected Simulator Disks")
		disk_layout = QVBoxLayout(disk_group)
		self.disk_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
		disk_layout.addWidget(self.disk_list)

		# Add refresh button below disk list
		refresh_layout = QHBoxLayout()
		self.refresh_disks_btn = AnimatedButton("Refresh")
		self.refresh_disks_btn.setObjectName("RefreshDisksButton")
		self.refresh_disks_btn.setToolTip("Rescan for simulator disks")
		self.refresh_disks_btn.clicked.connect(self.scan_disks)
		refresh_layout.addStretch()
		refresh_layout.addWidget(self.refresh_disks_btn)
		disk_layout.addLayout(refresh_layout)

		layout.addWidget(disk_group)

		self.tab_widget.addTab(dashboard, "Dashboard")

	def create_process_tab(self):
		process_widget = QWidget()
		layout = QVBoxLayout(process_widget)

		# Process controls
		controls = QHBoxLayout()
		self.refresh_processes_btn = AnimatedButton("Refresh Processes")
		self.refresh_processes_btn.setObjectName("RefreshProcessesButton")
		self.refresh_processes_btn.clicked.connect(self.refresh_processes)
		controls.addWidget(self.refresh_processes_btn)

		self.kill_selected_btn = AnimatedButton("Kill Selected")
		self.kill_selected_btn.setObjectName("KillSelectedButton")
		self.kill_selected_btn.clicked.connect(self.kill_selected_processes)
		controls.addWidget(self.kill_selected_btn)

		self.kill_all_btn = AnimatedButton("Kill All Simulators")
		self.kill_all_btn.setObjectName("KillAllSimulatorsButton")
		self.kill_all_btn.clicked.connect(self.kill_all_simulators)
		controls.addWidget(self.kill_all_btn)

		layout.addLayout(controls)

		# Process table
		self.process_table.setColumnCount(5)
		self.process_table.setHorizontalHeaderLabels(["Select", "PID", "CPU %", "Memory %", "Process Name"])
		self.process_table.horizontalHeader().setStretchLastSection(True)
		self.process_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
		layout.addWidget(self.process_table)

		self.tab_widget.addTab(process_widget, "Process Manager")

	def create_settings_tab(self):
		settings_widget = QWidget()
		layout = QVBoxLayout(settings_widget)

		# Auto-scan settings
		auto_group = QGroupBox("Automatic Operations")
		auto_layout = QVBoxLayout(auto_group)

		self.auto_scan_check.setChecked(True)
		self.auto_scan_check.setToolTip("Automatically scan for simulator disks on startup.")
		auto_layout.addWidget(self.auto_scan_check)

		self.auto_eject_check = QCheckBox("Auto-eject unmounted disks")
		self.auto_eject_check.setToolTip("Automatically attempt to eject detected disks during scans.")
		auto_layout.addWidget(self.auto_eject_check)

		# Scan interval
		interval_layout = QHBoxLayout()
		scan_interval_label = QLabel("Scan Interval (seconds):")
		scan_interval_label.setStyleSheet("color: white;")
		interval_layout.addWidget(scan_interval_label)
		self.scan_interval.setRange(5, 300)
		self.scan_interval.setValue(30)
		self.scan_interval.setToolTip("How often to auto-scan (when enabled).")
		interval_layout.addWidget(self.scan_interval)
		auto_layout.addLayout(interval_layout)

		layout.addWidget(auto_group)

		# Advanced settings
		advanced_group = QGroupBox("Advanced Options")
		advanced_layout = QVBoxLayout(advanced_group)
		advanced_layout.addWidget(self.force_unmount_check)
		self.force_unmount_check.setToolTip("Prefer force unmount when detaching volumes.")
		advanced_layout.addWidget(self.clear_cache_check)
		self.clear_cache_check.setToolTip("Clear simulator/Xcode caches as part of cleanup actions.")
		self.notify_check.setChecked(True)
		self.notify_check.setToolTip("Show notifications (including tray notifications).")
		advanced_layout.addWidget(self.notify_check)

		# Timeout setting
		timeout_layout = QHBoxLayout()
		timeout_label = QLabel("Operation Timeout (seconds):")
		timeout_label.setStyleSheet("color: white;")
		timeout_layout.addWidget(timeout_label)
		self.timeout_spin.setRange(5, 60)
		self.timeout_spin.setValue(15)
		self.timeout_spin.setToolTip("Detach timeout used for volume eject operations.")
		timeout_layout.addWidget(self.timeout_spin)
		advanced_layout.addLayout(timeout_layout)

		layout.addWidget(advanced_group)

		# Disk patterns
		patterns_group = QGroupBox("Disk Detection Patterns")
		patterns_layout = QVBoxLayout(patterns_group)
		self.patterns_edit.setPlainText("Simulator\nXcode\niOS\nwatchOS\ntvOS")
		self.patterns_edit.setMaximumHeight(100)
		patterns_layout.addWidget(self.patterns_edit)
		layout.addWidget(patterns_group)

		# Save settings button
		self.save_btn = AccentButton("Save Settings")
		self.save_btn.setObjectName("SaveButton")
		self.save_btn.clicked.connect(self.save_settings)
		layout.addWidget(self.save_btn)

		layout.addStretch()
		self.settings_tab_index = self.tab_widget.addTab(settings_widget, "Settings")

	def create_log_tab(self):
		log_widget = QWidget()
		layout = QVBoxLayout(log_widget)

		# Log controls
		log_controls = QHBoxLayout()
		self.clear_log_btn = AnimatedButton("Clear Log")
		self.clear_log_btn.setObjectName("ClearLogButton")
		self.clear_log_btn.clicked.connect(self.clear_log)
		log_controls.addWidget(self.clear_log_btn)

		self.export_log_btn = AnimatedButton("Export Log")
		self.export_log_btn.setObjectName("ExportLogButton")
		self.export_log_btn.clicked.connect(self.export_log)
		log_controls.addWidget(self.export_log_btn)

		log_label = QLabel("Log Level:")
		log_label.setStyleSheet("color: white;")
		log_controls.addWidget(log_label)
		self.log_level_combo.addItems(["All", "Info", "Warning", "Error"])
		self.log_level_combo.currentTextChanged.connect(self.filter_log)
		log_controls.addWidget(self.log_level_combo)

		log_controls.addStretch()
		layout.addLayout(log_controls)

		self.log_viewer.setReadOnly(True)
		layout.addWidget(self.log_viewer)
		self.tab_widget.addTab(log_widget, "Activity Log")

	def create_status_bar(self, layout):
		status_frame = QFrame()
		status_frame.setFixedHeight(30)
		status_frame.setStyleSheet(
			"""
			QFrame {
				background: rgba(0, 0, 0, 0.3);
				border-top: 1px solid rgba(255, 255, 255, 0.1);
			}
		"""
		)

		status_layout = QHBoxLayout(status_frame)
		status_layout.setContentsMargins(10, 0, 10, 0)

		self.status_label.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
		status_layout.addWidget(self.status_label)
		status_layout.addStretch()

		github_link = QLabel(
			'<a href="https://github.com/jguida941" style="color: #FFA500; text-decoration: none;">@jguida941</a>'
		)
		github_link.setTextFormat(Qt.TextFormat.RichText)
		github_link.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
		github_link.setOpenExternalLinks(True)
		github_link.setToolTip("Check out my GitHub!")
		github_link.setStyleSheet("QLabel { border: none; outline: none; background: transparent; } QLabel:focus { border: none; outline: none; }")
		status_layout.addWidget(github_link)

		self.connection_indicator.setStyleSheet("color: #27C93F;")
		status_layout.addWidget(self.connection_indicator)
		layout.addWidget(status_frame)

	def init_system_tray(self):
		if QSystemTrayIcon.isSystemTrayAvailable():
			self.tray_icon.setIcon(QIcon())
			tray_menu = QMenu()

			show_action = tray_menu.addAction("Show")
			show_action.triggered.connect(self.show)

			tray_menu.addSeparator()

			scan_action = tray_menu.addAction("Scan Disks")
			scan_action.triggered.connect(self.scan_disks)

			eject_all_action = tray_menu.addAction("Eject All")
			eject_all_action.triggered.connect(self.nuclear_option)

			tray_menu.addSeparator()

			quit_action = tray_menu.addAction("Quit")
			quit_action.triggered.connect(self.close)

			self.tray_icon.setContextMenu(tray_menu)
			self.tray_icon.show()


