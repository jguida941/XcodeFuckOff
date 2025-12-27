"""
Disk detection and management for Xcode simulator disk images.

This module provides functions to:
- Detect mounted simulator disk images via diskutil
- Parse disk information (name, mount point, size)
- Force unmount disk images

All functions that execute commands accept an optional `runner` parameter
for dependency injection in tests.
"""
import re
from typing import Callable, Dict, Iterable, List, Optional, Tuple

from xcodefuckoff.core.runner import CommandRunner, get_default_runner


# Keywords to identify simulator-related disk images in diskutil output
DEFAULT_KEYWORDS = ("Simulator", "Xcode", "iOS", "watchOS", "tvOS", "xrOS")


def parse_diskutil_list(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
	"""
	Parse `diskutil list` output to find simulator disk slices.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil list` command.
		keywords: Keywords to match (default: Simulator, iOS, etc.).

	Returns:
		List of disk slice identifiers (e.g., ["disk7s1", "disk11s1"]).
	"""
	lines = text.split("\n")
	disks: List[str] = []
	seen: set[str] = set()

	for line in lines:
		if not any(k in line for k in keywords):
			continue

		match = re.search(r"\b(disk\d+s\d+)\b", line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def _parse_size_bytes(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", 1)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def parse_diskutil_info(text: str) -> Dict[str, object]:
	"""
	Parse `diskutil info <device>` output to extract disk details.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil info /dev/diskXsY` command.

	Returns:
		Dict with keys: name, mount, size, size_bytes.
	"""
	volume_name = ""
	mount_point = ""
	size_str = ""
	size_bytes: Optional[int] = None

	for info_line in text.split("\n"):
		if "Volume Name:" in info_line:
			volume_name = info_line.split("Volume Name:")[1].strip()
		elif "Mount Point:" in info_line:
			mount_point = info_line.split("Mount Point:")[1].strip()
		elif "Disk Size:" in info_line:
			size_str, size_bytes = _parse_size_bytes(info_line)
		elif "Total Size:" in info_line and not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def list_simulator_disks(
	progress_callback: Optional[Callable[[int], None]] = None,
	runner: CommandRunner | None = None,
) -> List[Dict[str, object]]:
	"""
	List all mounted simulator disk images.

	Runs `diskutil list`, parses output to find simulator-related disks,
	then queries each disk for detailed info.

	Args:
		progress_callback: Optional callback(percent) for progress updates.
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		List of dicts with keys: device, name, mount, size, size_bytes.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["diskutil", "list"])
	lines = result.stdout.split("\n")
	disk_info: List[Dict[str, object]] = []

	devices = parse_diskutil_list(result.stdout)
	for i, device in enumerate(devices):
		if progress_callback:
			try:
				progress_callback(int((i / max(1, len(devices))) * 100))
			except Exception:
				pass

		device_path = f"/dev/{device}"
		info_result = runner.run(["diskutil", "info", device_path])
		parsed = parse_diskutil_info(info_result.stdout)

		if parsed.get("name") or parsed.get("mount"):
			disk_info.append(
				{
					"device": device_path,
					"name": parsed.get("name", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def _get_parent_disk(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def force_unmount_disk(
	device: str,
	timeout_seconds: int = 10,
	runner: CommandRunner | None = None,
) -> Tuple[bool, str]:
	"""
	Force unmount a disk image.
	Uses parent disk for more reliable unmounting.
	"""
	runner = runner or get_default_runner()
	parent = _get_parent_disk(device)
	timeout = max(1, int(timeout_seconds))

	try:
		# Try diskutil unmountDisk first (more reliable for disk images)
		result = runner.run(
			["diskutil", "unmountDisk", "force", parent],
			timeout=timeout,
		)
		if result.returncode == 0:
			return True, f"Unmounted {parent}"

		# Fallback to hdiutil detach on parent disk
		result = runner.run(
			["hdiutil", "detach", "-force", parent],
			timeout=timeout,
		)
		if result.returncode == 0:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def eject_disk(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(device, timeout_seconds=timeout_seconds)
