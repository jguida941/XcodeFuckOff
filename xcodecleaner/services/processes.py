import subprocess
from typing import Dict, List, Optional, Tuple

SIMULATOR_KEYWORDS = ("Simulator", "CoreSimulator", "SimulatorTrampoline", "launchd_sim")


def list_simulator_processes() -> List[Dict[str, str]]:
	try:
		ps_result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
		processes: List[Dict[str, str]] = []
		for line in ps_result.stdout.split("\n")[1:]:
			parts = line.split()
			if len(parts) >= 11:
				process_name = " ".join(parts[10:])
				if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
					processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
		return processes
	except Exception:
		return []


def _run_commands_with_admin(commands: List[str]) -> int:
	"""
	Run multiple commands in a single osascript admin prompt.
	This avoids multiple password dialogs - user only sees one prompt.
	"""
	# Combine commands with semicolons, ignore individual failures
	combined = " ; ".join(commands)
	# Escape for AppleScript
	escaped = combined.replace("\\", "\\\\").replace('"', '\\"')
	script = f'do shell script "{escaped}" with administrator privileges'
	return subprocess.run(["osascript", "-e", script], check=False).returncode


def _run_commands_no_admin(commands: List[str]) -> List[Tuple[str, int]]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[Tuple[str, int]] = []
	for cmd in commands:
		try:
			rc = subprocess.run(cmd, shell=True, check=False).returncode
		except Exception:
			rc = 1
		results.append((cmd, rc))
	return results


def kill_process(pid: str, use_admin: bool = False) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	cmd = f"kill -9 {pid}"
	try:
		if use_admin:
			rc = _run_commands_with_admin([cmd])
		else:
			rc = subprocess.run(cmd, shell=True, check=False).returncode
		return rc == 0
	except Exception:
		return False


def kill_all_simulators_and_xcode(password: Optional[str] = None) -> List[Tuple[str, int]]:
	"""
	Kill all simulator and Xcode processes.

	If password is None (default), runs without admin (works for user-owned processes).
	The 'password' parameter is kept for backward compatibility but ignored -
	macOS will prompt via osascript if admin is needed.
	"""
	commands = [
		"pkill -9 -f Simulator",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	# Run without admin - pkill/killall work for user-owned processes
	return _run_commands_no_admin(commands)


def kill_all_simulators_and_xcode_admin() -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.
	Returns (combined_command, return_code).
	"""
	commands = [
		"pkill -9 -f Simulator",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = _run_commands_with_admin(commands)
	return (combined, rc)


