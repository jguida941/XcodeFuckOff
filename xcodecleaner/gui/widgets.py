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
	"""Create a stat card widget. Styling is handled by the theme stylesheet."""
	widget = QFrame()
	widget.setObjectName("StatCard")

	layout = QVBoxLayout(widget)
	layout.setContentsMargins(12, 10, 12, 10)
	layout.setSpacing(4)

	title_label = QLabel(title)
	title_label.setObjectName("StatCardTitle")
	layout.addWidget(title_label)

	value_label = QLabel(value)
	value_label.setObjectName(f"{title.replace(' ', '')}Value")
	value_label.setProperty("class", "stat-value")
	layout.addWidget(value_label)

	return widget
