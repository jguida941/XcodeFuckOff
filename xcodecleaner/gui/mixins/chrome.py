from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import (
	QCheckBox,
	QComboBox,
	QFrame,
	QLineEdit,
	QListWidget,
	QMenu,
	QPushButton,
	QScrollBar,
	QSizeGrip,
	QSlider,
	QSpinBox,
	QTableWidget,
	QTextEdit,
	QHBoxLayout,
	QLabel,
	QWidget,
)


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
		title_bar = QFrame()
		title_bar.setFixedHeight(50)
		title_bar.setStyleSheet("QFrame { background: transparent; border: none; }")
		title_bar_layout = QHBoxLayout(title_bar)
		title_bar_layout.setContentsMargins(15, 0, 15, 0)

		# Window controls (macOS style: left-aligned)
		controls_layout = QHBoxLayout()
		controls_layout.setSpacing(8)

		# Red (close)
		close_btn = QPushButton()
		close_btn.setFixedSize(14, 14)
		close_btn.setStyleSheet(
			"""
			QPushButton {
				background: #FF5F56;
				border-radius: 7px;
				border: none;
				padding: 0;
				min-width: 0;
				max-width: 14px;
				max-height: 14px;
			}
			QPushButton:hover {
				background: #FF8980;
			}
		"""
		)
		close_btn.clicked.connect(self.close)

		# Yellow (minimize)
		min_btn = QPushButton()
		min_btn.setFixedSize(14, 14)
		min_btn.setStyleSheet(
			"""
			QPushButton {
				background: #FFBD2E;
				border-radius: 7px;
				border: none;
				padding: 0;
				min-width: 0;
				max-width: 14px;
				max-height: 14px;
			}
			QPushButton:hover {
				background: #FDD663;
			}
		"""
		)
		min_btn.clicked.connect(self.showMinimized)

		# Green (tile/maximize/zoom)
		green_btn = QPushButton()
		green_btn.setFixedSize(14, 14)
		green_btn.setStyleSheet(
			"""
			QPushButton {
				background: #28C840;
				border-radius: 7px;
				border: none;
				padding: 0;
				min-width: 0;
				max-width: 14px;
				max-height: 14px;
			}
			QPushButton:hover {
				background: #42D85C;
			}
		"""
		)
		green_btn.clicked.connect(self.show_mac_zoom_menu)
		self.green_button = green_btn

		controls_layout.addWidget(close_btn)
		controls_layout.addWidget(min_btn)
		controls_layout.addWidget(green_btn)
		controls_layout.addSpacing(10)

		# Title
		title = QLabel("Xcode Simulator Disk Ejector Utility")
		title.setObjectName("TitleLabel")
		title.setAlignment(Qt.AlignmentFlag.AlignCenter)

		# Menu button
		menu_btn = QPushButton("Menu")
		menu_btn.setFixedSize(80, 30)
		menu_btn.setStyleSheet(
			"""
			QPushButton {
				background: transparent;
				color: white;
				font-size: 14px;
				border: none;
			}
			QPushButton:hover {
				background: rgba(255, 255, 255, 0.1);
				border-radius: 4px;
			}
		"""
		)
		self.menu_button = menu_btn
		menu_btn.clicked.connect(lambda: self.show_menu(anchor_widget=self.menu_button))

		title_bar_layout.addLayout(controls_layout)
		title_bar_layout.addWidget(title, 1)
		title_bar_layout.addWidget(menu_btn)

		layout.addWidget(title_bar)

		# Make window draggable (macOS style)
		self.title_bar = title_bar
		self.title_bar.mousePressEvent = self.title_bar_mouse_press
		self.title_bar.mouseMoveEvent = self.title_bar_mouse_move

	def toggle_maximized(self):
		if self.isMaximized():
			self.showNormal()
		else:
			self.showMaximized()

	# --- window dragging (works even outside title bar) ---
	def _is_descendant_of(self, widget, ancestor) -> bool:
		w = widget
		while w is not None:
			if w is ancestor:
				return True
			w = w.parent()
		return False

	def _is_drag_allowed_for_widget(self, widget) -> bool:
		# If you click the title bar (or its children), always allow dragging
		if widget is not None and hasattr(self, "title_bar") and self.title_bar is not None:
			if self._is_descendant_of(widget, self.title_bar):
				return True

		if widget is None:
			return True

		# Don't start drag from interactive controls
		if isinstance(
			widget,
			(
				QPushButton,
				QLineEdit,
				QTextEdit,
				QCheckBox,
				QComboBox,
				QSpinBox,
				QSlider,
				QListWidget,
				QTableWidget,
				QSizeGrip,
				QScrollBar,
			),
		):
			return False

		# QTabBar isn't imported, so detect by class name
		try:
			if widget.metaObject().className() == "QTabBar":
				return False
		except Exception:
			pass

		return True

	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.LeftButton:
			target = self.childAt(event.position().toPoint())
			if self._is_drag_allowed_for_widget(target):
				self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
				event.accept()
				return
		self._qwidget_fallback("mousePressEvent", event)

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
			self.move(event.globalPosition().toPoint() - self.drag_position)
			event.accept()
			return
		self._qwidget_fallback("mouseMoveEvent", event)

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.MouseButton.LeftButton:
			self.drag_position = None
		self._qwidget_fallback("mouseReleaseEvent", event)

	def resizeEvent(self, event):
		# Keep the translucent container filling the window
		try:
			self.container.setGeometry(0, 0, self.width(), self.height())
		except Exception:
			pass

		# Keep the resize grip in the bottom-right corner
		if getattr(self, "size_grip", None) is not None:
			self.size_grip.move(self.width() - self.size_grip.width() - 6, self.height() - self.size_grip.height() - 6)
		self._qwidget_fallback("resizeEvent", event)

	# --- macOS-style drag-to-move and green-zoom dropdown ---
	def title_bar_mouse_press(self, event):
		if event.button() == Qt.MouseButton.LeftButton:
			self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
			event.accept()

	def title_bar_mouse_move(self, event):
		if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position is not None:
			self.move(event.globalPosition().toPoint() - self.drag_position)
			event.accept()

	def show_mac_zoom_menu(self):
		menu = QMenu(self)

		tile_left = menu.addAction("Tile Left")
		tile_left.triggered.connect(lambda: self.resize_to_half("left"))

		tile_right = menu.addAction("Tile Right")
		tile_right.triggered.connect(lambda: self.resize_to_half("right"))

		full_screen = menu.addAction("Full Screen")
		full_screen.triggered.connect(self.showFullScreen)

		menu.exec(self.green_button.mapToGlobal(QPoint(0, self.green_button.height())))

	def resize_to_half(self, side: str):
		screen = QGuiApplication.primaryScreen().geometry()
		if side == "left":
			self.setGeometry(screen.x(), screen.y(), screen.width() // 2, screen.height())
		elif side == "right":
			self.setGeometry(screen.x() + screen.width() // 2, screen.y(), screen.width() // 2, screen.height())


