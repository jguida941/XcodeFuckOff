"""Reusable GUI widgets: buttons and stat cards."""

from PyQt6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QFrame, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QColor


class AccentButton(QPushButton):
	"""Primary action button with gradient styling from theme."""

	def __init__(self, text: str = "", parent=None):
		super().__init__(text, parent)
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.setObjectName("AccentButton")


class AnimatedButton(QPushButton):
	"""Button with glow effect on hover and bright flash on press."""
	def __init__(self, text: str, parent=None):
		super().__init__(text, parent)
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.setMinimumHeight(32)
		self.setMaximumWidth(120)

		# Create shadow effect for hover glow
		self._shadow = QGraphicsDropShadowEffect(self)
		self._shadow.setBlurRadius(0)
		self._shadow.setColor(QColor(0, 255, 170, 200))  # Accent color glow
		self._shadow.setOffset(0, 0)
		self.setGraphicsEffect(self._shadow)

	def enterEvent(self, event):
		# Add glow on hover
		self._shadow.setBlurRadius(20)
		self._shadow.setColor(QColor(0, 255, 170, 200))
		super().enterEvent(event)

	def leaveEvent(self, event):
		# Remove glow
		self._shadow.setBlurRadius(0)
		super().leaveEvent(event)

	def mousePressEvent(self, event):
		# Bright white glow on press
		self._shadow.setBlurRadius(25)
		self._shadow.setColor(QColor(255, 255, 255, 220))
		super().mousePressEvent(event)

	def mouseReleaseEvent(self, event):
		# Return to hover glow if still hovering
		if self.underMouse():
			self._shadow.setBlurRadius(20)
			self._shadow.setColor(QColor(0, 255, 170, 200))
		else:
			self._shadow.setBlurRadius(0)
		super().mouseReleaseEvent(event)


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
