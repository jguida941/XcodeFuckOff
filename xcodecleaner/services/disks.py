import re
import subprocess
from typing import Callable, Dict, List, Optional, Tuple


def list_simulator_disks(progress_callback: Optional[Callable[[int], None]] = None) -> List[Dict[str, str]]:
	result = subprocess.run(["diskutil", "list"], capture_output=True, text=True)
	lines = result.stdout.split("\n")
	disk_info: List[Dict[str, str]] = []
	seen: set[str] = set()
	keywords = ("Simulator", "Xcode", "iOS", "watchOS", "tvOS")

	for i, line in enumerate(lines):
		if progress_callback:
			try:
				progress_callback(int((i / max(1, len(lines))) * 100))
			except Exception:
				pass

		# Prefer the actual filesystem slice (diskXsY) instead of /dev/diskX (often "Not applicable (no filesystem)")
		if not any(k in line for k in keywords):
			continue

		m = re.search(r"\b(disk\d+s\d+)\b", line)
		if not m:
			continue

		device = f"/dev/{m.group(1)}"
		if device in seen:
			continue
		seen.add(device)

		info_result = subprocess.run(["diskutil", "info", device], capture_output=True, text=True)
		volume_name = ""
		mount_point = ""
		size = ""
		for info_line in info_result.stdout.split("\n"):
			if "Volume Name:" in info_line:
				volume_name = info_line.split("Volume Name:")[1].strip()
			elif "Mount Point:" in info_line:
				mount_point = info_line.split("Mount Point:")[1].strip()
			elif "Disk Size:" in info_line:
				size = info_line.split("Disk Size:")[1].strip().split()[0]

		if mount_point.lower().startswith("not applicable"):
			mount_point = ""

		if volume_name or mount_point:
			disk_info.append(
				{
					"device": device,
					"name": volume_name or "Unknown",
					"mount": mount_point or "Not Mounted",
					"size": size or "Unknown",
				}
			)
	return disk_info


def force_unmount_disk(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	try:
		result = subprocess.run(
			["hdiutil", "detach", "-force", device],
			capture_output=True,
			text=True,
			timeout=max(1, int(timeout_seconds)),
		)
		if result.returncode == 0:
			return True, f"Detached {device}"
		return False, (result.stderr.strip() or result.stdout.strip() or f"Failed to detach {device}")
	except subprocess.TimeoutExpired:
		return False, f"Timeout detaching {device}"
	except Exception as exc:
		return False, f"Exception detaching {device}: {exc}"


def eject_disk(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	return force_unmount_disk(device, timeout_seconds=timeout_seconds)


