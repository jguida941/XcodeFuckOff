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

from xcodecleaner.core.runner import CmdResult, CommandRunner, get_default_runner

# Keywords to identify simulator-related processes in ps output
SIMULATOR_KEYWORDS = ("Simulator", "CoreSimulator", "SimulatorTrampoline", "launchd_sim")
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
	"""Forward call to original or mutated function, depending on the environment"""
	import os
	mutant_under_test = os.environ['MUTANT_UNDER_TEST']
	if mutant_under_test == 'fail':
		from mutmut.__main__ import MutmutProgrammaticFailException
		raise MutmutProgrammaticFailException('Failed programmatically')      
	elif mutant_under_test == 'stats':
		from mutmut.__main__ import record_trampoline_hit
		record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
		result = orig(*call_args, **call_kwargs)
		return result
	prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
	if not mutant_under_test.startswith(prefix):
		result = orig(*call_args, **call_kwargs)
		return result
	mutant_name = mutant_under_test.rpartition('.')[-1]
	if self_arg is not None:
		# call to a class method where self is not bound
		result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
	else:
		result = mutants[mutant_name](*call_args, **call_kwargs)
	return result


def x__parse_ps_aux__mutmut_orig(output: str) -> List[Dict[str, str]]:
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


def x__parse_ps_aux__mutmut_1(output: str) -> List[Dict[str, str]]:
	"""
	Parse `ps aux` output to find simulator-related processes.

	This is a pure function for easy testing - no side effects.

	Args:
		output: Raw output from `ps aux` command.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
	"""
	processes: List[Dict[str, str]] = None
	for line in output.split("\n")[1:]:
		parts = line.split()
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_2(output: str) -> List[Dict[str, str]]:
	"""
	Parse `ps aux` output to find simulator-related processes.

	This is a pure function for easy testing - no side effects.

	Args:
		output: Raw output from `ps aux` command.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
	"""
	processes: List[Dict[str, str]] = []
	for line in output.split(None)[1:]:
		parts = line.split()
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_3(output: str) -> List[Dict[str, str]]:
	"""
	Parse `ps aux` output to find simulator-related processes.

	This is a pure function for easy testing - no side effects.

	Args:
		output: Raw output from `ps aux` command.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
	"""
	processes: List[Dict[str, str]] = []
	for line in output.split("XX\nXX")[1:]:
		parts = line.split()
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_4(output: str) -> List[Dict[str, str]]:
	"""
	Parse `ps aux` output to find simulator-related processes.

	This is a pure function for easy testing - no side effects.

	Args:
		output: Raw output from `ps aux` command.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
	"""
	processes: List[Dict[str, str]] = []
	for line in output.split("\n")[2:]:
		parts = line.split()
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_5(output: str) -> List[Dict[str, str]]:
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
		parts = None
		if len(parts) >= 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_6(output: str) -> List[Dict[str, str]]:
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
		if len(parts) > 11:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_7(output: str) -> List[Dict[str, str]]:
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
		if len(parts) >= 12:
			process_name = " ".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_8(output: str) -> List[Dict[str, str]]:
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
			process_name = None
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_9(output: str) -> List[Dict[str, str]]:
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
			process_name = " ".join(None)
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_10(output: str) -> List[Dict[str, str]]:
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
			process_name = "XX XX".join(parts[10:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_11(output: str) -> List[Dict[str, str]]:
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
			process_name = " ".join(parts[11:])
			if any(keyword in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_12(output: str) -> List[Dict[str, str]]:
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
			if any(None):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_13(output: str) -> List[Dict[str, str]]:
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
			if any(keyword not in process_name for keyword in SIMULATOR_KEYWORDS):
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_14(output: str) -> List[Dict[str, str]]:
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
				processes.append(None)
	return processes


def x__parse_ps_aux__mutmut_15(output: str) -> List[Dict[str, str]]:
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
				processes.append({"XXpidXX": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_16(output: str) -> List[Dict[str, str]]:
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
				processes.append({"PID": parts[1], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_17(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[2], "cpu": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_18(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "XXcpuXX": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_19(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "CPU": parts[2], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_20(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[3], "mem": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_21(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[2], "XXmemXX": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_22(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[2], "MEM": parts[3], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_23(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[4], "name": process_name})
	return processes


def x__parse_ps_aux__mutmut_24(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "XXnameXX": process_name})
	return processes


def x__parse_ps_aux__mutmut_25(output: str) -> List[Dict[str, str]]:
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
				processes.append({"pid": parts[1], "cpu": parts[2], "mem": parts[3], "NAME": process_name})
	return processes

x__parse_ps_aux__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse_ps_aux__mutmut_1': x__parse_ps_aux__mutmut_1, 
    'x__parse_ps_aux__mutmut_2': x__parse_ps_aux__mutmut_2, 
    'x__parse_ps_aux__mutmut_3': x__parse_ps_aux__mutmut_3, 
    'x__parse_ps_aux__mutmut_4': x__parse_ps_aux__mutmut_4, 
    'x__parse_ps_aux__mutmut_5': x__parse_ps_aux__mutmut_5, 
    'x__parse_ps_aux__mutmut_6': x__parse_ps_aux__mutmut_6, 
    'x__parse_ps_aux__mutmut_7': x__parse_ps_aux__mutmut_7, 
    'x__parse_ps_aux__mutmut_8': x__parse_ps_aux__mutmut_8, 
    'x__parse_ps_aux__mutmut_9': x__parse_ps_aux__mutmut_9, 
    'x__parse_ps_aux__mutmut_10': x__parse_ps_aux__mutmut_10, 
    'x__parse_ps_aux__mutmut_11': x__parse_ps_aux__mutmut_11, 
    'x__parse_ps_aux__mutmut_12': x__parse_ps_aux__mutmut_12, 
    'x__parse_ps_aux__mutmut_13': x__parse_ps_aux__mutmut_13, 
    'x__parse_ps_aux__mutmut_14': x__parse_ps_aux__mutmut_14, 
    'x__parse_ps_aux__mutmut_15': x__parse_ps_aux__mutmut_15, 
    'x__parse_ps_aux__mutmut_16': x__parse_ps_aux__mutmut_16, 
    'x__parse_ps_aux__mutmut_17': x__parse_ps_aux__mutmut_17, 
    'x__parse_ps_aux__mutmut_18': x__parse_ps_aux__mutmut_18, 
    'x__parse_ps_aux__mutmut_19': x__parse_ps_aux__mutmut_19, 
    'x__parse_ps_aux__mutmut_20': x__parse_ps_aux__mutmut_20, 
    'x__parse_ps_aux__mutmut_21': x__parse_ps_aux__mutmut_21, 
    'x__parse_ps_aux__mutmut_22': x__parse_ps_aux__mutmut_22, 
    'x__parse_ps_aux__mutmut_23': x__parse_ps_aux__mutmut_23, 
    'x__parse_ps_aux__mutmut_24': x__parse_ps_aux__mutmut_24, 
    'x__parse_ps_aux__mutmut_25': x__parse_ps_aux__mutmut_25
}

def _parse_ps_aux(*args, **kwargs):
	result = _mutmut_trampoline(x__parse_ps_aux__mutmut_orig, x__parse_ps_aux__mutmut_mutants, args, kwargs)
	return result 

_parse_ps_aux.__signature__ = _mutmut_signature(x__parse_ps_aux__mutmut_orig)
x__parse_ps_aux__mutmut_orig.__name__ = 'x__parse_ps_aux'


def x_list_simulator_processes__mutmut_orig(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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


def x_list_simulator_processes__mutmut_1(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
	"""
	List all running simulator-related processes.

	Args:
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
		Returns empty list on error.
	"""
	try:
		runner = None
		ps_result = runner.run(["ps", "aux"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_2(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
	"""
	List all running simulator-related processes.

	Args:
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		List of dicts with keys: pid, cpu, mem, name.
		Returns empty list on error.
	"""
	try:
		runner = runner and get_default_runner()
		ps_result = runner.run(["ps", "aux"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_3(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = None
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_4(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = runner.run(None)
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_5(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = runner.run(["XXpsXX", "aux"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_6(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = runner.run(["PS", "aux"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_7(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = runner.run(["ps", "XXauxXX"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_8(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		ps_result = runner.run(["ps", "AUX"])
		return _parse_ps_aux(ps_result.stdout)
	except Exception:
		return []


def x_list_simulator_processes__mutmut_9(runner: CommandRunner | None = None) -> List[Dict[str, str]]:
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
		return _parse_ps_aux(None)
	except Exception:
		return []

x_list_simulator_processes__mutmut_mutants : ClassVar[MutantDict] = {
'x_list_simulator_processes__mutmut_1': x_list_simulator_processes__mutmut_1, 
    'x_list_simulator_processes__mutmut_2': x_list_simulator_processes__mutmut_2, 
    'x_list_simulator_processes__mutmut_3': x_list_simulator_processes__mutmut_3, 
    'x_list_simulator_processes__mutmut_4': x_list_simulator_processes__mutmut_4, 
    'x_list_simulator_processes__mutmut_5': x_list_simulator_processes__mutmut_5, 
    'x_list_simulator_processes__mutmut_6': x_list_simulator_processes__mutmut_6, 
    'x_list_simulator_processes__mutmut_7': x_list_simulator_processes__mutmut_7, 
    'x_list_simulator_processes__mutmut_8': x_list_simulator_processes__mutmut_8, 
    'x_list_simulator_processes__mutmut_9': x_list_simulator_processes__mutmut_9
}

def list_simulator_processes(*args, **kwargs):
	result = _mutmut_trampoline(x_list_simulator_processes__mutmut_orig, x_list_simulator_processes__mutmut_mutants, args, kwargs)
	return result 

list_simulator_processes.__signature__ = _mutmut_signature(x_list_simulator_processes__mutmut_orig)
x_list_simulator_processes__mutmut_orig.__name__ = 'x_list_simulator_processes'


def x__run_commands_no_admin__mutmut_orig(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_1(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = None
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_2(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = None
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_3(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(None)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_4(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = None
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_5(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(None, 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_6(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), None, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_7(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, None, "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_8(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", None)
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_9(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_10(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_11(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_12(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", )
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_13(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(None), 1, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_14(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 2, "", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_15(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "XXXX", "exception while executing command")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_16(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "XXexception while executing commandXX")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_17(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "EXCEPTION WHILE EXECUTING COMMAND")
		results.append(result)
	return results


def x__run_commands_no_admin__mutmut_18(commands: List[List[str]], runner: CommandRunner) -> List[CmdResult]:
	"""Run commands without admin privileges, returning individual results."""
	results: List[CmdResult] = []
	for cmd in commands:
		try:
			result = runner.run(cmd)
		except Exception:
			result = CmdResult(tuple(cmd), 1, "", "exception while executing command")
		results.append(None)
	return results

x__run_commands_no_admin__mutmut_mutants : ClassVar[MutantDict] = {
'x__run_commands_no_admin__mutmut_1': x__run_commands_no_admin__mutmut_1, 
    'x__run_commands_no_admin__mutmut_2': x__run_commands_no_admin__mutmut_2, 
    'x__run_commands_no_admin__mutmut_3': x__run_commands_no_admin__mutmut_3, 
    'x__run_commands_no_admin__mutmut_4': x__run_commands_no_admin__mutmut_4, 
    'x__run_commands_no_admin__mutmut_5': x__run_commands_no_admin__mutmut_5, 
    'x__run_commands_no_admin__mutmut_6': x__run_commands_no_admin__mutmut_6, 
    'x__run_commands_no_admin__mutmut_7': x__run_commands_no_admin__mutmut_7, 
    'x__run_commands_no_admin__mutmut_8': x__run_commands_no_admin__mutmut_8, 
    'x__run_commands_no_admin__mutmut_9': x__run_commands_no_admin__mutmut_9, 
    'x__run_commands_no_admin__mutmut_10': x__run_commands_no_admin__mutmut_10, 
    'x__run_commands_no_admin__mutmut_11': x__run_commands_no_admin__mutmut_11, 
    'x__run_commands_no_admin__mutmut_12': x__run_commands_no_admin__mutmut_12, 
    'x__run_commands_no_admin__mutmut_13': x__run_commands_no_admin__mutmut_13, 
    'x__run_commands_no_admin__mutmut_14': x__run_commands_no_admin__mutmut_14, 
    'x__run_commands_no_admin__mutmut_15': x__run_commands_no_admin__mutmut_15, 
    'x__run_commands_no_admin__mutmut_16': x__run_commands_no_admin__mutmut_16, 
    'x__run_commands_no_admin__mutmut_17': x__run_commands_no_admin__mutmut_17, 
    'x__run_commands_no_admin__mutmut_18': x__run_commands_no_admin__mutmut_18
}

def _run_commands_no_admin(*args, **kwargs):
	result = _mutmut_trampoline(x__run_commands_no_admin__mutmut_orig, x__run_commands_no_admin__mutmut_mutants, args, kwargs)
	return result 

_run_commands_no_admin.__signature__ = _mutmut_signature(x__run_commands_no_admin__mutmut_orig)
x__run_commands_no_admin__mutmut_orig.__name__ = 'x__run_commands_no_admin'


def x_kill_process__mutmut_orig(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_1(pid: str, use_admin: bool = True, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_2(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = None
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_3(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner and get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_4(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = None
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_5(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["XXkillXX", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_6(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["KILL", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_7(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "XX-9XX", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_8(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = None
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_9(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(None, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_10(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=None)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_11(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_12(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, )
		return result.returncode == 0
	except Exception:
		return False


def x_kill_process__mutmut_13(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode != 0
	except Exception:
		return False


def x_kill_process__mutmut_14(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 1
	except Exception:
		return False


def x_kill_process__mutmut_15(pid: str, use_admin: bool = False, runner: CommandRunner | None = None) -> bool:
	"""Kill a process by PID. If use_admin=True, prompts for admin once."""
	runner = runner or get_default_runner()
	cmd = ["kill", "-9", pid]
	try:
		result = runner.run(cmd, sudo=use_admin)
		return result.returncode == 0
	except Exception:
		return True

x_kill_process__mutmut_mutants : ClassVar[MutantDict] = {
'x_kill_process__mutmut_1': x_kill_process__mutmut_1, 
    'x_kill_process__mutmut_2': x_kill_process__mutmut_2, 
    'x_kill_process__mutmut_3': x_kill_process__mutmut_3, 
    'x_kill_process__mutmut_4': x_kill_process__mutmut_4, 
    'x_kill_process__mutmut_5': x_kill_process__mutmut_5, 
    'x_kill_process__mutmut_6': x_kill_process__mutmut_6, 
    'x_kill_process__mutmut_7': x_kill_process__mutmut_7, 
    'x_kill_process__mutmut_8': x_kill_process__mutmut_8, 
    'x_kill_process__mutmut_9': x_kill_process__mutmut_9, 
    'x_kill_process__mutmut_10': x_kill_process__mutmut_10, 
    'x_kill_process__mutmut_11': x_kill_process__mutmut_11, 
    'x_kill_process__mutmut_12': x_kill_process__mutmut_12, 
    'x_kill_process__mutmut_13': x_kill_process__mutmut_13, 
    'x_kill_process__mutmut_14': x_kill_process__mutmut_14, 
    'x_kill_process__mutmut_15': x_kill_process__mutmut_15
}

def kill_process(*args, **kwargs):
	result = _mutmut_trampoline(x_kill_process__mutmut_orig, x_kill_process__mutmut_mutants, args, kwargs)
	return result 

kill_process.__signature__ = _mutmut_signature(x_kill_process__mutmut_orig)
x_kill_process__mutmut_orig.__name__ = 'x_kill_process'


def x_stop_coresimulator_daemon__mutmut_orig(runner: CommandRunner | None = None) -> List[CmdResult]:
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


def x_stop_coresimulator_daemon__mutmut_1(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = None
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


def x_stop_coresimulator_daemon__mutmut_2(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner and get_default_runner()
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


def x_stop_coresimulator_daemon__mutmut_3(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = None

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


def x_stop_coresimulator_daemon__mutmut_4(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = None
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


def x_stop_coresimulator_daemon__mutmut_5(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = ["XXlaunchctlXX", "bootout", f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"]
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


def x_stop_coresimulator_daemon__mutmut_6(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = ["LAUNCHCTL", "bootout", f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"]
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


def x_stop_coresimulator_daemon__mutmut_7(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = ["launchctl", "XXbootoutXX", f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"]
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


def x_stop_coresimulator_daemon__mutmut_8(runner: CommandRunner | None = None) -> List[CmdResult]:
	"""
	Stop the CoreSimulator launchd daemon so it doesn't respawn processes.
	This is CRITICAL - without this, killed processes come back immediately.

	Uses launchctl bootout to unload the daemon from launchd.
	"""
	runner = runner or get_default_runner()
	results: List[CmdResult] = []

	# First try to bootout the user-level service (runs as current user)
	user_bootout = ["launchctl", "BOOTOUT", f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"]
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


def x_stop_coresimulator_daemon__mutmut_9(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = None
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


def x_stop_coresimulator_daemon__mutmut_10(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = runner.run(None)
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


def x_stop_coresimulator_daemon__mutmut_11(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = None
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_12(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(None, 1, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_13(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), None, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_14(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, None, "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_15(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "", None)
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_16(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(1, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_17(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_18(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_19(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "", )
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_20(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(None), 1, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_21(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 2, "", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_22(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "XXXX", "exception while executing command")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_23(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "", "XXexception while executing commandXX")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_24(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(user_bootout), 1, "", "EXCEPTION WHILE EXECUTING COMMAND")
	results.append(result)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_25(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	results.append(None)

	# Also try to remove any running service instances
	remove_cmd = ["launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_26(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = None
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_27(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["XXlaunchctlXX", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_28(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["LAUNCHCTL", "remove", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_29(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["launchctl", "XXremoveXX", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_30(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["launchctl", "REMOVE", "com.apple.CoreSimulator.CoreSimulatorService"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_31(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["launchctl", "remove", "XXcom.apple.CoreSimulator.CoreSimulatorServiceXX"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_32(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["launchctl", "remove", "com.apple.coresimulator.coresimulatorservice"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_33(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	remove_cmd = ["launchctl", "remove", "COM.APPLE.CORESIMULATOR.CORESIMULATORSERVICE"]
	try:
		result = runner.run(remove_cmd)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_34(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = None
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_35(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = runner.run(None)
	except Exception:
		result = CmdResult(tuple(remove_cmd), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_36(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = None
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_37(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(None, 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_38(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), None, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_39(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, None, "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_40(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "", None)
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_41(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_42(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_43(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_44(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "", )
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_45(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(None), 1, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_46(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 2, "", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_47(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "XXXX", "exception while executing command")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_48(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "", "XXexception while executing commandXX")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_49(runner: CommandRunner | None = None) -> List[CmdResult]:
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
		result = CmdResult(tuple(remove_cmd), 1, "", "EXCEPTION WHILE EXECUTING COMMAND")
	results.append(result)

	return results


def x_stop_coresimulator_daemon__mutmut_50(runner: CommandRunner | None = None) -> List[CmdResult]:
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
	results.append(None)

	return results

x_stop_coresimulator_daemon__mutmut_mutants : ClassVar[MutantDict] = {
'x_stop_coresimulator_daemon__mutmut_1': x_stop_coresimulator_daemon__mutmut_1, 
    'x_stop_coresimulator_daemon__mutmut_2': x_stop_coresimulator_daemon__mutmut_2, 
    'x_stop_coresimulator_daemon__mutmut_3': x_stop_coresimulator_daemon__mutmut_3, 
    'x_stop_coresimulator_daemon__mutmut_4': x_stop_coresimulator_daemon__mutmut_4, 
    'x_stop_coresimulator_daemon__mutmut_5': x_stop_coresimulator_daemon__mutmut_5, 
    'x_stop_coresimulator_daemon__mutmut_6': x_stop_coresimulator_daemon__mutmut_6, 
    'x_stop_coresimulator_daemon__mutmut_7': x_stop_coresimulator_daemon__mutmut_7, 
    'x_stop_coresimulator_daemon__mutmut_8': x_stop_coresimulator_daemon__mutmut_8, 
    'x_stop_coresimulator_daemon__mutmut_9': x_stop_coresimulator_daemon__mutmut_9, 
    'x_stop_coresimulator_daemon__mutmut_10': x_stop_coresimulator_daemon__mutmut_10, 
    'x_stop_coresimulator_daemon__mutmut_11': x_stop_coresimulator_daemon__mutmut_11, 
    'x_stop_coresimulator_daemon__mutmut_12': x_stop_coresimulator_daemon__mutmut_12, 
    'x_stop_coresimulator_daemon__mutmut_13': x_stop_coresimulator_daemon__mutmut_13, 
    'x_stop_coresimulator_daemon__mutmut_14': x_stop_coresimulator_daemon__mutmut_14, 
    'x_stop_coresimulator_daemon__mutmut_15': x_stop_coresimulator_daemon__mutmut_15, 
    'x_stop_coresimulator_daemon__mutmut_16': x_stop_coresimulator_daemon__mutmut_16, 
    'x_stop_coresimulator_daemon__mutmut_17': x_stop_coresimulator_daemon__mutmut_17, 
    'x_stop_coresimulator_daemon__mutmut_18': x_stop_coresimulator_daemon__mutmut_18, 
    'x_stop_coresimulator_daemon__mutmut_19': x_stop_coresimulator_daemon__mutmut_19, 
    'x_stop_coresimulator_daemon__mutmut_20': x_stop_coresimulator_daemon__mutmut_20, 
    'x_stop_coresimulator_daemon__mutmut_21': x_stop_coresimulator_daemon__mutmut_21, 
    'x_stop_coresimulator_daemon__mutmut_22': x_stop_coresimulator_daemon__mutmut_22, 
    'x_stop_coresimulator_daemon__mutmut_23': x_stop_coresimulator_daemon__mutmut_23, 
    'x_stop_coresimulator_daemon__mutmut_24': x_stop_coresimulator_daemon__mutmut_24, 
    'x_stop_coresimulator_daemon__mutmut_25': x_stop_coresimulator_daemon__mutmut_25, 
    'x_stop_coresimulator_daemon__mutmut_26': x_stop_coresimulator_daemon__mutmut_26, 
    'x_stop_coresimulator_daemon__mutmut_27': x_stop_coresimulator_daemon__mutmut_27, 
    'x_stop_coresimulator_daemon__mutmut_28': x_stop_coresimulator_daemon__mutmut_28, 
    'x_stop_coresimulator_daemon__mutmut_29': x_stop_coresimulator_daemon__mutmut_29, 
    'x_stop_coresimulator_daemon__mutmut_30': x_stop_coresimulator_daemon__mutmut_30, 
    'x_stop_coresimulator_daemon__mutmut_31': x_stop_coresimulator_daemon__mutmut_31, 
    'x_stop_coresimulator_daemon__mutmut_32': x_stop_coresimulator_daemon__mutmut_32, 
    'x_stop_coresimulator_daemon__mutmut_33': x_stop_coresimulator_daemon__mutmut_33, 
    'x_stop_coresimulator_daemon__mutmut_34': x_stop_coresimulator_daemon__mutmut_34, 
    'x_stop_coresimulator_daemon__mutmut_35': x_stop_coresimulator_daemon__mutmut_35, 
    'x_stop_coresimulator_daemon__mutmut_36': x_stop_coresimulator_daemon__mutmut_36, 
    'x_stop_coresimulator_daemon__mutmut_37': x_stop_coresimulator_daemon__mutmut_37, 
    'x_stop_coresimulator_daemon__mutmut_38': x_stop_coresimulator_daemon__mutmut_38, 
    'x_stop_coresimulator_daemon__mutmut_39': x_stop_coresimulator_daemon__mutmut_39, 
    'x_stop_coresimulator_daemon__mutmut_40': x_stop_coresimulator_daemon__mutmut_40, 
    'x_stop_coresimulator_daemon__mutmut_41': x_stop_coresimulator_daemon__mutmut_41, 
    'x_stop_coresimulator_daemon__mutmut_42': x_stop_coresimulator_daemon__mutmut_42, 
    'x_stop_coresimulator_daemon__mutmut_43': x_stop_coresimulator_daemon__mutmut_43, 
    'x_stop_coresimulator_daemon__mutmut_44': x_stop_coresimulator_daemon__mutmut_44, 
    'x_stop_coresimulator_daemon__mutmut_45': x_stop_coresimulator_daemon__mutmut_45, 
    'x_stop_coresimulator_daemon__mutmut_46': x_stop_coresimulator_daemon__mutmut_46, 
    'x_stop_coresimulator_daemon__mutmut_47': x_stop_coresimulator_daemon__mutmut_47, 
    'x_stop_coresimulator_daemon__mutmut_48': x_stop_coresimulator_daemon__mutmut_48, 
    'x_stop_coresimulator_daemon__mutmut_49': x_stop_coresimulator_daemon__mutmut_49, 
    'x_stop_coresimulator_daemon__mutmut_50': x_stop_coresimulator_daemon__mutmut_50
}

def stop_coresimulator_daemon(*args, **kwargs):
	result = _mutmut_trampoline(x_stop_coresimulator_daemon__mutmut_orig, x_stop_coresimulator_daemon__mutmut_mutants, args, kwargs)
	return result 

stop_coresimulator_daemon.__signature__ = _mutmut_signature(x_stop_coresimulator_daemon__mutmut_orig)
x_stop_coresimulator_daemon__mutmut_orig.__name__ = 'x_stop_coresimulator_daemon'


def x_kill_all_simulators_and_xcode__mutmut_orig(
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


def x_kill_all_simulators_and_xcode__mutmut_1(
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
	runner = None
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


def x_kill_all_simulators_and_xcode__mutmut_2(
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
	runner = runner and get_default_runner()
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


def x_kill_all_simulators_and_xcode__mutmut_3(
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
	results: List[CmdResult] = None

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


def x_kill_all_simulators_and_xcode__mutmut_4(
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
	daemon_results = None
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


def x_kill_all_simulators_and_xcode__mutmut_5(
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
	daemon_results = stop_coresimulator_daemon(runner=None)
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


def x_kill_all_simulators_and_xcode__mutmut_6(
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
	results.extend(None)

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


def x_kill_all_simulators_and_xcode__mutmut_7(
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
	commands = None
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_8(
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
		["XXpkillXX", "-9", "-f", "Simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_9(
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
		["PKILL", "-9", "-f", "Simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_10(
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
		["pkill", "XX-9XX", "-f", "Simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_11(
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
		["pkill", "-9", "XX-fXX", "Simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_12(
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
		["pkill", "-9", "-F", "Simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_13(
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
		["pkill", "-9", "-f", "XXSimulatorXX"],
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


def x_kill_all_simulators_and_xcode__mutmut_14(
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
		["pkill", "-9", "-f", "simulator"],
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


def x_kill_all_simulators_and_xcode__mutmut_15(
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
		["pkill", "-9", "-f", "SIMULATOR"],
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


def x_kill_all_simulators_and_xcode__mutmut_16(
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
		["XXpkillXX", "-9", "-f", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_17(
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
		["PKILL", "-9", "-f", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_18(
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
		["pkill", "XX-9XX", "-f", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_19(
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
		["pkill", "-9", "XX-fXX", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_20(
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
		["pkill", "-9", "-F", "CoreSimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_21(
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
		["pkill", "-9", "-f", "XXCoreSimulatorXX"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_22(
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
		["pkill", "-9", "-f", "coresimulator"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_23(
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
		["pkill", "-9", "-f", "CORESIMULATOR"],
		["pkill", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_24(
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
		["XXpkillXX", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_25(
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
		["PKILL", "-9", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_26(
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
		["pkill", "XX-9XX", "-f", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_27(
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
		["pkill", "-9", "XX-fXX", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_28(
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
		["pkill", "-9", "-F", "SimulatorTrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_29(
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
		["pkill", "-9", "-f", "XXSimulatorTrampolineXX"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_30(
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
		["pkill", "-9", "-f", "simulatortrampoline"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_31(
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
		["pkill", "-9", "-f", "SIMULATORTRAMPOLINE"],
		["pkill", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_32(
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
		["XXpkillXX", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_33(
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
		["PKILL", "-9", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_34(
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
		["pkill", "XX-9XX", "-f", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_35(
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
		["pkill", "-9", "XX-fXX", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_36(
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
		["pkill", "-9", "-F", "launchd_sim"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_37(
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
		["pkill", "-9", "-f", "XXlaunchd_simXX"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_38(
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
		["pkill", "-9", "-f", "LAUNCHD_SIM"],
		["killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_39(
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
		["XXkillallXX", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_40(
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
		["KILLALL", "-9", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_41(
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
		["killall", "XX-9XX", "com.apple.CoreSimulator.CoreSimulatorService"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_42(
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
		["killall", "-9", "XXcom.apple.CoreSimulator.CoreSimulatorServiceXX"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_43(
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
		["killall", "-9", "com.apple.coresimulator.coresimulatorservice"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_44(
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
		["killall", "-9", "COM.APPLE.CORESIMULATOR.CORESIMULATORSERVICE"],
		["pkill", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_45(
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
		["XXpkillXX", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_46(
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
		["PKILL", "-9", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_47(
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
		["pkill", "XX-9XX", "-x", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_48(
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
		["pkill", "-9", "XX-xXX", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_49(
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
		["pkill", "-9", "-X", "Xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_50(
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
		["pkill", "-9", "-x", "XXXcodeXX"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_51(
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
		["pkill", "-9", "-x", "xcode"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_52(
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
		["pkill", "-9", "-x", "XCODE"],
	]
	# Run without admin - pkill/killall work for user-owned processes
	kill_results = _run_commands_no_admin(commands, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_53(
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
	kill_results = None
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_54(
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
	kill_results = _run_commands_no_admin(None, runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_55(
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
	kill_results = _run_commands_no_admin(commands, runner=None)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_56(
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
	kill_results = _run_commands_no_admin(runner=runner)
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_57(
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
	kill_results = _run_commands_no_admin(commands, )
	results.extend(kill_results)

	return results


def x_kill_all_simulators_and_xcode__mutmut_58(
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
	results.extend(None)

	return results

x_kill_all_simulators_and_xcode__mutmut_mutants : ClassVar[MutantDict] = {
'x_kill_all_simulators_and_xcode__mutmut_1': x_kill_all_simulators_and_xcode__mutmut_1, 
    'x_kill_all_simulators_and_xcode__mutmut_2': x_kill_all_simulators_and_xcode__mutmut_2, 
    'x_kill_all_simulators_and_xcode__mutmut_3': x_kill_all_simulators_and_xcode__mutmut_3, 
    'x_kill_all_simulators_and_xcode__mutmut_4': x_kill_all_simulators_and_xcode__mutmut_4, 
    'x_kill_all_simulators_and_xcode__mutmut_5': x_kill_all_simulators_and_xcode__mutmut_5, 
    'x_kill_all_simulators_and_xcode__mutmut_6': x_kill_all_simulators_and_xcode__mutmut_6, 
    'x_kill_all_simulators_and_xcode__mutmut_7': x_kill_all_simulators_and_xcode__mutmut_7, 
    'x_kill_all_simulators_and_xcode__mutmut_8': x_kill_all_simulators_and_xcode__mutmut_8, 
    'x_kill_all_simulators_and_xcode__mutmut_9': x_kill_all_simulators_and_xcode__mutmut_9, 
    'x_kill_all_simulators_and_xcode__mutmut_10': x_kill_all_simulators_and_xcode__mutmut_10, 
    'x_kill_all_simulators_and_xcode__mutmut_11': x_kill_all_simulators_and_xcode__mutmut_11, 
    'x_kill_all_simulators_and_xcode__mutmut_12': x_kill_all_simulators_and_xcode__mutmut_12, 
    'x_kill_all_simulators_and_xcode__mutmut_13': x_kill_all_simulators_and_xcode__mutmut_13, 
    'x_kill_all_simulators_and_xcode__mutmut_14': x_kill_all_simulators_and_xcode__mutmut_14, 
    'x_kill_all_simulators_and_xcode__mutmut_15': x_kill_all_simulators_and_xcode__mutmut_15, 
    'x_kill_all_simulators_and_xcode__mutmut_16': x_kill_all_simulators_and_xcode__mutmut_16, 
    'x_kill_all_simulators_and_xcode__mutmut_17': x_kill_all_simulators_and_xcode__mutmut_17, 
    'x_kill_all_simulators_and_xcode__mutmut_18': x_kill_all_simulators_and_xcode__mutmut_18, 
    'x_kill_all_simulators_and_xcode__mutmut_19': x_kill_all_simulators_and_xcode__mutmut_19, 
    'x_kill_all_simulators_and_xcode__mutmut_20': x_kill_all_simulators_and_xcode__mutmut_20, 
    'x_kill_all_simulators_and_xcode__mutmut_21': x_kill_all_simulators_and_xcode__mutmut_21, 
    'x_kill_all_simulators_and_xcode__mutmut_22': x_kill_all_simulators_and_xcode__mutmut_22, 
    'x_kill_all_simulators_and_xcode__mutmut_23': x_kill_all_simulators_and_xcode__mutmut_23, 
    'x_kill_all_simulators_and_xcode__mutmut_24': x_kill_all_simulators_and_xcode__mutmut_24, 
    'x_kill_all_simulators_and_xcode__mutmut_25': x_kill_all_simulators_and_xcode__mutmut_25, 
    'x_kill_all_simulators_and_xcode__mutmut_26': x_kill_all_simulators_and_xcode__mutmut_26, 
    'x_kill_all_simulators_and_xcode__mutmut_27': x_kill_all_simulators_and_xcode__mutmut_27, 
    'x_kill_all_simulators_and_xcode__mutmut_28': x_kill_all_simulators_and_xcode__mutmut_28, 
    'x_kill_all_simulators_and_xcode__mutmut_29': x_kill_all_simulators_and_xcode__mutmut_29, 
    'x_kill_all_simulators_and_xcode__mutmut_30': x_kill_all_simulators_and_xcode__mutmut_30, 
    'x_kill_all_simulators_and_xcode__mutmut_31': x_kill_all_simulators_and_xcode__mutmut_31, 
    'x_kill_all_simulators_and_xcode__mutmut_32': x_kill_all_simulators_and_xcode__mutmut_32, 
    'x_kill_all_simulators_and_xcode__mutmut_33': x_kill_all_simulators_and_xcode__mutmut_33, 
    'x_kill_all_simulators_and_xcode__mutmut_34': x_kill_all_simulators_and_xcode__mutmut_34, 
    'x_kill_all_simulators_and_xcode__mutmut_35': x_kill_all_simulators_and_xcode__mutmut_35, 
    'x_kill_all_simulators_and_xcode__mutmut_36': x_kill_all_simulators_and_xcode__mutmut_36, 
    'x_kill_all_simulators_and_xcode__mutmut_37': x_kill_all_simulators_and_xcode__mutmut_37, 
    'x_kill_all_simulators_and_xcode__mutmut_38': x_kill_all_simulators_and_xcode__mutmut_38, 
    'x_kill_all_simulators_and_xcode__mutmut_39': x_kill_all_simulators_and_xcode__mutmut_39, 
    'x_kill_all_simulators_and_xcode__mutmut_40': x_kill_all_simulators_and_xcode__mutmut_40, 
    'x_kill_all_simulators_and_xcode__mutmut_41': x_kill_all_simulators_and_xcode__mutmut_41, 
    'x_kill_all_simulators_and_xcode__mutmut_42': x_kill_all_simulators_and_xcode__mutmut_42, 
    'x_kill_all_simulators_and_xcode__mutmut_43': x_kill_all_simulators_and_xcode__mutmut_43, 
    'x_kill_all_simulators_and_xcode__mutmut_44': x_kill_all_simulators_and_xcode__mutmut_44, 
    'x_kill_all_simulators_and_xcode__mutmut_45': x_kill_all_simulators_and_xcode__mutmut_45, 
    'x_kill_all_simulators_and_xcode__mutmut_46': x_kill_all_simulators_and_xcode__mutmut_46, 
    'x_kill_all_simulators_and_xcode__mutmut_47': x_kill_all_simulators_and_xcode__mutmut_47, 
    'x_kill_all_simulators_and_xcode__mutmut_48': x_kill_all_simulators_and_xcode__mutmut_48, 
    'x_kill_all_simulators_and_xcode__mutmut_49': x_kill_all_simulators_and_xcode__mutmut_49, 
    'x_kill_all_simulators_and_xcode__mutmut_50': x_kill_all_simulators_and_xcode__mutmut_50, 
    'x_kill_all_simulators_and_xcode__mutmut_51': x_kill_all_simulators_and_xcode__mutmut_51, 
    'x_kill_all_simulators_and_xcode__mutmut_52': x_kill_all_simulators_and_xcode__mutmut_52, 
    'x_kill_all_simulators_and_xcode__mutmut_53': x_kill_all_simulators_and_xcode__mutmut_53, 
    'x_kill_all_simulators_and_xcode__mutmut_54': x_kill_all_simulators_and_xcode__mutmut_54, 
    'x_kill_all_simulators_and_xcode__mutmut_55': x_kill_all_simulators_and_xcode__mutmut_55, 
    'x_kill_all_simulators_and_xcode__mutmut_56': x_kill_all_simulators_and_xcode__mutmut_56, 
    'x_kill_all_simulators_and_xcode__mutmut_57': x_kill_all_simulators_and_xcode__mutmut_57, 
    'x_kill_all_simulators_and_xcode__mutmut_58': x_kill_all_simulators_and_xcode__mutmut_58
}

def kill_all_simulators_and_xcode(*args, **kwargs):
	result = _mutmut_trampoline(x_kill_all_simulators_and_xcode__mutmut_orig, x_kill_all_simulators_and_xcode__mutmut_mutants, args, kwargs)
	return result 

kill_all_simulators_and_xcode.__signature__ = _mutmut_signature(x_kill_all_simulators_and_xcode__mutmut_orig)
x_kill_all_simulators_and_xcode__mutmut_orig.__name__ = 'x_kill_all_simulators_and_xcode'


def x_kill_all_simulators_and_xcode_admin__mutmut_orig(runner: CommandRunner | None = None) -> Tuple[str, int]:
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


def x_kill_all_simulators_and_xcode_admin__mutmut_1(runner: CommandRunner | None = None) -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn.

	Returns (combined_command, return_code).
	"""
	runner = None
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


def x_kill_all_simulators_and_xcode_admin__mutmut_2(runner: CommandRunner | None = None) -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn.

	Returns (combined_command, return_code).
	"""
	runner = runner and get_default_runner()
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


def x_kill_all_simulators_and_xcode_admin__mutmut_3(runner: CommandRunner | None = None) -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn.

	Returns (combined_command, return_code).
	"""
	runner = runner or get_default_runner()
	# Stop daemon first, then kill processes
	user_scope = None
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


def x_kill_all_simulators_and_xcode_admin__mutmut_4(runner: CommandRunner | None = None) -> Tuple[str, int]:
	"""
	Kill all simulator/Xcode processes with admin privileges.
	Prompts user ONCE for admin password via macOS dialog.

	IMPORTANT: First stops the CoreSimulator launchd daemon to prevent respawn.

	Returns (combined_command, return_code).
	"""
	runner = runner or get_default_runner()
	# Stop daemon first, then kill processes
	user_scope = f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = None
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_5(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXlaunchctl remove com.apple.CoreSimulator.CoreSimulatorServiceXX",
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


def x_kill_all_simulators_and_xcode_admin__mutmut_6(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"launchctl remove com.apple.coresimulator.coresimulatorservice",
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


def x_kill_all_simulators_and_xcode_admin__mutmut_7(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"LAUNCHCTL REMOVE COM.APPLE.CORESIMULATOR.CORESIMULATORSERVICE",
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


def x_kill_all_simulators_and_xcode_admin__mutmut_8(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXpkill -9 -f SimulatorXX",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_9(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"pkill -9 -f simulator",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_10(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"PKILL -9 -F SIMULATOR",
		"pkill -9 -f CoreSimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_11(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXpkill -9 -f CoreSimulatorXX",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_12(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"pkill -9 -f coresimulator",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_13(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"PKILL -9 -F CORESIMULATOR",
		"pkill -9 -f SimulatorTrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_14(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXpkill -9 -f SimulatorTrampolineXX",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_15(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"pkill -9 -f simulatortrampoline",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_16(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"PKILL -9 -F SIMULATORTRAMPOLINE",
		"pkill -9 -f launchd_sim",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_17(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXpkill -9 -f launchd_simXX",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_18(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"PKILL -9 -F LAUNCHD_SIM",
		"killall -9 com.apple.CoreSimulator.CoreSimulatorService",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_19(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXkillall -9 com.apple.CoreSimulator.CoreSimulatorServiceXX",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_20(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"killall -9 com.apple.coresimulator.coresimulatorservice",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_21(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"KILLALL -9 COM.APPLE.CORESIMULATOR.CORESIMULATORSERVICE",
		"pkill -9 -x Xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_22(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"XXpkill -9 -x XcodeXX",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_23(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"pkill -9 -x xcode",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_24(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
		"PKILL -9 -X XCODE",
	]
	combined = " ; ".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_25(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	combined = None
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_26(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	combined = " ; ".join(None)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_27(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	combined = "XX ; XX".join(commands)
	rc = runner.run(["/bin/sh", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_28(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = None
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_29(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(None, sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_30(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/bin/sh", "-c", combined], sudo=None).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_31(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_32(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/bin/sh", "-c", combined], ).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_33(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["XX/bin/shXX", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_34(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/BIN/SH", "-c", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_35(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/bin/sh", "XX-cXX", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_36(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/bin/sh", "-C", combined], sudo=True).returncode
	return (combined, rc)


def x_kill_all_simulators_and_xcode_admin__mutmut_37(runner: CommandRunner | None = None) -> Tuple[str, int]:
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
	rc = runner.run(["/bin/sh", "-c", combined], sudo=False).returncode
	return (combined, rc)

x_kill_all_simulators_and_xcode_admin__mutmut_mutants : ClassVar[MutantDict] = {
'x_kill_all_simulators_and_xcode_admin__mutmut_1': x_kill_all_simulators_and_xcode_admin__mutmut_1, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_2': x_kill_all_simulators_and_xcode_admin__mutmut_2, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_3': x_kill_all_simulators_and_xcode_admin__mutmut_3, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_4': x_kill_all_simulators_and_xcode_admin__mutmut_4, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_5': x_kill_all_simulators_and_xcode_admin__mutmut_5, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_6': x_kill_all_simulators_and_xcode_admin__mutmut_6, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_7': x_kill_all_simulators_and_xcode_admin__mutmut_7, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_8': x_kill_all_simulators_and_xcode_admin__mutmut_8, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_9': x_kill_all_simulators_and_xcode_admin__mutmut_9, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_10': x_kill_all_simulators_and_xcode_admin__mutmut_10, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_11': x_kill_all_simulators_and_xcode_admin__mutmut_11, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_12': x_kill_all_simulators_and_xcode_admin__mutmut_12, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_13': x_kill_all_simulators_and_xcode_admin__mutmut_13, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_14': x_kill_all_simulators_and_xcode_admin__mutmut_14, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_15': x_kill_all_simulators_and_xcode_admin__mutmut_15, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_16': x_kill_all_simulators_and_xcode_admin__mutmut_16, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_17': x_kill_all_simulators_and_xcode_admin__mutmut_17, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_18': x_kill_all_simulators_and_xcode_admin__mutmut_18, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_19': x_kill_all_simulators_and_xcode_admin__mutmut_19, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_20': x_kill_all_simulators_and_xcode_admin__mutmut_20, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_21': x_kill_all_simulators_and_xcode_admin__mutmut_21, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_22': x_kill_all_simulators_and_xcode_admin__mutmut_22, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_23': x_kill_all_simulators_and_xcode_admin__mutmut_23, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_24': x_kill_all_simulators_and_xcode_admin__mutmut_24, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_25': x_kill_all_simulators_and_xcode_admin__mutmut_25, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_26': x_kill_all_simulators_and_xcode_admin__mutmut_26, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_27': x_kill_all_simulators_and_xcode_admin__mutmut_27, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_28': x_kill_all_simulators_and_xcode_admin__mutmut_28, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_29': x_kill_all_simulators_and_xcode_admin__mutmut_29, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_30': x_kill_all_simulators_and_xcode_admin__mutmut_30, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_31': x_kill_all_simulators_and_xcode_admin__mutmut_31, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_32': x_kill_all_simulators_and_xcode_admin__mutmut_32, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_33': x_kill_all_simulators_and_xcode_admin__mutmut_33, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_34': x_kill_all_simulators_and_xcode_admin__mutmut_34, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_35': x_kill_all_simulators_and_xcode_admin__mutmut_35, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_36': x_kill_all_simulators_and_xcode_admin__mutmut_36, 
    'x_kill_all_simulators_and_xcode_admin__mutmut_37': x_kill_all_simulators_and_xcode_admin__mutmut_37
}

def kill_all_simulators_and_xcode_admin(*args, **kwargs):
	result = _mutmut_trampoline(x_kill_all_simulators_and_xcode_admin__mutmut_orig, x_kill_all_simulators_and_xcode_admin__mutmut_mutants, args, kwargs)
	return result 

kill_all_simulators_and_xcode_admin.__signature__ = _mutmut_signature(x_kill_all_simulators_and_xcode_admin__mutmut_orig)
x_kill_all_simulators_and_xcode_admin__mutmut_orig.__name__ = 'x_kill_all_simulators_and_xcode_admin'
