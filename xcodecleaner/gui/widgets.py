from PyQt6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QCursor


class AccentButton(QPushButton):
	def __init__(self, text: str = "", parent=None):
		super().__init__(text, parent)
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.setObjectName("AccentButton")


class AnimatedButton(QPushButton):
	def __init__(self, text: str, parent=None):
		super().__init__(text, parent)
		self.animation = QPropertyAnimation(self, b"geometry")
		self.animation.setDuration(200)
		self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

	def enterEvent(self, event):
		self.animation.setStartValue(self.geometry())
		self.animation.setEndValue(self.geometry().adjusted(-2, -2, 2, 2))
		self.animation.start()
		super().enterEvent(event)

	def leaveEvent(self, event):
		self.animation.setStartValue(self.geometry())
		self.animation.setEndValue(self.geometry().adjusted(2, 2, -2, -2))
		self.animation.start()
		super().leaveEvent(event)


def create_stat_widget(title: str, value: str) -> QFrame:
	widget = QFrame()
	widget.setStyleSheet("""
		QFrame {
			background: rgba(72, 72, 74, 150);
			border-radius: 8px;
			padding: 15px;
		}
	""")

	layout = QVBoxLayout(widget)

	title_label = QLabel(title)
	title_label.setStyleSheet("color: rgba(255, 255, 255, 0.6); font-size: 12px;")
	layout.addWidget(title_label)

	value_label = QLabel(value)
	value_label.setObjectName(f"{title}Value")
	value_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
	layout.addWidget(value_label)

	return widget


