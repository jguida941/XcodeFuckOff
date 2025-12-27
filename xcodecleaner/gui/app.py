import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication

from .main_window import EnhancedSimulatorKiller


def main() -> int:
	# Enable high DPI scaling before creating the application
	QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

	app = QApplication(sys.argv)
	app.setApplicationName("Xcode Simulator Disk Ejector Utility")

	# Attempt to load tab_button_colors.qss for custom button styles (optional)
	try:
		with open("tab_button_colors.qss", "r", encoding="utf-8") as file:
			app.setStyleSheet(file.read())
	except Exception:
		pass

	window = EnhancedSimulatorKiller()
	window.show()
	return app.exec()


__all__ = ["main"]


