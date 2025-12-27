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


def x_parse_df_output__mutmut_orig(text: str) -> Optional[Dict[str, int]]:
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


def x_parse_df_output__mutmut_1(text: str) -> Optional[Dict[str, int]]:
	"""
	Parse `df -k` output to extract disk space metrics.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `df -k <path>` command.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	lines = None
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


def x_parse_df_output__mutmut_2(text: str) -> Optional[Dict[str, int]]:
	"""
	Parse `df -k` output to extract disk space metrics.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `df -k <path>` command.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	lines = [ln for ln in text.splitlines() if ln.strip()]
	if len(lines) <= 2:
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


def x_parse_df_output__mutmut_3(text: str) -> Optional[Dict[str, int]]:
	"""
	Parse `df -k` output to extract disk space metrics.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `df -k <path>` command.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	lines = [ln for ln in text.splitlines() if ln.strip()]
	if len(lines) < 3:
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


def x_parse_df_output__mutmut_4(text: str) -> Optional[Dict[str, int]]:
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
	parts = None
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


def x_parse_df_output__mutmut_5(text: str) -> Optional[Dict[str, int]]:
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
	parts = lines[+1].split()
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


def x_parse_df_output__mutmut_6(text: str) -> Optional[Dict[str, int]]:
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
	parts = lines[-2].split()
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


def x_parse_df_output__mutmut_7(text: str) -> Optional[Dict[str, int]]:
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
	if len(parts) <= 4:
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


def x_parse_df_output__mutmut_8(text: str) -> Optional[Dict[str, int]]:
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
	if len(parts) < 5:
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


def x_parse_df_output__mutmut_9(text: str) -> Optional[Dict[str, int]]:
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
		blocks_k = None
		used_k = int(parts[2])
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_10(text: str) -> Optional[Dict[str, int]]:
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
		blocks_k = int(None)
		used_k = int(parts[2])
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_11(text: str) -> Optional[Dict[str, int]]:
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
		blocks_k = int(parts[2])
		used_k = int(parts[2])
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_12(text: str) -> Optional[Dict[str, int]]:
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
		used_k = None
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_13(text: str) -> Optional[Dict[str, int]]:
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
		used_k = int(None)
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_14(text: str) -> Optional[Dict[str, int]]:
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
		used_k = int(parts[3])
		avail_k = int(parts[3])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_15(text: str) -> Optional[Dict[str, int]]:
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
		avail_k = None
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_16(text: str) -> Optional[Dict[str, int]]:
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
		avail_k = int(None)
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_17(text: str) -> Optional[Dict[str, int]]:
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
		avail_k = int(parts[4])
	except ValueError:
		return None
	return {
		"blocks_bytes": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_18(text: str) -> Optional[Dict[str, int]]:
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
		"XXblocks_bytesXX": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_19(text: str) -> Optional[Dict[str, int]]:
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
		"BLOCKS_BYTES": blocks_k * 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_20(text: str) -> Optional[Dict[str, int]]:
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
		"blocks_bytes": blocks_k / 1024,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_21(text: str) -> Optional[Dict[str, int]]:
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
		"blocks_bytes": blocks_k * 1025,
		"used_bytes": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_22(text: str) -> Optional[Dict[str, int]]:
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
		"XXused_bytesXX": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_23(text: str) -> Optional[Dict[str, int]]:
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
		"USED_BYTES": used_k * 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_24(text: str) -> Optional[Dict[str, int]]:
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
		"used_bytes": used_k / 1024,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_25(text: str) -> Optional[Dict[str, int]]:
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
		"used_bytes": used_k * 1025,
		"available_bytes": avail_k * 1024,
	}


def x_parse_df_output__mutmut_26(text: str) -> Optional[Dict[str, int]]:
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
		"XXavailable_bytesXX": avail_k * 1024,
	}


def x_parse_df_output__mutmut_27(text: str) -> Optional[Dict[str, int]]:
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
		"AVAILABLE_BYTES": avail_k * 1024,
	}


def x_parse_df_output__mutmut_28(text: str) -> Optional[Dict[str, int]]:
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
		"available_bytes": avail_k / 1024,
	}


def x_parse_df_output__mutmut_29(text: str) -> Optional[Dict[str, int]]:
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
		"available_bytes": avail_k * 1025,
	}

x_parse_df_output__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_df_output__mutmut_1': x_parse_df_output__mutmut_1, 
    'x_parse_df_output__mutmut_2': x_parse_df_output__mutmut_2, 
    'x_parse_df_output__mutmut_3': x_parse_df_output__mutmut_3, 
    'x_parse_df_output__mutmut_4': x_parse_df_output__mutmut_4, 
    'x_parse_df_output__mutmut_5': x_parse_df_output__mutmut_5, 
    'x_parse_df_output__mutmut_6': x_parse_df_output__mutmut_6, 
    'x_parse_df_output__mutmut_7': x_parse_df_output__mutmut_7, 
    'x_parse_df_output__mutmut_8': x_parse_df_output__mutmut_8, 
    'x_parse_df_output__mutmut_9': x_parse_df_output__mutmut_9, 
    'x_parse_df_output__mutmut_10': x_parse_df_output__mutmut_10, 
    'x_parse_df_output__mutmut_11': x_parse_df_output__mutmut_11, 
    'x_parse_df_output__mutmut_12': x_parse_df_output__mutmut_12, 
    'x_parse_df_output__mutmut_13': x_parse_df_output__mutmut_13, 
    'x_parse_df_output__mutmut_14': x_parse_df_output__mutmut_14, 
    'x_parse_df_output__mutmut_15': x_parse_df_output__mutmut_15, 
    'x_parse_df_output__mutmut_16': x_parse_df_output__mutmut_16, 
    'x_parse_df_output__mutmut_17': x_parse_df_output__mutmut_17, 
    'x_parse_df_output__mutmut_18': x_parse_df_output__mutmut_18, 
    'x_parse_df_output__mutmut_19': x_parse_df_output__mutmut_19, 
    'x_parse_df_output__mutmut_20': x_parse_df_output__mutmut_20, 
    'x_parse_df_output__mutmut_21': x_parse_df_output__mutmut_21, 
    'x_parse_df_output__mutmut_22': x_parse_df_output__mutmut_22, 
    'x_parse_df_output__mutmut_23': x_parse_df_output__mutmut_23, 
    'x_parse_df_output__mutmut_24': x_parse_df_output__mutmut_24, 
    'x_parse_df_output__mutmut_25': x_parse_df_output__mutmut_25, 
    'x_parse_df_output__mutmut_26': x_parse_df_output__mutmut_26, 
    'x_parse_df_output__mutmut_27': x_parse_df_output__mutmut_27, 
    'x_parse_df_output__mutmut_28': x_parse_df_output__mutmut_28, 
    'x_parse_df_output__mutmut_29': x_parse_df_output__mutmut_29
}

def parse_df_output(*args, **kwargs):
	result = _mutmut_trampoline(x_parse_df_output__mutmut_orig, x_parse_df_output__mutmut_mutants, args, kwargs)
	return result 

parse_df_output.__signature__ = _mutmut_signature(x_parse_df_output__mutmut_orig)
x_parse_df_output__mutmut_orig.__name__ = 'x_parse_df_output'


def x_df_bytes__mutmut_orig(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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


def x_df_bytes__mutmut_1(path: str = "XX/System/Volumes/DataXX", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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


def x_df_bytes__mutmut_2(path: str = "/system/volumes/data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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


def x_df_bytes__mutmut_3(path: str = "/SYSTEM/VOLUMES/DATA", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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


def x_df_bytes__mutmut_4(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = None
	result = runner.run(["df", "-k", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_5(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner and get_default_runner()
	result = runner.run(["df", "-k", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_6(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = None
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_7(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(None)
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_8(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["XXdfXX", "-k", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_9(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["DF", "-k", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_10(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["df", "XX-kXX", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_11(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
	"""
	Get disk space from `df` command (fallback if APFS query fails).

	Args:
		path: Mount point to query (default: /System/Volumes/Data).
		runner: Optional CommandRunner for dependency injection in tests.

	Returns:
		Dict with blocks_bytes, used_bytes, available_bytes, or None on error.
	"""
	runner = runner or get_default_runner()
	result = runner.run(["df", "-K", path])
	if result.returncode != 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_12(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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
	if result.returncode == 0:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_13(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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
	if result.returncode != 1:
		return None
	return parse_df_output(result.stdout)


def x_df_bytes__mutmut_14(path: str = "/System/Volumes/Data", runner: CommandRunner | None = None) -> Optional[Dict[str, int]]:
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
	return parse_df_output(None)

x_df_bytes__mutmut_mutants : ClassVar[MutantDict] = {
'x_df_bytes__mutmut_1': x_df_bytes__mutmut_1, 
    'x_df_bytes__mutmut_2': x_df_bytes__mutmut_2, 
    'x_df_bytes__mutmut_3': x_df_bytes__mutmut_3, 
    'x_df_bytes__mutmut_4': x_df_bytes__mutmut_4, 
    'x_df_bytes__mutmut_5': x_df_bytes__mutmut_5, 
    'x_df_bytes__mutmut_6': x_df_bytes__mutmut_6, 
    'x_df_bytes__mutmut_7': x_df_bytes__mutmut_7, 
    'x_df_bytes__mutmut_8': x_df_bytes__mutmut_8, 
    'x_df_bytes__mutmut_9': x_df_bytes__mutmut_9, 
    'x_df_bytes__mutmut_10': x_df_bytes__mutmut_10, 
    'x_df_bytes__mutmut_11': x_df_bytes__mutmut_11, 
    'x_df_bytes__mutmut_12': x_df_bytes__mutmut_12, 
    'x_df_bytes__mutmut_13': x_df_bytes__mutmut_13, 
    'x_df_bytes__mutmut_14': x_df_bytes__mutmut_14
}

def df_bytes(*args, **kwargs):
	result = _mutmut_trampoline(x_df_bytes__mutmut_orig, x_df_bytes__mutmut_mutants, args, kwargs)
	return result 

df_bytes.__signature__ = _mutmut_signature(x_df_bytes__mutmut_orig)
x_df_bytes__mutmut_orig.__name__ = 'x_df_bytes'


def x__find_container_for_mount__mutmut_orig(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_1(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get(None, []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_2(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", None):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_3(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get([]):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_4(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", ):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_5(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("XXContainersXX", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_6(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_7(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("CONTAINERS", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_8(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get(None, []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_9(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", None):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_10(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get([]):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_11(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", ):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_12(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("XXVolumesXX", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_13(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_14(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("VOLUMES", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_15(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get(None) == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_16(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("XXMountPointXX") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_17(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("mountpoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_18(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MOUNTPOINT") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_19(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") != mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_20(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = None
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_21(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") and []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_22(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get(None) or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_23(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("XXRolesXX") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_24(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_25(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("ROLES") or []
			if mount_point == "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_26(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" or "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_27(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point != "/System/Volumes/Data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_28(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "XX/System/Volumes/DataXX" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_29(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/system/volumes/data" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_30(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/SYSTEM/VOLUMES/DATA" and "Data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_31(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "XXDataXX" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_32(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "data" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_33(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "DATA" in roles:
				return container
	return None


def x__find_container_for_mount__mutmut_34(apfs_data: dict, mount_point: str) -> Optional[dict]:
	"""Find the APFS container that contains the given mount point."""
	for container in apfs_data.get("Containers", []):
		for volume in container.get("Volumes", []):
			if volume.get("MountPoint") == mount_point:
				return container
			roles = volume.get("Roles") or []
			if mount_point == "/System/Volumes/Data" and "Data" not in roles:
				return container
	return None

x__find_container_for_mount__mutmut_mutants : ClassVar[MutantDict] = {
'x__find_container_for_mount__mutmut_1': x__find_container_for_mount__mutmut_1, 
    'x__find_container_for_mount__mutmut_2': x__find_container_for_mount__mutmut_2, 
    'x__find_container_for_mount__mutmut_3': x__find_container_for_mount__mutmut_3, 
    'x__find_container_for_mount__mutmut_4': x__find_container_for_mount__mutmut_4, 
    'x__find_container_for_mount__mutmut_5': x__find_container_for_mount__mutmut_5, 
    'x__find_container_for_mount__mutmut_6': x__find_container_for_mount__mutmut_6, 
    'x__find_container_for_mount__mutmut_7': x__find_container_for_mount__mutmut_7, 
    'x__find_container_for_mount__mutmut_8': x__find_container_for_mount__mutmut_8, 
    'x__find_container_for_mount__mutmut_9': x__find_container_for_mount__mutmut_9, 
    'x__find_container_for_mount__mutmut_10': x__find_container_for_mount__mutmut_10, 
    'x__find_container_for_mount__mutmut_11': x__find_container_for_mount__mutmut_11, 
    'x__find_container_for_mount__mutmut_12': x__find_container_for_mount__mutmut_12, 
    'x__find_container_for_mount__mutmut_13': x__find_container_for_mount__mutmut_13, 
    'x__find_container_for_mount__mutmut_14': x__find_container_for_mount__mutmut_14, 
    'x__find_container_for_mount__mutmut_15': x__find_container_for_mount__mutmut_15, 
    'x__find_container_for_mount__mutmut_16': x__find_container_for_mount__mutmut_16, 
    'x__find_container_for_mount__mutmut_17': x__find_container_for_mount__mutmut_17, 
    'x__find_container_for_mount__mutmut_18': x__find_container_for_mount__mutmut_18, 
    'x__find_container_for_mount__mutmut_19': x__find_container_for_mount__mutmut_19, 
    'x__find_container_for_mount__mutmut_20': x__find_container_for_mount__mutmut_20, 
    'x__find_container_for_mount__mutmut_21': x__find_container_for_mount__mutmut_21, 
    'x__find_container_for_mount__mutmut_22': x__find_container_for_mount__mutmut_22, 
    'x__find_container_for_mount__mutmut_23': x__find_container_for_mount__mutmut_23, 
    'x__find_container_for_mount__mutmut_24': x__find_container_for_mount__mutmut_24, 
    'x__find_container_for_mount__mutmut_25': x__find_container_for_mount__mutmut_25, 
    'x__find_container_for_mount__mutmut_26': x__find_container_for_mount__mutmut_26, 
    'x__find_container_for_mount__mutmut_27': x__find_container_for_mount__mutmut_27, 
    'x__find_container_for_mount__mutmut_28': x__find_container_for_mount__mutmut_28, 
    'x__find_container_for_mount__mutmut_29': x__find_container_for_mount__mutmut_29, 
    'x__find_container_for_mount__mutmut_30': x__find_container_for_mount__mutmut_30, 
    'x__find_container_for_mount__mutmut_31': x__find_container_for_mount__mutmut_31, 
    'x__find_container_for_mount__mutmut_32': x__find_container_for_mount__mutmut_32, 
    'x__find_container_for_mount__mutmut_33': x__find_container_for_mount__mutmut_33, 
    'x__find_container_for_mount__mutmut_34': x__find_container_for_mount__mutmut_34
}

def _find_container_for_mount(*args, **kwargs):
	result = _mutmut_trampoline(x__find_container_for_mount__mutmut_orig, x__find_container_for_mount__mutmut_mutants, args, kwargs)
	return result 

_find_container_for_mount.__signature__ = _mutmut_signature(x__find_container_for_mount__mutmut_orig)
x__find_container_for_mount__mutmut_orig.__name__ = 'x__find_container_for_mount'


def x_parse_apfs_not_allocated__mutmut_orig(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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


def x_parse_apfs_not_allocated__mutmut_1(plist_bytes: bytes, mount_point: str = "XX/System/Volumes/DataXX") -> Optional[int]:
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


def x_parse_apfs_not_allocated__mutmut_2(plist_bytes: bytes, mount_point: str = "/system/volumes/data") -> Optional[int]:
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


def x_parse_apfs_not_allocated__mutmut_3(plist_bytes: bytes, mount_point: str = "/SYSTEM/VOLUMES/DATA") -> Optional[int]:
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


def x_parse_apfs_not_allocated__mutmut_4(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
		apfs_data = None
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


def x_parse_apfs_not_allocated__mutmut_5(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
		apfs_data = plistlib.loads(None)
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


def x_parse_apfs_not_allocated__mutmut_6(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	container = None
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_7(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	container = _find_container_for_mount(None, mount_point)
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_8(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	container = _find_container_for_mount(apfs_data, None)
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_9(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	container = _find_container_for_mount(mount_point)
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_10(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	container = _find_container_for_mount(apfs_data, )
	if not container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_11(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	if container:
		return None

	for key in ("CapacityNotAllocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_12(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("XXCapacityNotAllocatedXX", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_13(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("capacitynotallocated", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_14(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CAPACITYNOTALLOCATED", "CapacityFree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_15(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "XXCapacityFreeXX", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_16(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "capacityfree", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_17(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "CAPACITYFREE", "CapacityAvailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_18(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "CapacityFree", "XXCapacityAvailableXX"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_19(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "CapacityFree", "capacityavailable"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_20(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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

	for key in ("CapacityNotAllocated", "CapacityFree", "CAPACITYAVAILABLE"):
		value = container.get(key)
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_21(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
		value = None
		if isinstance(value, int):
			return value
	return None


def x_parse_apfs_not_allocated__mutmut_22(plist_bytes: bytes, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
		value = container.get(None)
		if isinstance(value, int):
			return value
	return None

x_parse_apfs_not_allocated__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_apfs_not_allocated__mutmut_1': x_parse_apfs_not_allocated__mutmut_1, 
    'x_parse_apfs_not_allocated__mutmut_2': x_parse_apfs_not_allocated__mutmut_2, 
    'x_parse_apfs_not_allocated__mutmut_3': x_parse_apfs_not_allocated__mutmut_3, 
    'x_parse_apfs_not_allocated__mutmut_4': x_parse_apfs_not_allocated__mutmut_4, 
    'x_parse_apfs_not_allocated__mutmut_5': x_parse_apfs_not_allocated__mutmut_5, 
    'x_parse_apfs_not_allocated__mutmut_6': x_parse_apfs_not_allocated__mutmut_6, 
    'x_parse_apfs_not_allocated__mutmut_7': x_parse_apfs_not_allocated__mutmut_7, 
    'x_parse_apfs_not_allocated__mutmut_8': x_parse_apfs_not_allocated__mutmut_8, 
    'x_parse_apfs_not_allocated__mutmut_9': x_parse_apfs_not_allocated__mutmut_9, 
    'x_parse_apfs_not_allocated__mutmut_10': x_parse_apfs_not_allocated__mutmut_10, 
    'x_parse_apfs_not_allocated__mutmut_11': x_parse_apfs_not_allocated__mutmut_11, 
    'x_parse_apfs_not_allocated__mutmut_12': x_parse_apfs_not_allocated__mutmut_12, 
    'x_parse_apfs_not_allocated__mutmut_13': x_parse_apfs_not_allocated__mutmut_13, 
    'x_parse_apfs_not_allocated__mutmut_14': x_parse_apfs_not_allocated__mutmut_14, 
    'x_parse_apfs_not_allocated__mutmut_15': x_parse_apfs_not_allocated__mutmut_15, 
    'x_parse_apfs_not_allocated__mutmut_16': x_parse_apfs_not_allocated__mutmut_16, 
    'x_parse_apfs_not_allocated__mutmut_17': x_parse_apfs_not_allocated__mutmut_17, 
    'x_parse_apfs_not_allocated__mutmut_18': x_parse_apfs_not_allocated__mutmut_18, 
    'x_parse_apfs_not_allocated__mutmut_19': x_parse_apfs_not_allocated__mutmut_19, 
    'x_parse_apfs_not_allocated__mutmut_20': x_parse_apfs_not_allocated__mutmut_20, 
    'x_parse_apfs_not_allocated__mutmut_21': x_parse_apfs_not_allocated__mutmut_21, 
    'x_parse_apfs_not_allocated__mutmut_22': x_parse_apfs_not_allocated__mutmut_22
}

def parse_apfs_not_allocated(*args, **kwargs):
	result = _mutmut_trampoline(x_parse_apfs_not_allocated__mutmut_orig, x_parse_apfs_not_allocated__mutmut_mutants, args, kwargs)
	return result 

parse_apfs_not_allocated.__signature__ = _mutmut_signature(x_parse_apfs_not_allocated__mutmut_orig)
x_parse_apfs_not_allocated__mutmut_orig.__name__ = 'x_parse_apfs_not_allocated'


def x_get_apfs_available_bytes__mutmut_orig(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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


def x_get_apfs_available_bytes__mutmut_1(runner: CommandRunner | None = None, mount_point: str = "XX/System/Volumes/DataXX") -> Optional[int]:
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


def x_get_apfs_available_bytes__mutmut_2(runner: CommandRunner | None = None, mount_point: str = "/system/volumes/data") -> Optional[int]:
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


def x_get_apfs_available_bytes__mutmut_3(runner: CommandRunner | None = None, mount_point: str = "/SYSTEM/VOLUMES/DATA") -> Optional[int]:
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


def x_get_apfs_available_bytes__mutmut_4(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	runner = None
	result = runner.run(["diskutil", "apfs", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_5(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	runner = runner and get_default_runner()
	result = runner.run(["diskutil", "apfs", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_6(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = None
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_7(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(None, text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_8(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "list", "-plist"], text=None)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_9(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_10(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "list", "-plist"], )
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_11(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["XXdiskutilXX", "apfs", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_12(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["DISKUTIL", "apfs", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_13(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "XXapfsXX", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_14(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "APFS", "list", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_15(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "XXlistXX", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_16(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "LIST", "-plist"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_17(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "list", "XX-plistXX"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_18(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "list", "-PLIST"], text=False)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_19(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	result = runner.run(["diskutil", "apfs", "list", "-plist"], text=True)
	if result.returncode != 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_20(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	if result.returncode == 0:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_21(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	if result.returncode != 1:
		return None
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_22(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = None
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_23(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes and result.stdout.encode("utf-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_24(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode(None, errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_25(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors=None)
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_26(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode(errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_27(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("utf-8", )
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_28(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("XXutf-8XX", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_29(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("UTF-8", errors="replace")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_30(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="XXreplaceXX")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_31(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	payload = result.stdout_bytes or result.stdout.encode("utf-8", errors="REPLACE")
	return parse_apfs_not_allocated(payload, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_32(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	return parse_apfs_not_allocated(None, mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_33(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	return parse_apfs_not_allocated(payload, mount_point=None)


def x_get_apfs_available_bytes__mutmut_34(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	return parse_apfs_not_allocated(mount_point=mount_point)


def x_get_apfs_available_bytes__mutmut_35(runner: CommandRunner | None = None, mount_point: str = "/System/Volumes/Data") -> Optional[int]:
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
	return parse_apfs_not_allocated(payload, )

x_get_apfs_available_bytes__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_apfs_available_bytes__mutmut_1': x_get_apfs_available_bytes__mutmut_1, 
    'x_get_apfs_available_bytes__mutmut_2': x_get_apfs_available_bytes__mutmut_2, 
    'x_get_apfs_available_bytes__mutmut_3': x_get_apfs_available_bytes__mutmut_3, 
    'x_get_apfs_available_bytes__mutmut_4': x_get_apfs_available_bytes__mutmut_4, 
    'x_get_apfs_available_bytes__mutmut_5': x_get_apfs_available_bytes__mutmut_5, 
    'x_get_apfs_available_bytes__mutmut_6': x_get_apfs_available_bytes__mutmut_6, 
    'x_get_apfs_available_bytes__mutmut_7': x_get_apfs_available_bytes__mutmut_7, 
    'x_get_apfs_available_bytes__mutmut_8': x_get_apfs_available_bytes__mutmut_8, 
    'x_get_apfs_available_bytes__mutmut_9': x_get_apfs_available_bytes__mutmut_9, 
    'x_get_apfs_available_bytes__mutmut_10': x_get_apfs_available_bytes__mutmut_10, 
    'x_get_apfs_available_bytes__mutmut_11': x_get_apfs_available_bytes__mutmut_11, 
    'x_get_apfs_available_bytes__mutmut_12': x_get_apfs_available_bytes__mutmut_12, 
    'x_get_apfs_available_bytes__mutmut_13': x_get_apfs_available_bytes__mutmut_13, 
    'x_get_apfs_available_bytes__mutmut_14': x_get_apfs_available_bytes__mutmut_14, 
    'x_get_apfs_available_bytes__mutmut_15': x_get_apfs_available_bytes__mutmut_15, 
    'x_get_apfs_available_bytes__mutmut_16': x_get_apfs_available_bytes__mutmut_16, 
    'x_get_apfs_available_bytes__mutmut_17': x_get_apfs_available_bytes__mutmut_17, 
    'x_get_apfs_available_bytes__mutmut_18': x_get_apfs_available_bytes__mutmut_18, 
    'x_get_apfs_available_bytes__mutmut_19': x_get_apfs_available_bytes__mutmut_19, 
    'x_get_apfs_available_bytes__mutmut_20': x_get_apfs_available_bytes__mutmut_20, 
    'x_get_apfs_available_bytes__mutmut_21': x_get_apfs_available_bytes__mutmut_21, 
    'x_get_apfs_available_bytes__mutmut_22': x_get_apfs_available_bytes__mutmut_22, 
    'x_get_apfs_available_bytes__mutmut_23': x_get_apfs_available_bytes__mutmut_23, 
    'x_get_apfs_available_bytes__mutmut_24': x_get_apfs_available_bytes__mutmut_24, 
    'x_get_apfs_available_bytes__mutmut_25': x_get_apfs_available_bytes__mutmut_25, 
    'x_get_apfs_available_bytes__mutmut_26': x_get_apfs_available_bytes__mutmut_26, 
    'x_get_apfs_available_bytes__mutmut_27': x_get_apfs_available_bytes__mutmut_27, 
    'x_get_apfs_available_bytes__mutmut_28': x_get_apfs_available_bytes__mutmut_28, 
    'x_get_apfs_available_bytes__mutmut_29': x_get_apfs_available_bytes__mutmut_29, 
    'x_get_apfs_available_bytes__mutmut_30': x_get_apfs_available_bytes__mutmut_30, 
    'x_get_apfs_available_bytes__mutmut_31': x_get_apfs_available_bytes__mutmut_31, 
    'x_get_apfs_available_bytes__mutmut_32': x_get_apfs_available_bytes__mutmut_32, 
    'x_get_apfs_available_bytes__mutmut_33': x_get_apfs_available_bytes__mutmut_33, 
    'x_get_apfs_available_bytes__mutmut_34': x_get_apfs_available_bytes__mutmut_34, 
    'x_get_apfs_available_bytes__mutmut_35': x_get_apfs_available_bytes__mutmut_35
}

def get_apfs_available_bytes(*args, **kwargs):
	result = _mutmut_trampoline(x_get_apfs_available_bytes__mutmut_orig, x_get_apfs_available_bytes__mutmut_mutants, args, kwargs)
	return result 

get_apfs_available_bytes.__signature__ = _mutmut_signature(x_get_apfs_available_bytes__mutmut_orig)
x_get_apfs_available_bytes__mutmut_orig.__name__ = 'x_get_apfs_available_bytes'
