import subprocess
from typing import Optional


def is_sip_enabled() -> Optional[bool]:
	try:
		output = subprocess.check_output(["csrutil", "status"], text=True).strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


