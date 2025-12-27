"""Unit tests for the CLI interface."""
import sys
from unittest.mock import patch


class TestCLIParsing:
	"""Test CLI argument parsing."""

	def test_default_launches_gui(self):
		"""With no arguments, GUI should launch."""
		with patch("xcodecleaner.__main__.gui_main", return_value=0) as mock_gui:
			from xcodecleaner.__main__ import main

			with patch.object(sys, "argv", ["xcodecleaner"]):
				result = main()

			mock_gui.assert_called_once()
			assert result == 0

	def test_gui_flag_launches_gui(self):
		"""--gui flag should launch GUI."""
		with patch("xcodecleaner.__main__.gui_main", return_value=0) as mock_gui:
			from xcodecleaner.__main__ import main

			with patch.object(sys, "argv", ["xcodecleaner", "--gui"]):
				result = main()

			mock_gui.assert_called_once()
			assert result == 0

	def test_nuclear_flag_runs_cleanup(self):
		"""--nuclear flag should run headless cleanup."""
		with patch("xcodecleaner.__main__.gui_main") as mock_gui:
			with patch("xcodecleaner.__main__.cmd_nuclear", return_value=0) as mock_nuclear:
				from xcodecleaner.__main__ import main

				with patch.object(sys, "argv", ["xcodecleaner", "--nuclear"]):
					result = main()

				mock_nuclear.assert_called_once_with(None)
				mock_gui.assert_not_called()
				assert result == 0

	def test_nuclear_with_password(self):
		"""--nuclear --password should pass password to cleanup."""
		with patch("xcodecleaner.__main__.gui_main"):
			with patch("xcodecleaner.__main__.cmd_nuclear", return_value=0) as mock_nuclear:
				from xcodecleaner.__main__ import main

				with patch.object(sys, "argv", ["xcodecleaner", "--nuclear", "--password", "secret"]):
					main()

				mock_nuclear.assert_called_once_with("secret")


class TestNuclearCommand:
	"""Test the nuclear cleanup command."""

	def test_nuclear_returns_zero_on_success(self):
		"""cmd_nuclear should return 0 on success."""
		with patch("xcodecleaner.__main__.cleanup") as mock_cleanup:
			mock_cleanup.nuclear_cleanup.return_value = type("Result", (), {"commands_ok": True})()
			from xcodecleaner.__main__ import cmd_nuclear

			assert cmd_nuclear(None) == 0

	def test_nuclear_returns_one_on_failure(self):
		"""cmd_nuclear should return 1 on failure."""
		with patch("xcodecleaner.__main__.cleanup") as mock_cleanup:
			mock_cleanup.nuclear_cleanup.return_value = type("Result", (), {"commands_ok": False})()
			from xcodecleaner.__main__ import cmd_nuclear

			assert cmd_nuclear(None) == 1
