import glob
import os
import subprocess
from typing import Dict, List, Optional, Tuple


def delete_all_sim_devices() -> bool:
	try:
		subprocess.run(["xcrun", "simctl", "shutdown", "all"], check=False)
		subprocess.run(["xcrun", "simctl", "delete", "all"], check=False)
		return True
	except Exception:
		return False


def delete_unavailable_sim_devices() -> bool:
	"""
	Delete simulator devices that reference runtimes that are no longer installed.
	This is generally safe and usually does not require admin.
	"""
	try:
		subprocess.run(["xcrun", "simctl", "shutdown", "all"], check=False)
		subprocess.run(["xcrun", "simctl", "delete", "unavailable"], check=False)
		return True
	except Exception:
		return False


def remove_device_directories_and_profiles() -> bool:
	try:
		devices_path = os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")
		profiles_path = os.path.expanduser("~/Library/Developer/CoreSimulator/Profiles")
		subprocess.run(["rm", "-rf", devices_path], check=False)
		subprocess.run(["rm", "-rf", profiles_path], check=False)
		return True
	except Exception:
		return False


def disable_core_simulator_service() -> bool:
	try:
		subprocess.run(["sudo", "launchctl", "disable", "system/com.apple.CoreSimulator.CoreSimulatorService"], check=False)
		return True
	except Exception:
		return False


def clear_all_simulator_caches() -> List[Tuple[str, int]]:
	paths = [
		"~/Library/Developer/CoreSimulator/Caches",
		"~/Library/Developer/CoreSimulator/Temp",
		"~/Library/Caches/com.apple.CoreSimulator",
		"~/Library/Developer/Xcode/DerivedData",
	]
	results: List[Tuple[str, int]] = []
	for path in paths:
		try:
			expanded = os.path.expanduser(path)
			rc = subprocess.run(["rm", "-rf", expanded], check=False).returncode
		except Exception:
			rc = 1
		results.append((path, rc))
	return results


def df_bytes(path: str = "/System/Volumes/Data") -> Optional[Dict[str, int]]:
	"""
	Returns a dict with byte counts from `df -k`:
	- blocks_bytes, used_bytes, available_bytes
	"""
	try:
		result = subprocess.run(["df", "-k", path], capture_output=True, text=True, check=False)
		lines = [ln for ln in result.stdout.splitlines() if ln.strip()]
		if len(lines) < 2:
			return None
		# take the last line in case filesystem name wraps
		parts = lines[-1].split()
		# Expect: Filesystem 1024-blocks Used Available Capacity ...
		blocks_k = int(parts[1])
		used_k = int(parts[2])
		avail_k = int(parts[3])
		return {
			"blocks_bytes": blocks_k * 1024,
			"used_bytes": used_k * 1024,
			"available_bytes": avail_k * 1024,
		}
	except Exception:
		return None


def _run_osascript_admin(cmd: str, password: Optional[str]) -> int:
	"""
	Run a shell command with admin privileges via osascript.

	Important:
	- We avoid embedding cmd inside quotes directly (quote bugs / injection).
	- We pass cmd as argv into AppleScript.
	- If password is provided, it will be embedded; otherwise macOS will prompt.
	"""
	if password:
		# Keep backward compatibility, but escape quotes to avoid AppleScript parse issues.
		escaped_cmd = cmd.replace('"', '\\"')
		escaped_pwd = password.replace('"', '\\"')
		script = f'do shell script "{escaped_cmd}" with administrator privileges password "{escaped_pwd}"'
		return subprocess.run(["osascript", "-e", script], check=False).returncode

	script = (
		'on run argv\n'
		'  do shell script (item 1 of argv) with administrator privileges\n'
		'end run\n'
	)
	return subprocess.run(["osascript", "-e", script, cmd], check=False).returncode


def _unmount_simulator_volumes() -> List[Tuple[str, int]]:
	"""
	Unmount all simulator runtime volumes before attempting deletion.
	These are mounted disk images under /Library/Developer/CoreSimulator/Volumes/.
	"""
	results: List[Tuple[str, int]] = []
	vol_glob = "/Library/Developer/CoreSimulator/Volumes/iOS_*"
	volume_paths = sorted(glob.glob(vol_glob))

	for vol_path in volume_paths:
		# Use hdiutil to detach the volume
		cmd = f'hdiutil detach "{vol_path}" -force'
		try:
			rc = subprocess.run(
				["hdiutil", "detach", vol_path, "-force"],
				capture_output=True,
				check=False,
			).returncode
		except Exception:
			rc = 1
		results.append((cmd, rc))

	return results


def is_xcode_running() -> bool:
	"""Check if Xcode or Simulator is currently running."""
	try:
		result = subprocess.run(["pgrep", "-x", "Xcode"], capture_output=True)
		if result.returncode == 0:
			return True
		result = subprocess.run(["pgrep", "-x", "Simulator"], capture_output=True)
		return result.returncode == 0
	except Exception:
		return False


def _delete_runtimes_via_simctl() -> List[Tuple[str, int]]:
	"""
	Use Apple's official simctl command to delete simulator runtimes.
	This UNREGISTERS them from Xcode so they don't get re-mounted.
	"""
	results: List[Tuple[str, int]] = []

	# First, list available runtimes
	try:
		list_result = subprocess.run(
			["xcrun", "simctl", "runtime", "list"],
			capture_output=True,
			text=True,
			check=False,
		)
		results.append(("xcrun simctl runtime list", list_result.returncode))

		# Parse runtime identifiers from the output and delete each one
		# Format: "iOS 18.4 (18.4 - 22E5XXX) - XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
		if list_result.returncode == 0:
			for line in list_result.stdout.splitlines():
				# Look for UUID pattern at end of line
				parts = line.strip().split(" - ")
				if len(parts) >= 2:
					runtime_id = parts[-1].strip()
					# Check if it looks like a UUID
					if len(runtime_id) == 36 and runtime_id.count("-") == 4:
						try:
							del_result = subprocess.run(
								["xcrun", "simctl", "runtime", "delete", runtime_id],
								capture_output=True,
								text=True,
								check=False,
							)
							results.append((f"xcrun simctl runtime delete {runtime_id[:8]}...", del_result.returncode))
						except Exception:
							results.append((f"xcrun simctl runtime delete {runtime_id[:8]}...", 1))
	except Exception:
		results.append(("xcrun simctl runtime list", 1))

	# Also try the "delete all" command as a fallback
	try:
		delete_result = subprocess.run(
			["xcrun", "simctl", "runtime", "delete", "all"],
			capture_output=True,
			text=True,
			check=False,
		)
		results.append(("xcrun simctl runtime delete all", delete_result.returncode))
	except Exception:
		results.append(("xcrun simctl runtime delete all", 1))

	return results


def get_mounted_simulator_volumes() -> List[str]:
	"""
	Check for currently mounted simulator disk images.
	Returns list of mount points if any are found.
	"""
	try:
		result = subprocess.run(["hdiutil", "info"], capture_output=True, text=True, check=False)
		mounts = []
		for line in result.stdout.splitlines():
			if "Simulator" in line and "/Library/Developer/CoreSimulator/Volumes" in line:
				mounts.append(line.strip())
		return mounts
	except Exception:
		return []


def remove_runtime_backing_files(admin_password: Optional[str] = None) -> List[Tuple[str, int]]:
	"""
	Remove the big simulator runtime backing files that actually free disk space.

	Strategy:
	1. First try Apple's official `xcrun simctl runtime delete all` (works with SIP)
	2. Unmount any remaining volumes
	3. As fallback, try rm -rf with admin privileges (may fail due to SIP)

	Returns list of (command, return_code).
	"""
	results: List[Tuple[str, int]] = []

	# Step 1: Use Apple's official command (best approach, works with SIP)
	simctl_results = _delete_runtimes_via_simctl()
	results.extend(simctl_results)

	# Step 2: Unmount any remaining simulator volumes
	unmount_results = _unmount_simulator_volumes()
	results.extend(unmount_results)

	# Step 3: Fallback - try to rm -rf remaining paths (may fail due to SIP)
	vol_glob = "/Library/Developer/CoreSimulator/Volumes/iOS_*"
	volume_paths = sorted(glob.glob(vol_glob))
	targets = volume_paths + ["/Library/Developer/CoreSimulator/Cryptex"]

	# Only attempt rm if there are still paths remaining after simctl delete
	if targets and any(os.path.exists(t) for t in targets):
		for target in targets:
			if not os.path.exists(target):
				continue
			cmd = f'rm -rf "{target}"'
			rc = _run_osascript_admin(cmd, admin_password)
			results.append((cmd, rc))

	return results


def free_runtime_space(
	include_system_runtime_files: bool,
	admin_password: Optional[str] = None,
	include_user_space: bool = False,
	delete_devices: bool = False,
	delete_derived_data: bool = False,
	stop_processes: bool = True,
) -> Dict[str, object]:
	"""
	High-level cleanup intended to actually reclaim disk space.
	- simctl delete unavailable
	- optionally remove /Library CoreSimulator Volumes/Cryptex (admin)
	- optionally remove user-space Devices + DerivedData (no admin)
	- returns df before/after for the Data volume
	"""
	before = df_bytes("/System/Volumes/Data")

	steps: List[Tuple[str, int]] = []

	# Best-effort: stop Xcode/Simulator/CoreSimulator before touching system runtime files
	if stop_processes and include_system_runtime_files:
		try:
			# local import to avoid circular deps
			from xcodecleaner.services import processes as svc_processes

			for cmd, rc in svc_processes.kill_all_simulators_and_xcode(password=None):
				steps.append((cmd, rc))
		except Exception:
			steps.append(("pkill/killall simulators/xcode", 1))

	# Stop simulator state and delete unavailable devices first
	try:
		steps.append(("xcrun simctl shutdown all", subprocess.run(["xcrun", "simctl", "shutdown", "all"], check=False).returncode))
		steps.append(
			(
				"xcrun simctl delete unavailable",
				subprocess.run(["xcrun", "simctl", "delete", "unavailable"], check=False).returncode,
			)
		)
	except Exception:
		steps.append(("xcrun simctl ...", 1))

	if include_user_space:
		user_cmds: List[str] = []
		if delete_devices:
			user_cmds.append(f'rm -rf "{os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")}"')
		if delete_derived_data:
			user_cmds.append(f'rm -rf "{os.path.expanduser("~/Library/Developer/Xcode/DerivedData")}"')
		for cmd in user_cmds:
			steps.append((cmd, subprocess.run(cmd, shell=True, check=False).returncode))

	runtime_results: List[Tuple[str, int]] = []
	if include_system_runtime_files:
		runtime_results = remove_runtime_backing_files(admin_password=admin_password)
		steps.extend(runtime_results)

	after = df_bytes("/System/Volumes/Data")
	return {
		"before": before,
		"after": after,
		"steps": steps,
	}


