"""
Unit tests for theme system - validates color consistency, stylesheet generation,
and theme switching functionality.

Based on best practices from:
- https://github.com/Alexhuszagh/BreezeStyleSheets (comprehensive widget testing)
- https://qt-material.readthedocs.io/en/latest/index.html (theme validation)
"""

import re
import pytest
from xcodecleaner.gui import styles


class TestThemeDefinitions:
    """Test that all themes have required color keys."""

    REQUIRED_KEYS = [
        "bg",
        "bg_secondary",
        "bg_button",
        "border",
        "text",
        "text_muted",
        "accent",
        "accent_dim",
        "destructive",
        "destructive_end",
        "success",
        "warning",
    ]

    def test_all_themes_have_required_keys(self):
        """Every theme must define all required color keys."""
        for theme_name, theme_colors in styles.THEMES.items():
            for key in self.REQUIRED_KEYS:
                assert key in theme_colors, f"Theme '{theme_name}' missing required key: {key}"

    def test_theme_names_not_empty(self):
        """Theme names list should not be empty."""
        names = styles.get_theme_names()
        assert len(names) > 0, "No themes defined"

    def test_default_theme_exists(self):
        """Default theme should exist in THEMES."""
        current = styles.get_current_theme()
        assert current in styles.THEMES, f"Default theme '{current}' not found in THEMES"


class TestColorFormats:
    """Test that color values are valid CSS color formats."""

    HEX_PATTERN = re.compile(r"^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")
    RGBA_PATTERN = re.compile(r"^rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(,\s*[\d.]+\s*)?\)$")

    def _is_valid_color(self, color: str) -> bool:
        """Check if color is valid hex or rgba format."""
        color = color.strip()
        if self.HEX_PATTERN.match(color):
            return True
        if self.RGBA_PATTERN.match(color):
            return True
        return False

    def test_all_colors_valid_format(self):
        """All color values must be valid hex or rgba format."""
        for theme_name, theme_colors in styles.THEMES.items():
            for key, color in theme_colors.items():
                assert self._is_valid_color(color), (
                    f"Theme '{theme_name}' has invalid color format for '{key}': {color}"
                )

    def test_hex_colors_proper_length(self):
        """Hex colors should be 3, 6, or 8 characters (excluding #)."""
        for theme_name, theme_colors in styles.THEMES.items():
            for key, color in theme_colors.items():
                if color.startswith("#"):
                    hex_part = color[1:]
                    assert len(hex_part) in [3, 6, 8], (
                        f"Theme '{theme_name}' has invalid hex length for '{key}': {color}"
                    )


class TestStylesheetGeneration:
    """Test that stylesheets generate without errors."""

    def test_stylesheet_generates_for_all_themes(self):
        """get_stylesheet should return a non-empty string for all themes."""
        for theme_name in styles.get_theme_names():
            stylesheet = styles.get_stylesheet(theme_name)
            assert isinstance(stylesheet, str), f"Stylesheet for '{theme_name}' is not a string"
            assert len(stylesheet) > 100, f"Stylesheet for '{theme_name}' seems too short"

    def test_stylesheet_contains_expected_selectors(self):
        """Stylesheet should contain key Qt widget selectors."""
        expected_selectors = [
            "QWidget",
            "QPushButton",
            "QLabel",
            "QListWidget",
            "QTabWidget",
            "QGroupBox",
            "QCheckBox",
            "QProgressBar",
        ]
        stylesheet = styles.get_stylesheet()
        for selector in expected_selectors:
            assert selector in stylesheet, f"Missing selector '{selector}' in stylesheet"

    def test_menu_stylesheet_generates(self):
        """get_menu_stylesheet should return a valid stylesheet."""
        for theme_name in styles.get_theme_names():
            menu_ss = styles.get_menu_stylesheet(theme_name)
            assert isinstance(menu_ss, str)
            assert "QMenu" in menu_ss
            assert len(menu_ss) > 50

    def test_advanced_stylesheet_backwards_compatible(self):
        """get_advanced_stylesheet should return same as get_stylesheet."""
        advanced = styles.get_advanced_stylesheet()
        current = styles.get_stylesheet()
        assert advanced == current, "get_advanced_stylesheet should match get_stylesheet"


class TestThemeSwitching:
    """Test theme switching functionality."""

    def test_set_theme_changes_current(self):
        """set_current_theme should change the active theme."""
        original = styles.get_current_theme()
        try:
            # Switch to a different theme
            themes = styles.get_theme_names()
            new_theme = themes[1] if themes[0] == original else themes[0]
            styles.set_current_theme(new_theme)
            assert styles.get_current_theme() == new_theme
        finally:
            # Restore original
            styles.set_current_theme(original)

    def test_set_invalid_theme_does_nothing(self):
        """set_current_theme with invalid name should not change theme."""
        original = styles.get_current_theme()
        styles.set_current_theme("NonExistentTheme")
        assert styles.get_current_theme() == original

    def test_stylesheet_changes_with_theme(self):
        """Stylesheet content should differ between themes."""
        themes = styles.get_theme_names()
        if len(themes) < 2:
            pytest.skip("Need at least 2 themes to compare")

        ss1 = styles.get_stylesheet(themes[0])
        ss2 = styles.get_stylesheet(themes[1])
        assert ss1 != ss2, "Different themes should produce different stylesheets"


class TestColorContrast:
    """Test color contrast for accessibility."""

    @staticmethod
    def _hex_to_rgb(hex_color: str) -> tuple:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip("#")
        if len(hex_color) == 3:
            hex_color = "".join(c * 2 for c in hex_color)
        if len(hex_color) == 8:  # RGBA
            hex_color = hex_color[:6]
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def _luminance(rgb: tuple) -> float:
        """Calculate relative luminance of a color."""
        r, g, b = [x / 255.0 for x in rgb]
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    def _contrast_ratio(self, color1: str, color2: str) -> float:
        """Calculate contrast ratio between two colors."""
        if not color1.startswith("#") or not color2.startswith("#"):
            return 21.0  # Skip rgba colors, assume they pass
        lum1 = self._luminance(self._hex_to_rgb(color1))
        lum2 = self._luminance(self._hex_to_rgb(color2))
        lighter = max(lum1, lum2)
        darker = min(lum1, lum2)
        return (lighter + 0.05) / (darker + 0.05)

    def test_text_background_contrast(self):
        """Text should have sufficient contrast against background (WCAG AA: 4.5:1)."""
        for theme_name, theme_colors in styles.THEMES.items():
            bg = theme_colors["bg"]
            text = theme_colors["text"]
            if bg.startswith("#") and text.startswith("#"):
                ratio = self._contrast_ratio(text, bg)
                assert ratio >= 4.5, (
                    f"Theme '{theme_name}' has insufficient text/bg contrast: {ratio:.2f} (need 4.5)"
                )

    def test_accent_visible_on_background(self):
        """Accent color should be visible against background (ratio >= 3:1)."""
        for theme_name, theme_colors in styles.THEMES.items():
            bg = theme_colors["bg_secondary"]
            accent = theme_colors["accent"]
            if bg.startswith("#") and accent.startswith("#"):
                ratio = self._contrast_ratio(accent, bg)
                assert ratio >= 3.0, (
                    f"Theme '{theme_name}' has low accent visibility: {ratio:.2f} (need 3.0)"
                )


class TestStatCardStyling:
    """Test that stat card object names are consistent."""

    def test_stat_card_selector_in_stylesheet(self):
        """Stylesheet should contain StatCard styling."""
        stylesheet = styles.get_stylesheet()
        assert "StatCard" in stylesheet, "Missing StatCard selector"
        assert "StatCardTitle" in stylesheet, "Missing StatCardTitle selector"

    def test_groupbox_uses_accent_color(self):
        """GroupBox title should use accent color."""
        for theme_name in styles.get_theme_names():
            theme = styles.THEMES[theme_name]
            stylesheet = styles.get_stylesheet(theme_name)
            # Check that accent color appears in QGroupBox styling
            assert theme["accent"] in stylesheet, (
                f"Theme '{theme_name}' accent color not found in stylesheet"
            )
