# Theme definitions for XcodeCleaner
# Futuristic dark theme with neon accents
from typing import Dict

THEMES: Dict[str, Dict[str, str]] = {
	"Neon": {
		# Futuristic dark with cyan accent
		"bg": "#121212",
		"bg_secondary": "#1E1E1E",
		"bg_button": "#1F1F1F",
		"border": "#2D2D2D",
		"text": "#EEE",
		"text_muted": "#888",
		"accent": "#00FFAA",
		"accent_dim": "#00CC88",
		"destructive": "#FF4500",
		"destructive_end": "#FFD700",
		"success": "#00FFAA",
		"warning": "#FFD700",
	},
	"Cyber Red": {
		# Dark with red/orange gradient accent
		"bg": "#0D0D0D",
		"bg_secondary": "#1A1A1A",
		"bg_button": "#1F1F1F",
		"border": "#333333",
		"text": "#F0F0F0",
		"text_muted": "#888",
		"accent": "#FF3366",
		"accent_dim": "#CC2952",
		"destructive": "#FF3366",
		"destructive_end": "#FF6633",
		"success": "#00FF88",
		"warning": "#FFAA00",
	},
	"Electric Blue": {
		# Dark with electric blue accent
		"bg": "#0A0A12",
		"bg_secondary": "#12121F",
		"bg_button": "#1A1A2E",
		"border": "#2A2A40",
		"text": "#E8E8FF",
		"text_muted": "#8888AA",
		"accent": "#00D4FF",
		"accent_dim": "#00A8CC",
		"destructive": "#FF4466",
		"destructive_end": "#FF8844",
		"success": "#00FFAA",
		"warning": "#FFCC00",
	},
	"Purple Haze": {
		# Dark purple with gold/yellow buttons
		"bg": "#0D0A12",
		"bg_secondary": "#16121F",
		"bg_button": "#1E1A2A",
		"border": "#2D2640",
		"text": "#F0E8FF",
		"text_muted": "#9988AA",
		"accent": "#AA66FF",
		"accent_dim": "#8844DD",
		"destructive": "#FFB800",
		"destructive_end": "#FFD54F",
		"success": "#66FFAA",
		"warning": "#FFB800",
	},
	"Matrix": {
		# Classic terminal style - orange/amber text for readability
		"bg": "#0A0F0A",
		"bg_secondary": "#0F160F",
		"bg_button": "#142014",
		"border": "#1F2F1F",
		"text": "#FFAA00",  # Amber/orange text - easier on eyes
		"text_muted": "#AA7700",
		"accent": "#00FF66",
		"accent_dim": "#00CC44",
		"destructive": "#FF4400",
		"destructive_end": "#FFAA00",
		"success": "#00FF00",  # Log text stays green
		"warning": "#FFCC00",
	},
}

_current_theme = "Neon"


def get_current_theme() -> str:
	return _current_theme


def set_current_theme(theme_name: str) -> None:
	global _current_theme
	if theme_name in THEMES:
		_current_theme = theme_name


def get_theme_names() -> list:
	return list(THEMES.keys())


def get_stylesheet(theme_name: str = None) -> str:
	if theme_name is None:
		theme_name = _current_theme
	t = THEMES.get(theme_name, THEMES["Neon"])

	return f"""
	QWidget {{
		background: {t['bg']};
		color: {t['text']};
		font-family: -apple-system, BlinkMacSystemFont, '.SFNSText-Regular', sans-serif;
	}}

	QFrame#MainContainer {{
		background: {t['bg']};
		border: none;
	}}

	QLabel {{
		color: {t['text']};
		background: transparent;
	}}

	QLabel#TitleLabel {{
		color: {t['destructive']};
		font-size: 18px;
		font-weight: bold;
		padding: 2px;
		background: transparent;
	}}

	/* Stat cards */
	QFrame#StatCard {{
		background: {t['bg_secondary']};
		border: 1px solid {t['accent']};
		border-radius: 8px;
		padding: 10px;
	}}

	QLabel#StatCardTitle {{
		color: {t['accent']};
		font-size: 12px;
		font-weight: 500;
		background: transparent;
	}}

	QLabel[class="stat-value"] {{
		color: {t['text']};
		font-size: 28px;
		font-weight: bold;
		background: transparent;
	}}

	/* General buttons - exclude window controls */
	QPushButton {{
		background: {t['bg_button']};
		border: 2px solid {t['border']};
		border-radius: 8px;
		padding: 10px 20px;
		min-height: 20px;
		color: {t['text']};
		font-weight: 500;
		font-size: 13px;
	}}

	QPushButton:hover {{
		border-color: {t['accent']};
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
			stop:0 {t['bg_button']}, stop:1 #2F2F2F);
	}}

	QPushButton:pressed {{
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
			stop:0 #2F2F2F, stop:1 {t['bg_button']});
	}}

	QPushButton:disabled {{
		background: {t['bg_secondary']};
		border-color: {t['border']};
		color: {t['text_muted']};
	}}

	/* Accent buttons */
	QPushButton#AccentButton,
	QPushButton#ScanDisksButton,
	QPushButton#EjectSelectedButton,
	QPushButton#FreeRuntimeSpaceButton,
	QPushButton#NuclearOptionButton {{
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
			stop:0 {t['destructive']}, stop:1 {t['destructive_end']});
		color: #000;
		font-weight: bold;
		border: none;
		padding: 12px 24px;
		min-height: 20px;
	}}

	QPushButton#AccentButton:hover,
	QPushButton#ScanDisksButton:hover,
	QPushButton#EjectSelectedButton:hover,
	QPushButton#FreeRuntimeSpaceButton:hover,
	QPushButton#NuclearOptionButton:hover {{
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
			stop:0 {t['destructive_end']}, stop:1 {t['destructive']});
		border: 2px solid {t['accent']};
	}}

	/* Refresh/secondary buttons - green with orange outline on hover */
	QPushButton#RefreshButton,
	QPushButton#RefreshDisksButton,
	QPushButton#RefreshProcessesButton,
	QPushButton#SaveButton {{
		background: {t['accent']};
		color: #000;
		font-weight: bold;
		font-size: 13px;
		border: 2px solid transparent;
		border-radius: 8px;
		padding: 6px 16px;
		min-height: 16px;
	}}

	QPushButton#RefreshButton:hover,
	QPushButton#RefreshDisksButton:hover,
	QPushButton#RefreshProcessesButton:hover,
	QPushButton#SaveButton:hover {{
		background: {t['accent']};
		border: 2px solid {t['destructive']};
	}}

	QPushButton#RefreshButton:pressed,
	QPushButton#RefreshDisksButton:pressed,
	QPushButton#RefreshProcessesButton:pressed,
	QPushButton#SaveButton:pressed {{
		background: {t['accent_dim']};
		border: 2px solid {t['destructive_end']};
	}}

	/* Tab widget */
	QTabWidget#MainTabs {{
		background: transparent;
		border: none;
	}}

	QTabWidget::pane {{
		border: 1px solid {t['border']};
		border-radius: 6px;
		background: {t['bg_secondary']};
		padding: 8px;
	}}

	QTabBar::tab {{
		background: {t['bg_button']};
		padding: 8px 16px;
		border: 1px solid {t['border']};
		border-radius: 4px;
		margin-right: 4px;
		color: {t['text_muted']};
	}}

	QTabBar::tab:selected {{
		background: #272727;
		border-bottom: 2px solid {t['accent']};
		color: {t['text']};
	}}

	QTabBar::tab:hover:!selected {{
		background: #2A2A2A;
		color: {t['text']};
	}}

	/* Group boxes */
	QGroupBox {{
		color: {t['accent']};
		font-weight: bold;
		font-size: 14px;
		border: 1px solid {t['border']};
		border-radius: 6px;
		margin-top: 14px;
		padding-top: 10px;
	}}

	QGroupBox::title {{
		subcontrol-origin: margin;
		subcontrol-position: top left;
		left: 10px;
		padding: 0 4px;
		background: transparent;
		color: {t['accent']};
	}}

	/* Lists */
	QListWidget {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 4px;
		color: {t['text']};
		outline: none;
	}}

	QListWidget::item {{
		padding: 8px;
		margin: 2px;
		border-radius: 4px;
	}}

	QListWidget::item:selected {{
		background: {t['accent']};
		color: #000;
	}}

	QListWidget::item:hover:!selected {{
		background: {t['bg_button']};
	}}

	/* Tables */
	QTableWidget {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		gridline-color: {t['border']};
		color: {t['text']};
		outline: none;
	}}

	QTableWidget::item {{
		padding: 8px 12px;
		min-height: 24px;
	}}

	QTableWidget::item:selected {{
		background: {t['accent']};
		color: #000;
		font-weight: bold;
	}}

	QHeaderView::section {{
		background: {t['bg_button']};
		color: {t['text']};
		padding: 8px;
		border: none;
		border-bottom: 1px solid {t['border']};
		font-weight: bold;
	}}

	/* Text areas / Log viewer */
	QTextEdit {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 8px;
		color: {t['success']};
		font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
		font-size: 11px;
	}}

	/* Progress bar */
	QProgressBar {{
		background: {t['bg_button']};
		border: 1px solid {t['border']};
		border-radius: 4px;
		height: 8px;
		text-align: center;
	}}

	QProgressBar::chunk {{
		background: {t['accent']};
		border-radius: 4px;
	}}

	/* Checkboxes */
	QCheckBox {{
		color: {t['text']};
		spacing: 6px;
		background: transparent;
	}}

	QCheckBox::indicator {{
		width: 16px;
		height: 16px;
		border: 2px solid {t['border']};
		border-radius: 4px;
		background: {t['bg_button']};
	}}

	QCheckBox::indicator:checked {{
		background: {t['accent']};
		border-color: {t['accent']};
	}}

	QCheckBox::indicator:hover {{
		border-color: {t['accent']};
	}}

	/* Input fields */
	QLineEdit {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 6px 10px;
		color: {t['text']};
	}}

	QLineEdit:focus {{
		border-color: {t['accent']};
	}}

	/* Spin boxes */
	QSpinBox {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 4px 8px;
		color: {t['text']};
	}}

	QSpinBox:focus {{
		border-color: {t['accent']};
	}}

	QSpinBox::up-button, QSpinBox::down-button {{
		background: {t['bg_button']};
		border: none;
		width: 16px;
	}}

	/* Combo boxes */
	QComboBox {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 6px 10px;
		color: {t['text']};
	}}

	QComboBox:focus {{
		border-color: {t['accent']};
	}}

	QComboBox::drop-down {{
		border: none;
		width: 20px;
	}}

	QComboBox QAbstractItemView {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		selection-background-color: {t['accent']};
		selection-color: #000;
	}}

	/* Scroll bars */
	QScrollBar:vertical {{
		border: none;
		background: {t['bg_secondary']};
		width: 10px;
		margin: 0;
	}}

	QScrollBar::handle:vertical {{
		background: {t['border']};
		min-height: 20px;
		border-radius: 5px;
	}}

	QScrollBar::handle:vertical:hover {{
		background: {t['accent']};
	}}

	QScrollBar::add-line:vertical,
	QScrollBar::sub-line:vertical,
	QScrollBar::add-page:vertical,
	QScrollBar::sub-page:vertical {{
		background: transparent;
		height: 0;
	}}

	QScrollBar:horizontal {{
		border: none;
		background: {t['bg_secondary']};
		height: 10px;
		margin: 0;
	}}

	QScrollBar::handle:horizontal {{
		background: {t['border']};
		min-width: 20px;
		border-radius: 5px;
	}}

	QScrollBar::handle:horizontal:hover {{
		background: {t['accent']};
	}}

	QScrollBar::add-line:horizontal,
	QScrollBar::sub-line:horizontal,
	QScrollBar::add-page:horizontal,
	QScrollBar::sub-page:horizontal {{
		background: transparent;
		width: 0;
	}}

	/* Tooltips */
	QToolTip {{
		background: {t['bg_button']};
		color: {t['text']};
		border: 1px solid {t['accent']};
		border-radius: 4px;
		padding: 4px 8px;
	}}

	/* Menus */
	QMenu {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 4px;
	}}

	QMenu::item {{
		color: {t['text']};
		padding: 8px 24px 8px 12px;
		border-radius: 4px;
	}}

	QMenu::item:selected {{
		background: {t['accent']};
		color: #000;
	}}

	QMenu::separator {{
		height: 1px;
		background: {t['border']};
		margin: 4px 8px;
	}}

	/* Message boxes */
	QMessageBox {{
		background: {t['bg']};
	}}

	QMessageBox QLabel {{
		color: {t['text']};
	}}

	QMessageBox QPushButton {{
		min-width: 80px;
	}}
	"""


def get_advanced_stylesheet() -> str:
	"""Backwards compatible - returns current theme stylesheet."""
	return get_stylesheet()


def get_menu_stylesheet(theme_name: str = None) -> str:
	"""Get stylesheet specifically for popup menus."""
	if theme_name is None:
		theme_name = _current_theme
	t = THEMES.get(theme_name, THEMES["Neon"])

	return f"""
	QMenu {{
		background: {t['bg_secondary']};
		border: 1px solid {t['border']};
		border-radius: 6px;
		padding: 4px;
	}}
	QMenu::item {{
		color: {t['text']};
		padding: 8px 32px 8px 12px;
		border-radius: 4px;
	}}
	QMenu::item:selected {{
		background: {t['accent']};
		color: #000;
	}}
	QMenu::separator {{
		height: 1px;
		background: {t['border']};
		margin: 4px 8px;
	}}
	"""
