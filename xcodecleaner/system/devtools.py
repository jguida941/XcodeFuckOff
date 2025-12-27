"""
Developer Tools availability checks.

This module validates that Xcode and simctl are properly configured before
attempting cleanup operations. Without simctl, the tool cannot permanently
delete runtimes - it can only temporarily unmount disk images.

Common issue: xcode-select points to /Library/Developer/CommandLineTools
instead of /Applications/Xcode.app/Contents/Developer. This causes
"xcrun: error: unable to find utility 'simctl'" errors.

Fix: sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
"""
import os
from typing import Mapping, Tuple, Optional

from xcodecleaner.core.runner import CommandRunner, get_default_runner

DEFAULT_XCODE_DEVELOPER_DIR = "/Applications/Xcode.app/Contents/Developer"


def get_xcode_select_path(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def is_simctl_available(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def is_xcode_path(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "Xcode.app" in path


def get_simctl_env(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def check_devtools(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def get_fix_command() -> str:
	"""Get the terminal command to fix xcode-select."""
	return "sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
