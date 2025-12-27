"""
Process management for Xcode simulator processes.

This module provides functions to:
- List running simulator processes
- Kill individual or all simulator processes
- Stop the CoreSimulator daemon to prevent respawn

All functions that execute commands accept an optional `runner` parameter
for dependency injection in tests.
"""
import os
from typing import Dict, List, Optional, Tuple

from xcodefuckoff.core.runner import CmdResult, CommandRunner, get_default_runner

# Keywords to identify simulator-related processes in ps output
SIMULATOR_KEYWORDS = ("Simulator", "CoreSimulator", "SimulatorTrampoline", "launchd_sim")


def _parse_ps_aux(output: str) -> List[Dict[str, str]]:
	"""
	Parse `ps aux` output to find simulator-related processes.

	This is a pure function for easy testing - no side effects.

	Args:
		output: Raw output from `ps aux` command.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
	"""
	processes: List[Dict[str, str]] = []
	for line in output.split("\n")[1:]:
		parts = line.split()
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def list_simulator_processes(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
	"""
	List all running simulator-related processes.

	Args:
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
		Returns empty list on error.
	"""
	try:
		runner = runner or get_default_runner()
		ps_result = runner.run(["ps", "aux"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def _run_commands_no_admin(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(result)
	return results


def kill_process(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def stop_coresimulator_daemon(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = ["launchctl", "bootout", f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(user_bootout)
	except Exception:
		result = CmdResult(tuple(user_bootout), 1, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def kill_all_simulators_and_xcode(
	password: Optional[str] = None,
	runner: CommandRunner | None = None,
) -> List[CmdResult]:
	"""
	Kill all simulator and Xcode processes.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn,
	then kills all related processes.

	If password is None (default), runs without admin (works for user-owned processes).
	The 'password' parameter is kept for backward compatibility but ignored -
	macOS will prompt via osascript if admin is needed.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# CRITICAL: Stop the launchd daemon FIRST so processes don't respawn
	daemon_results = stop_coresimulator_daemon(runner=runner)
	results.extend(daemon_results)

	# Now kill the processes - they won't come back
	commands = [
		["pkill", "-9", "-f", "Simulator"],
		["pkill", "-9", "-f", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def kill_all_simulators_and_xcode_admin(runner: CommandRunner | None = None) -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn.

	Returns (combined_command, return_code).
	"""
	runner = runner or get_default_runner()
	# Stop daemon first, then kill processes
	user_scope = f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = [
		f"launchctl bootout {user_scope}",
		"launchctl remove com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -f Simulator",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)
