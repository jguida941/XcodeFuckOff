"""Application entry point and macOS menu bar configuration."""

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication

from .main_window import EnhancedSimulatorKiller

APP_NAME = "XcodeFuckOff"


def _set_macos_app_name():
	"""Set the application name in macOS menu bar and dock."""
	try:
		from Foundation import NSBundle
		from AppKit import NSApplication

		# Set bundle name
		bundle = NSBundle.mainBundle()
		info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
		if info:
			info["CFBundleName"] = APP_NAME
			info["CFBundleDisplayName"] = APP_NAME

	except Exception:
		pass


def _update_macos_menus():
	"""Update macOS app menu items after Qt has created them."""
	try:
		from AppKit import NSApplication

		ns_app = NSApplication.sharedApplication()
		main_menu = ns_app.mainMenu()
		if main_menu and main_menu.numberOfItems() > 0:
			app_menu_item = main_menu.itemAtIndex_(0)
			if app_menu_item:
				app_menu = app_menu_item.submenu()
				if app_menu:
					app_menu.setTitle_(APP_NAME)
					# Update menu items that reference the app name
					for i in range(app_menu.numberOfItems()):
						item = app_menu.itemAtIndex_(i)
						if item and item.title():
							title = item.title()
							if "Quit" in title:
								item.setTitle_(f"Quit {APP_NAME}")
							elif "Hide" in title and "Others" not in title:
								item.setTitle_(f"Hide {APP_NAME}")
							elif "About" in title:
								item.setTitle_(f"About {APP_NAME}")
	except Exception:
		pass


def main() -> int:
	# Enable high DPI scaling before creating the application
	QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

	app = QApplication(sys.argv)
	app.setApplicationName(APP_NAME)
	app.setApplicationDisplayName(APP_NAME)

	# On macOS, set the app name for the menu bar
	if sys.platform == "darwin":
		_set_macos_app_name()

	# Attempt to load tab_button_colors.qss for custom button styles (optional)
	try:
		with open("tab_button_colors.qss", "r", encoding="utf-8") as file:
			app.setStyleSheet(file.read())
	except Exception:
		pass

	window = EnhancedSimulatorKiller()
	window.show()

	# On macOS, update menus after Qt has created them
	if sys.platform == "darwin":
		from PyQt6.QtCore import QTimer
		QTimer.singleShot(100, _update_macos_menus)

	return app.exec()


__all__ = ["main"]
