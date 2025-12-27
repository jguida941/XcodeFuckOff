def get_advanced_stylesheet() -> str:
	return """
	QFrame#MainContainer {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(28, 28, 30, 240),
			stop:0.5 rgba(44, 44, 46, 240),
			stop:1 rgba(28, 28, 30, 240));
		border-radius: 12px;
		border: 1px solid rgba(255, 255, 255, 0.1);
	}

	QLabel#TitleLabel {
		color: white;
		font-size: 18px;
		font-weight: bold;
		padding: 10px;
		background: transparent;
	}

	QPushButton {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(255, 59, 48, 200),
			stop:1 rgba(255, 45, 35, 200));
		color: white;
		border: none;
		border-radius: 8px;
		padding: 10px 20px;
		font-weight: 600;
		font-size: 14px;
	}

	QPushButton:hover {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(255, 69, 58, 255),
			stop:1 rgba(255, 55, 45, 255));
	}

	QPushButton:pressed {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(200, 50, 40, 255),
			stop:1 rgba(180, 40, 30, 255));
	}

	QPushButton#RefreshButton {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(10, 132, 255, 200),
			stop:1 rgba(0, 122, 255, 200));
	}

	QPushButton#RefreshButton:hover {
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
			stop:0 rgba(20, 142, 255, 255),
			stop:1 rgba(10, 132, 255, 255));
	}

	QTabWidget#MainTabs {
		background: transparent;
		border: none;
	}

	QTabWidget::pane {
		background: rgba(44, 44, 46, 100);
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 8px;
		padding: 10px;
	}

	QTabBar::tab {
		background: rgba(72, 72, 74, 150);
		color: rgba(255, 255, 255, 0.7);
		padding: 10px 20px;
		margin-right: 5px;
		border-top-left-radius: 8px;
		border-top-right-radius: 8px;
		font-weight: 500;
	}

	QTabBar::tab:selected {
		background: rgba(99, 99, 102, 200);
		color: white;
	}

	QListWidget {
		background: rgba(30, 30, 32, 200);
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 8px;
		padding: 5px;
		color: white;
		font-size: 13px;
	}

	QListWidget::item {
		padding: 8px;
		margin: 2px;
		border-radius: 6px;
		background: rgba(72, 72, 74, 100);
	}

	QListWidget::item:selected {
		background: rgba(10, 132, 255, 150);
	}

	QListWidget::item:hover {
		background: rgba(99, 99, 102, 150);
	}

	QTableWidget {
		background: rgba(30, 30, 32, 200);
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 8px;
		gridline-color: rgba(255, 255, 255, 0.05);
		color: white;
	}

	QTableWidget::item {
		padding: 5px;
	}

	QHeaderView::section {
		background: rgba(58, 58, 60, 200);
		color: white;
		padding: 8px;
		border: none;
		font-weight: 600;
	}

	QTextEdit {
		background: rgba(30, 30, 32, 200);
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 8px;
		color: #00ff00;
		font-family: 'Menlo', 'Monaco', monospace;
		font-size: 12px;
		padding: 10px;
	}

	QProgressBar {
		background: rgba(72, 72, 74, 200);
		border: none;
		border-radius: 4px;
		height: 8px;
		text-align: center;
	}

	QProgressBar::chunk {
		background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
			stop:0 rgba(52, 199, 89, 255),
			stop:1 rgba(48, 209, 88, 255));
		border-radius: 4px;
	}

	QCheckBox {
		color: white;
		spacing: 8px;
	}

	QCheckBox::indicator {
		width: 18px;
		height: 18px;
		border: 2px solid rgba(255, 255, 255, 0.3);
		border-radius: 4px;
		background: rgba(72, 72, 74, 200);
	}

	QCheckBox::indicator:checked {
		background: rgba(48, 209, 88, 255);
		border-color: rgba(48, 209, 88, 255);
	}

	QLineEdit {
		background: rgba(72, 72, 74, 200);
		border: 1px solid rgba(255, 255, 255, 0.2);
		border-radius: 6px;
		padding: 8px;
		color: white;
		font-size: 14px;
	}

	QLineEdit:focus {
		border-color: rgba(10, 132, 255, 255);
	}

	QGroupBox {
		color: rgba(255, 255, 255, 0.9);
		font-weight: 600;
		border: 1px solid rgba(255, 255, 255, 0.1);
		border-radius: 8px;
		margin-top: 10px;
		padding-top: 10px;
	}

	QGroupBox::title {
		subcontrol-origin: margin;
		left: 10px;
		padding: 0 10px 0 10px;
	}
	"""


