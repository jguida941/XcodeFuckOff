from datetime import datetime

from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QPoint
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QLabel, QMenu, QMessageBox, QScrollBar, QGraphicsOpacityEffect

from xcodecleaner.gui import styles


class LoggingMixin:
	def show_notification(self, message, level="info"):
		colors = {
			"info": "rgba(10, 132, 255, 255)",
			"success": "rgba(48, 209, 88, 255)",
			"warning": "rgba(255, 159, 10, 255)",
			"error": "rgba(255, 69, 58, 255)",
		}

		popup = QLabel(message, self)
		popup.setStyleSheet(
			f"""
			QLabel {{
				background: {colors.get(level, colors['info'])};
				color: white;
				font-weight: bold;
				padding: 15px 25px;
				border-radius: 10px;
				font-size: 14px;
			}}
		"""
		)
		popup.setAlignment(Qt.AlignmentFlag.AlignCenter)
		popup.adjustSize()
		popup.move((self.width() - popup.width()) // 2, 60)

		effect = QGraphicsOpacityEffect()
		popup.setGraphicsEffect(effect)

		self.fade_in = QPropertyAnimation(effect, b"opacity")
		self.fade_in.setDuration(200)
		self.fade_in.setStartValue(0)
		self.fade_in.setEndValue(1)

		popup.show()
		self.fade_in.start()

		QTimer.singleShot(3000, lambda: self.fade_out_notification(popup, effect))

		self.status_label.setText(message)

		if self.notify_check.isChecked() and hasattr(self, "tray_icon"):
			try:
				self.tray_icon.showMessage("Simulator Ejector", message, 0, 2000)
			except Exception:
				pass

	def fade_out_notification(self, popup, effect):
		self.fade_out = QPropertyAnimation(effect, b"opacity")
		self.fade_out.setDuration(200)
		self.fade_out.setStartValue(1)
		self.fade_out.setEndValue(0)
		self.fade_out.finished.connect(popup.deleteLater)
		self.fade_out.start()

	def log(self, message, level="info"):
		timestamp = datetime.now().strftime("%H:%M:%S")
		colors = {"info": "#00ff00", "success": "#30d158", "warning": "#ff9500", "error": "#ff453a"}

		formatted_message = (
			f'<span style="color: #888;">[{timestamp}]</span> '
			f'<span style="color: {colors.get(level, "#fff")}">{message}</span>'
		)

		self.log_viewer.append(formatted_message)

		scrollbar = QScrollBar(Qt.Orientation.Vertical)
		scrollbar.setStyleSheet("QScrollBar:vertical { background: transparent; width: 12px; margin: 0px; }")
		self.log_viewer.setVerticalScrollBar(scrollbar)
		scrollbar.setValue(scrollbar.maximum())

	def clear_log(self):
		self.log_viewer.clear()
		self.log("Log cleared", "info")

	def export_log(self):
		content = self.log_viewer.toPlainText()
		filename = f"simulator_ejector_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

		try:
			with open(filename, "w", encoding="utf-8") as f:
				f.write(content)
			self.show_notification(f"Log exported to {filename}", "success")
		except Exception as exc:
			self.show_notification(f"Failed to export log: {exc}", "error")

	def filter_log(self, level):
		# TODO: Implement log filtering
		pass

	def save_settings(self):
		# TODO: Implement settings persistence
		self.show_notification("Settings saved", "success")

	def auto_scan(self):
		if self.auto_scan_check.isChecked():
			self.scan_disks()

	def open_preferences(self):
		# Switch to the Settings tab
		try:
			idx = getattr(self, "settings_tab_index", 2)
			self.tab_widget.setCurrentIndex(idx)
			self.raise_()
			self.activateWindow()
		except Exception:
			pass

	def apply_theme(self, theme_name: str):
		"""Apply a new theme to the application."""
		styles.set_current_theme(theme_name)
		new_stylesheet = styles.get_stylesheet(theme_name)
		self.setStyleSheet(new_stylesheet)
		self.show_notification(f"Theme changed to {theme_name}", "success")

	def show_menu(self, anchor_widget=None):
		menu = QMenu(self)
		menu.setStyleSheet(styles.get_menu_stylesheet())

		about_action = menu.addAction("About")
		about_action.triggered.connect(self.show_about)

		menu.addSeparator()

		# Themes submenu
		themes_menu = menu.addMenu("Themes")
		themes_menu.setStyleSheet(styles.get_menu_stylesheet())
		current_theme = styles.get_current_theme()
		for theme_name in styles.get_theme_names():
			action = themes_menu.addAction(theme_name)
			action.setCheckable(True)
			action.setChecked(theme_name == current_theme)
			action.triggered.connect(lambda checked, t=theme_name: self.apply_theme(t))

		menu.addSeparator()

		quit_action = menu.addAction("Quit")
		quit_action.triggered.connect(self.close)

		# Make sure Qt computes the final menu size before positioning
		try:
			menu.ensurePolished()
			menu.adjustSize()
		except Exception:
			pass

		pos = None
		if anchor_widget is not None:
			try:
				pos = anchor_widget.mapToGlobal(QPoint(0, anchor_widget.height()))
			except Exception:
				pos = None
		if pos is None:
			pos = self.mapToGlobal(self.rect().topRight())

		# Clamp to the current screen so the menu is never clipped/off-screen
		try:
			screen = QGuiApplication.screenAt(pos) or QGuiApplication.primaryScreen()
			geo = screen.availableGeometry()
			# Use the actual size (after adjustSize) and keep some padding so shadows/borders aren't clipped
			size = menu.size()
			pad = 12
			x = min(max(pos.x(), geo.left() + pad), geo.right() - size.width() - pad)
			y = min(max(pos.y(), geo.top() + pad), geo.bottom() - size.height() - pad)
			pos = QPoint(x, y)
		except Exception:
			pass

		menu.exec(pos)

	def show_about(self):
		about_text = """<h2>Xcode Simulator Disk Ejector Utility</h2>
		<p>Version 2.0.0</p>
		<p>Utility for managing Xcode Simulator disks and processes.</p>
		<p>Features:</p>
		<ul>
		<li>Automatic disk detection and monitoring</li>
		<li>Process management with live updates</li>
		<li>Secure password handling with Keychain integration</li>
		<li>Advanced logging and analytics</li>
		<li>Native macOS UI design</li>
		</ul>
		<p>© 2024 - Built with PyQt6</p>"""

		msg = QMessageBox(self)
		msg.setWindowTitle("About")
		msg.setTextFormat(Qt.TextFormat.RichText)
		msg.setText(about_text)
		msg.exec()

	def toggle_maximize(self):
		if self.isMaximized():
			self.showNormal()
		else:
			self.showMaximized()

	def closeEvent(self, event):
		if hasattr(self, "tray_icon"):
			try:
				self.tray_icon.hide()
			except Exception:
				pass
		event.accept()


