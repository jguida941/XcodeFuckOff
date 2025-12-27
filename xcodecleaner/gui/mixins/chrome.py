import sys
from ctypes import c_void_p
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (
	QFrame,
	QPushButton,
	QHBoxLayout,
	QLabel,
	QWidget,
)

# Native macOS window button support
if sys.platform == "darwin":
	try:
		from AppKit import NSWindow, NSWindowStyleMask, NSView
		from Cocoa import NSMakeRect
		import objc
		HAS_PYOBJC = True
	except ImportError:
		HAS_PYOBJC = False
else:
	HAS_PYOBJC = False


class ChromeMixin:
	def _qwidget_fallback(self, method_name: str, event) -> None:
		"""
		In PyQt, base class event handlers aren't always discoverable via Python MRO.
		When this mixin implements an event handler, `super()` may not have the Qt method.
		So we explicitly call QWidget.<event>() when available.
		"""
		fn = getattr(QWidget, method_name, None)
		if fn is None:
			return
		try:
			fn(self, event)
		except Exception:
			# best-effort fallback; never crash the app on event propagation
			return
	def create_title_bar(self, layout):
		"""Create a title bar that sits below the native Apple title bar."""
		title_bar = QFrame()
		title_bar.setFixedHeight(36)
		title_bar.setStyleSheet("QFrame { background: transparent; border: none; }")
		title_bar_layout = QHBoxLayout(title_bar)
		title_bar_layout.setContentsMargins(15, 4, 15, 0)

		# Title (centered) - styled by theme stylesheet
		title = QLabel("Xcode Disk Ejector Utility")
		title.setObjectName("TitleLabel")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)

		# Menu button
		menu_btn = QPushButton("Menu")
		menu_btn.setObjectName("MenuButton")
		menu_btn.setFixedSize(70, 26)
		menu_btn.setStyleSheet(
			"""
			QPushButton#MenuButton {
				background: transparent;
				color: white;
				font-size: 14px;
				font-weight: 500;
				border: none;
				min-height: 0;
				padding: 4px 12px;
			}
			QPushButton#MenuButton:hover {
				color: white;
				background: rgba(255, 255, 255, 0.15);
				border-radius: 4px;
			}
		"""
		)
		self.menu_button = menu_btn
		menu_btn.clicked.connect(lambda: self.show_menu(anchor_widget=self.menu_button))

		title_bar_layout.addWidget(title, 1)
		title_bar_layout.addWidget(menu_btn)

		layout.addWidget(title_bar)

		# Store reference
		self.title_bar = title_bar

		# Setup native macOS window styling after window is shown
		QTimer.singleShot(50, self._setup_native_window_style)

	def _setup_native_window_style(self):
		"""Configure native macOS window - keep standard Apple title bar."""
		if not HAS_PYOBJC:
			return

		try:
			# Get the NSWindow from PyQt window
			win_id = int(self.winId())
			ns_view = objc.objc_object(c_void_p=win_id)
			ns_window = ns_view.window()

			if ns_window is None:
				return

			# Hide the window title text (we have our own centered title)
			ns_window.setTitleVisibility_(1)  # NSWindowTitleHidden

		except Exception as e:
			print(f"[WARNING] Failed to setup native window style: {e}")

	def toggle_maximized(self):
		if self.isMaximized():
			self.showNormal()
		else:
			self.showMaximized()

	def resizeEvent(self, event):
		# Keep the translucent container filling the window
		try:
			self.container.setGeometry(0, 0, self.width(), self.height())
		except Exception:
			pass
		self._qwidget_fallback("resizeEvent", event)


