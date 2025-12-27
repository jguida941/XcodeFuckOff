"""
Disk space measurement for accurate space reclaim reporting.

This module provides the "truth metric" for disk space:
- APFS container free space (CapacityNotAllocated) - the TRUE available space
- df output parsing as a fallback

The key insight: "Space Used" by mounted disk images != actual disk space used.
APFS containers share space, so you must measure the container's free capacity
before/after cleanup to know how much space was actually reclaimed.

All functions that execute commands accept an optional `runner` parameter
for dependency injection in tests.
"""
from __future__ import annotations

import plistlib
from typing import Dict, Optional

from xcodecleaner.core.runner import CommandRunner, get_default_runner


def parse_df_output(text: str) -> Optional[Dict[str, int]]:
	"""
	Parse `df -k` output to extract disk space metrics.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `df -k <path>` command.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	lines = [ln for ln in text.splitlines() if ln.strip()]
	if len(lines) < 2:
		return None
	parts = lines[-1].split()
	if len(parts) < 4:
		return None
	try:
		blocks_k = int(parts[1])
		used_k = int(parts[2])
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def df_bytes(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["df", "-k", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def _find_container_for_mount(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def parse_apfs_not_allocated(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
	"""
	Parse `diskutil apfs list -plist` output to extract container free space.

	This is the TRUE available space metric for APFS volumes. Use this
	before/after cleanup to calculate actual space reclaimed.

	This is a pure function for easy testing - no side effects.

	Args:
		plist_bytes: Raw plist output from `diskutil apfs list -plist`.
		mount_point: Mount point to find container for.

	Returns:
		CapacityNotAllocated in bytes, or None if not found.
	"""
	try:
		apfs_data = plistlib.loads(plist_bytes)
	except Exception:
		return None

	container = _find_container_for_mount(apfs_data, mount_point)
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def get_apfs_available_bytes(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
	"""
	Get actual available bytes from APFS container.

	This is the TRUE available space - use this to measure space reclaimed,
	not the sum of mounted disk image sizes.

	Args:
		runner: Optional CommandRunner for dependency injection in tests.
		mount_point: Mount point to find container for.

	Returns:
		Available bytes in the APFS container, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["diskutil", "apfs", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)
