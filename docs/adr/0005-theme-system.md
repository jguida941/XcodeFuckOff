# ADR 0005: Theme System with Qt Stylesheets

Status: Accepted
Date: 2024-12-27
Developer: Justin Guida

## Context
The app needed a consistent dark theme with multiple color variants. Options considered:
1. Hardcoded colors in each widget
2. QPalette-based theming
3. Qt Stylesheet (QSS) based theming

Hardcoded colors are inflexible. QPalette works but is limited to standard roles and doesn't support gradients or complex styling.

## Decision
Use Qt Stylesheets (QSS) with a theme dictionary system:

1. **Theme Definitions**: Each theme is a dict of color values in `styles.py`:
```python
THEMES = {
    "Neon": {
        "bg": "#121212",
        "accent": "#00FFAA",
        "destructive": "#FF4500",
        ...
    },
    "Cyber Red": { ... },
}
```

2. **Stylesheet Generation**: `get_stylesheet(theme_name)` generates a complete QSS string using f-string interpolation:
```python
return f"""
QWidget {{ background: {t['bg']}; }}
QPushButton#AccentButton {{
    background: qlineargradient(...{t['destructive']}...);
}}
"""
```

3. **Widget ObjectNames**: Widgets use `setObjectName()` to enable targeted styling:
```python
btn.setObjectName("AccentButton")  # Matches QPushButton#AccentButton
```

4. **Theme Switching**: `LoggingMixin.switch_theme()` calls `setStyleSheet()` on the main window.

## Consequences
- Adding a theme = adding a dict entry (no code changes needed)
- All colors are centralized in one file
- Gradient buttons, hover effects, and complex styling are supported
- ObjectName selectors allow precise targeting without subclassing
- Some Qt widgets (e.g., native dialogs) don't fully respect QSS
- Large stylesheet string (~500 lines) but it's generated, not hand-written

## Themes
- **Neon**: Dark with cyan/teal accent (default)
- **Cyber Red**: Dark with red/orange gradient
- **Electric Blue**: Dark with electric blue accent
- **Purple Haze**: Dark purple with gold accents
- **Forest & Gold**: Luxe forest green with gold buttons

## Notes
- Theme state is stored in module-level `_current_theme` variable
- `get_theme_names()` returns list for populating the theme menu
- AnimatedButton uses QGraphicsDropShadowEffect for hover glow (not QSS)
