from typing import Optional

from xcodecleaner.core.runner import CommandRunner, get_default_runner


def is_sip_enabled(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None

