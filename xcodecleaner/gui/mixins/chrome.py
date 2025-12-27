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
		"""Create a minimal title bar that integrates with native traffic lights."""
		title_bar = QFrame()
		title_bar.setFixedHeight(32)
		title_bar.setStyleSheet("QFrame { background: transparent; border: none; }")
		title_bar_layout = QHBoxLayout(title_bar)
		title_bar_layout.setContentsMargins(80, 0, 15, 0)  # Left margin for native traffic lights

		# Title (centered) - styled by theme stylesheet
		title = QLabel("Xcode Disk Ejector Utility")
		title.setObjectName("TitleLabel")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)

		# Menu button - larger and more visible
		menu_btn = QPushButton("Menu")
		menu_btn.setObjectName("MenuButton")
		menu_btn.setFixedSize(80, 28)
		menu_btn.setStyleSheet(
			"""
			QPushButton#MenuButton {
				background: rgba(255, 255, 255, 0.1);
				color: #EEE;
				font-size: 13px;
				font-weight: 500;
				border: 1px solid rgba(255, 255, 255, 0.2);
				border-radius: 6px;
				min-height: 0;
				padding: 4px 12px;
			}
			QPushButton#MenuButton:hover {
				background: rgba(255, 255, 255, 0.2);
				color: white;
				border-color: rgba(255, 255, 255, 0.35);
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
		"""Configure native macOS window with transparent title bar."""
		if not HAS_PYOBJC:
			return

		try:
			# Get the NSWindow from PyQt window
			win_id = int(self.winId())
			ns_view = objc.objc_object(c_void_p=win_id)
			ns_window = ns_view.window()

			if ns_window is None:
				return

			# Make title bar transparent so our dark theme shows through
			ns_window.setTitlebarAppearsTransparent_(True)

			# Hide the window title text (we have our own)
			ns_window.setTitleVisibility_(1)  # NSWindowTitleHidden

			# Make content extend into title bar area
			ns_window.setStyleMask_(ns_window.styleMask() | (1 << 15))  # NSWindowStyleMaskFullSizeContentView

			# Set window background to match our theme
			try:
				from AppKit import NSColor
				ns_window.setBackgroundColor_(NSColor.colorWithRed_green_blue_alpha_(
					0x12/255, 0x12/255, 0x12/255, 1.0
				))
			except Exception:
				pass

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


