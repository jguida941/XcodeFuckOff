"""Main application window combining all GUI mixins."""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import (
	QApplication,
	QCheckBox,
	QComboBox,
	QFrame,
	QListWidget,
	QProgressBar,
	QSpinBox,
	QSystemTrayIcon,
	QTabWidget,
	QTableWidget,
	QTextEdit,
	QLabel,
	QWidget,
)

from xcodefuckoff.core.runner import get_default_runner
from xcodefuckoff.services import cleanup as svc_cleanup
from xcodefuckoff.gui.threads import DiskScanner, ProcessMonitor
from xcodefuckoff.gui.widgets import AccentButton, create_stat_widget
from xcodefuckoff.gui.mixins import ActionsMixin, ChromeMixin, LoggingMixin, MonitoringMixin, TabsMixin


class EnhancedSimulatorKiller(QWidget, ChromeMixin, TabsMixin, MonitoringMixin, ActionsMixin, LoggingMixin):
    """
    Main application window for XcodeFuckOff.

    Combines multiple mixins for functionality:
    - ChromeMixin: Native macOS window chrome and title bar
    - TabsMixin: Tab-based UI layout (Dashboard, Processes, Settings, Log)
    - MonitoringMixin: Background disk/process scanning
    - ActionsMixin: Cleanup actions (eject, free space, nuclear option)
    - LoggingMixin: Activity logging and export
    """

    def __init__(self):
        super().__init__()
        self.runner = get_default_runner()
        self.cleanup_service = svc_cleanup.CleanupService(runner=self.runner)
        self.main_layout = None
        self.title_bar = None
        self.eject_selected_btn = AccentButton("Eject Selected")
        self.eject_selected_btn.setObjectName("EjectSelectedButton")
        self.free_space_btn = AccentButton("Free Runtime Space")
        self.free_space_btn.setObjectName("FreeRuntimeSpaceButton")
        self.old_pos = None
        self.space_stat = create_stat_widget("Space Used", "0 GB")
        self.mounted_stat = create_stat_widget("Mounted Disks", "0")
        self.connection_indicator = QLabel("●")
        self.status_label = QLabel("Ready")
        self.scan_btn = AccentButton("Scan Disks")
        self.scan_btn.setObjectName("ScanDisksButton")
        self.log_level_combo = QComboBox()
        self.process_table = QTableWidget()
        self.patterns_edit = QTextEdit()
        self.notify_check = QCheckBox("Show notifications")
        self.progress_bar = QProgressBar()
        self.nuclear_btn = AccentButton("Nuclear Option")
        self.nuclear_btn.setObjectName("NuclearOptionButton")
        # Placeholders for new process tab/process buttons
        self.refresh_processes_btn = None
        self.kill_selected_btn = None
        self.kill_all_btn = None
        self.save_btn = None
        self.clear_log_btn = None
        self.export_log_btn = None
        self.disk_list = QListWidget()
        self.clear_cache_check = QCheckBox("Clear simulator caches on eject")
        self.scan_interval = QSpinBox()
        self.force_unmount_check = QCheckBox("Always force unmount")
        self.timeout_spin = QSpinBox()
        self.process_stat = create_stat_widget("Simulator Processes", "0")
        self.tab_widget = QTabWidget()
        self.container = QFrame(self)
        self.auto_eject_check = None
        self.auto_scan_check = QCheckBox("Auto-scan on startup")
        self.refresh_disks_btn = None  # Created in tabs.py
        # Placeholder for the green zoom button (assigned in create_title_bar)
        self.green_button = None
        self.log_viewer = QTextEdit()
        self.tray_icon = QSystemTrayIcon(self)
        self.fade_in = None
        self.scan_timer = None
        self.fade_out = None
        self.drag_position = None
        self.size_grip = None
        self.disk_scanner = DiskScanner(runner=self.runner)
        self.process_monitor = ProcessMonitor(runner=self.runner)
        self.selected_disks = []
        self.init_ui()
        self.init_system_tray()


if __name__ == "__main__":
    # Enable high DPI scaling before creating the application
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setApplicationName("XcodeFuckOff")
    app.setApplicationDisplayName("XcodeFuckOff")

    if sys.platform == "darwin":
        try:
            from Foundation import NSBundle
            bundle = NSBundle.mainBundle()
            info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
            if info:
                info["CFBundleName"] = "XcodeFuckOff"
        except ImportError:
            pass

    # Attempt to load tab_button_colors.qss for custom button styles
    try:
        with open("tab_button_colors.qss", "r") as file:
            qss = file.read()
            app.setStyleSheet(qss)
    except Exception as e:
        print(f"[WARNING] Failed to load QSS: {e}")


    window = EnhancedSimulatorKiller()
    window.show()

    sys.exit(app.exec())
