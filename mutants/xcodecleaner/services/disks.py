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

from xcodecleaner.core.runner import CommandRunner, get_default_runner


# Keywords to identify simulator-related disk images in diskutil output
DEFAULT_KEYWORDS = ("Simulator", "Xcode", "iOS", "watchOS", "tvOS", "xrOS")
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


def x_parse_diskutil_list__mutmut_orig(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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


def x_parse_diskutil_list__mutmut_1(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
	"""
	Parse `diskutil list` output to find simulator disk slices.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil list` command.
		keywords: Keywords to match (default: Simulator, iOS, etc.).

	Returns:
		List of disk slice identifiers (e.g., ["disk7s1", "disk11s1"]).
	"""
	lines = None
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


def x_parse_diskutil_list__mutmut_2(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
	"""
	Parse `diskutil list` output to find simulator disk slices.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil list` command.
		keywords: Keywords to match (default: Simulator, iOS, etc.).

	Returns:
		List of disk slice identifiers (e.g., ["disk7s1", "disk11s1"]).
	"""
	lines = text.split(None)
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


def x_parse_diskutil_list__mutmut_3(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
	"""
	Parse `diskutil list` output to find simulator disk slices.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil list` command.
		keywords: Keywords to match (default: Simulator, iOS, etc.).

	Returns:
		List of disk slice identifiers (e.g., ["disk7s1", "disk11s1"]).
	"""
	lines = text.split("XX\nXX")
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


def x_parse_diskutil_list__mutmut_4(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
	disks: List[str] = None
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


def x_parse_diskutil_list__mutmut_5(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
	seen: set[str] = None

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


def x_parse_diskutil_list__mutmut_6(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		if any(k in line for k in keywords):
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


def x_parse_diskutil_list__mutmut_7(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		if not any(None):
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


def x_parse_diskutil_list__mutmut_8(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		if not any(k not in line for k in keywords):
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


def x_parse_diskutil_list__mutmut_9(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
			break

		match = re.search(r"\b(disk\d+s\d+)\b", line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_10(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = None
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_11(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(None, line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_12(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(r"\b(disk\d+s\d+)\b", None)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_13(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_14(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(r"\b(disk\d+s\d+)\b", )
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_15(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(r"XX\b(disk\d+s\d+)\bXX", line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_16(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		match = re.search(r"\b(DISK\d+S\d+)\b", line)
		if not match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_17(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		if match:
			continue

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_18(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
			break

		device = match.group(1)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_19(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		device = None
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_20(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		device = match.group(None)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_21(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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

		device = match.group(2)
		if device in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_22(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		if device not in seen:
			continue
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_23(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
			break
		seen.add(device)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_24(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		seen.add(None)
		disks.append(device)

	return disks


def x_parse_diskutil_list__mutmut_25(text: str, keywords: Iterable[str] = DEFAULT_KEYWORDS) -> List[str]:
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
		disks.append(None)

	return disks

x_parse_diskutil_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_diskutil_list__mutmut_1': x_parse_diskutil_list__mutmut_1, 
    'x_parse_diskutil_list__mutmut_2': x_parse_diskutil_list__mutmut_2, 
    'x_parse_diskutil_list__mutmut_3': x_parse_diskutil_list__mutmut_3, 
    'x_parse_diskutil_list__mutmut_4': x_parse_diskutil_list__mutmut_4, 
    'x_parse_diskutil_list__mutmut_5': x_parse_diskutil_list__mutmut_5, 
    'x_parse_diskutil_list__mutmut_6': x_parse_diskutil_list__mutmut_6, 
    'x_parse_diskutil_list__mutmut_7': x_parse_diskutil_list__mutmut_7, 
    'x_parse_diskutil_list__mutmut_8': x_parse_diskutil_list__mutmut_8, 
    'x_parse_diskutil_list__mutmut_9': x_parse_diskutil_list__mutmut_9, 
    'x_parse_diskutil_list__mutmut_10': x_parse_diskutil_list__mutmut_10, 
    'x_parse_diskutil_list__mutmut_11': x_parse_diskutil_list__mutmut_11, 
    'x_parse_diskutil_list__mutmut_12': x_parse_diskutil_list__mutmut_12, 
    'x_parse_diskutil_list__mutmut_13': x_parse_diskutil_list__mutmut_13, 
    'x_parse_diskutil_list__mutmut_14': x_parse_diskutil_list__mutmut_14, 
    'x_parse_diskutil_list__mutmut_15': x_parse_diskutil_list__mutmut_15, 
    'x_parse_diskutil_list__mutmut_16': x_parse_diskutil_list__mutmut_16, 
    'x_parse_diskutil_list__mutmut_17': x_parse_diskutil_list__mutmut_17, 
    'x_parse_diskutil_list__mutmut_18': x_parse_diskutil_list__mutmut_18, 
    'x_parse_diskutil_list__mutmut_19': x_parse_diskutil_list__mutmut_19, 
    'x_parse_diskutil_list__mutmut_20': x_parse_diskutil_list__mutmut_20, 
    'x_parse_diskutil_list__mutmut_21': x_parse_diskutil_list__mutmut_21, 
    'x_parse_diskutil_list__mutmut_22': x_parse_diskutil_list__mutmut_22, 
    'x_parse_diskutil_list__mutmut_23': x_parse_diskutil_list__mutmut_23, 
    'x_parse_diskutil_list__mutmut_24': x_parse_diskutil_list__mutmut_24, 
    'x_parse_diskutil_list__mutmut_25': x_parse_diskutil_list__mutmut_25
}

def parse_diskutil_list(*args, **kwargs):
	result = _mutmut_trampoline(x_parse_diskutil_list__mutmut_orig, x_parse_diskutil_list__mutmut_mutants, args, kwargs)
	return result 

parse_diskutil_list.__signature__ = _mutmut_signature(x_parse_diskutil_list__mutmut_orig)
x_parse_diskutil_list__mutmut_orig.__name__ = 'x_parse_diskutil_list'


def x__parse_size_bytes__mutmut_orig(line: str) -> Tuple[str, Optional[int]]:
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


def x__parse_size_bytes__mutmut_1(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = None
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_2(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(None, 1)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_3(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", None)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_4(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(1)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_5(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", )
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_6(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.rsplit(":", 1)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_7(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split("XX:XX", 1)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_8(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", 2)
	if len(parts) < 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_9(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", 1)
	if len(parts) <= 2:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_10(line: str) -> Tuple[str, Optional[int]]:
	"""
	Parse a size line from diskutil info output.

	Extracts both human-readable size (e.g., "59.6 GB") and exact byte count.

	Args:
		line: A line like "Disk Size: 59.6 GB (64021856256 Bytes)"

	Returns:
		Tuple of (size_string, size_bytes) where size_bytes may be None.
	"""
	parts = line.split(":", 1)
	if len(parts) < 3:
		return "", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_11(line: str) -> Tuple[str, Optional[int]]:
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
		return "XXXX", None
	value = parts[1].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_12(line: str) -> Tuple[str, Optional[int]]:
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
	value = None
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_13(line: str) -> Tuple[str, Optional[int]]:
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
	value = parts[2].strip()
	match = re.search(r"\((\d+)\s+Bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_14(line: str) -> Tuple[str, Optional[int]]:
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
	match = None
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_15(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(None, value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_16(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(r"\((\d+)\s+Bytes\)", None)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_17(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_18(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(r"\((\d+)\s+Bytes\)", )
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_19(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(r"XX\((\d+)\s+Bytes\)XX", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_20(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(r"\((\d+)\s+bytes\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_21(line: str) -> Tuple[str, Optional[int]]:
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
	match = re.search(r"\((\d+)\s+BYTES\)", value)
	size_bytes = int(match.group(1)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_22(line: str) -> Tuple[str, Optional[int]]:
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
	size_bytes = None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_23(line: str) -> Tuple[str, Optional[int]]:
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
	size_bytes = int(None) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_24(line: str) -> Tuple[str, Optional[int]]:
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
	size_bytes = int(match.group(None)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_25(line: str) -> Tuple[str, Optional[int]]:
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
	size_bytes = int(match.group(2)) if match else None
	size_str = value.split("(")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_26(line: str) -> Tuple[str, Optional[int]]:
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
	size_str = None
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_27(line: str) -> Tuple[str, Optional[int]]:
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
	size_str = value.split(None)[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_28(line: str) -> Tuple[str, Optional[int]]:
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
	size_str = value.split("XX(XX")[0].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_29(line: str) -> Tuple[str, Optional[int]]:
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
	size_str = value.split("(")[1].strip() if value else ""
	return size_str, size_bytes


def x__parse_size_bytes__mutmut_30(line: str) -> Tuple[str, Optional[int]]:
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
	size_str = value.split("(")[0].strip() if value else "XXXX"
	return size_str, size_bytes

x__parse_size_bytes__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse_size_bytes__mutmut_1': x__parse_size_bytes__mutmut_1, 
    'x__parse_size_bytes__mutmut_2': x__parse_size_bytes__mutmut_2, 
    'x__parse_size_bytes__mutmut_3': x__parse_size_bytes__mutmut_3, 
    'x__parse_size_bytes__mutmut_4': x__parse_size_bytes__mutmut_4, 
    'x__parse_size_bytes__mutmut_5': x__parse_size_bytes__mutmut_5, 
    'x__parse_size_bytes__mutmut_6': x__parse_size_bytes__mutmut_6, 
    'x__parse_size_bytes__mutmut_7': x__parse_size_bytes__mutmut_7, 
    'x__parse_size_bytes__mutmut_8': x__parse_size_bytes__mutmut_8, 
    'x__parse_size_bytes__mutmut_9': x__parse_size_bytes__mutmut_9, 
    'x__parse_size_bytes__mutmut_10': x__parse_size_bytes__mutmut_10, 
    'x__parse_size_bytes__mutmut_11': x__parse_size_bytes__mutmut_11, 
    'x__parse_size_bytes__mutmut_12': x__parse_size_bytes__mutmut_12, 
    'x__parse_size_bytes__mutmut_13': x__parse_size_bytes__mutmut_13, 
    'x__parse_size_bytes__mutmut_14': x__parse_size_bytes__mutmut_14, 
    'x__parse_size_bytes__mutmut_15': x__parse_size_bytes__mutmut_15, 
    'x__parse_size_bytes__mutmut_16': x__parse_size_bytes__mutmut_16, 
    'x__parse_size_bytes__mutmut_17': x__parse_size_bytes__mutmut_17, 
    'x__parse_size_bytes__mutmut_18': x__parse_size_bytes__mutmut_18, 
    'x__parse_size_bytes__mutmut_19': x__parse_size_bytes__mutmut_19, 
    'x__parse_size_bytes__mutmut_20': x__parse_size_bytes__mutmut_20, 
    'x__parse_size_bytes__mutmut_21': x__parse_size_bytes__mutmut_21, 
    'x__parse_size_bytes__mutmut_22': x__parse_size_bytes__mutmut_22, 
    'x__parse_size_bytes__mutmut_23': x__parse_size_bytes__mutmut_23, 
    'x__parse_size_bytes__mutmut_24': x__parse_size_bytes__mutmut_24, 
    'x__parse_size_bytes__mutmut_25': x__parse_size_bytes__mutmut_25, 
    'x__parse_size_bytes__mutmut_26': x__parse_size_bytes__mutmut_26, 
    'x__parse_size_bytes__mutmut_27': x__parse_size_bytes__mutmut_27, 
    'x__parse_size_bytes__mutmut_28': x__parse_size_bytes__mutmut_28, 
    'x__parse_size_bytes__mutmut_29': x__parse_size_bytes__mutmut_29, 
    'x__parse_size_bytes__mutmut_30': x__parse_size_bytes__mutmut_30
}

def _parse_size_bytes(*args, **kwargs):
	result = _mutmut_trampoline(x__parse_size_bytes__mutmut_orig, x__parse_size_bytes__mutmut_mutants, args, kwargs)
	return result 

_parse_size_bytes.__signature__ = _mutmut_signature(x__parse_size_bytes__mutmut_orig)
x__parse_size_bytes__mutmut_orig.__name__ = 'x__parse_size_bytes'


def x_parse_diskutil_info__mutmut_orig(text: str) -> Dict[str, object]:
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


def x_parse_diskutil_info__mutmut_1(text: str) -> Dict[str, object]:
	"""
	Parse `diskutil info <device>` output to extract disk details.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil info /dev/diskXsY` command.

	Returns:
		Dict with keys: name, mount, size, size_bytes.
	"""
	volume_name = None
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


def x_parse_diskutil_info__mutmut_2(text: str) -> Dict[str, object]:
	"""
	Parse `diskutil info <device>` output to extract disk details.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil info /dev/diskXsY` command.

	Returns:
		Dict with keys: name, mount, size, size_bytes.
	"""
	volume_name = "XXXX"
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


def x_parse_diskutil_info__mutmut_3(text: str) -> Dict[str, object]:
	"""
	Parse `diskutil info <device>` output to extract disk details.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil info /dev/diskXsY` command.

	Returns:
		Dict with keys: name, mount, size, size_bytes.
	"""
	volume_name = ""
	mount_point = None
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


def x_parse_diskutil_info__mutmut_4(text: str) -> Dict[str, object]:
	"""
	Parse `diskutil info <device>` output to extract disk details.

	This is a pure function for easy testing - no side effects.

	Args:
		text: Raw output from `diskutil info /dev/diskXsY` command.

	Returns:
		Dict with keys: name, mount, size, size_bytes.
	"""
	volume_name = ""
	mount_point = "XXXX"
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


def x_parse_diskutil_info__mutmut_5(text: str) -> Dict[str, object]:
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
	size_str = None
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


def x_parse_diskutil_info__mutmut_6(text: str) -> Dict[str, object]:
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
	size_str = "XXXX"
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


def x_parse_diskutil_info__mutmut_7(text: str) -> Dict[str, object]:
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
	size_bytes: Optional[int] = ""

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


def x_parse_diskutil_info__mutmut_8(text: str) -> Dict[str, object]:
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

	for info_line in text.split(None):
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


def x_parse_diskutil_info__mutmut_9(text: str) -> Dict[str, object]:
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

	for info_line in text.split("XX\nXX"):
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


def x_parse_diskutil_info__mutmut_10(text: str) -> Dict[str, object]:
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
		if "XXVolume Name:XX" in info_line:
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


def x_parse_diskutil_info__mutmut_11(text: str) -> Dict[str, object]:
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
		if "volume name:" in info_line:
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


def x_parse_diskutil_info__mutmut_12(text: str) -> Dict[str, object]:
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
		if "VOLUME NAME:" in info_line:
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


def x_parse_diskutil_info__mutmut_13(text: str) -> Dict[str, object]:
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
		if "Volume Name:" not in info_line:
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


def x_parse_diskutil_info__mutmut_14(text: str) -> Dict[str, object]:
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
			volume_name = None
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


def x_parse_diskutil_info__mutmut_15(text: str) -> Dict[str, object]:
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
			volume_name = info_line.split(None)[1].strip()
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


def x_parse_diskutil_info__mutmut_16(text: str) -> Dict[str, object]:
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
			volume_name = info_line.split("XXVolume Name:XX")[1].strip()
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


def x_parse_diskutil_info__mutmut_17(text: str) -> Dict[str, object]:
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
			volume_name = info_line.split("volume name:")[1].strip()
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


def x_parse_diskutil_info__mutmut_18(text: str) -> Dict[str, object]:
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
			volume_name = info_line.split("VOLUME NAME:")[1].strip()
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


def x_parse_diskutil_info__mutmut_19(text: str) -> Dict[str, object]:
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
			volume_name = info_line.split("Volume Name:")[2].strip()
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


def x_parse_diskutil_info__mutmut_20(text: str) -> Dict[str, object]:
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
		elif "XXMount Point:XX" in info_line:
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


def x_parse_diskutil_info__mutmut_21(text: str) -> Dict[str, object]:
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
		elif "mount point:" in info_line:
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


def x_parse_diskutil_info__mutmut_22(text: str) -> Dict[str, object]:
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
		elif "MOUNT POINT:" in info_line:
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


def x_parse_diskutil_info__mutmut_23(text: str) -> Dict[str, object]:
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
		elif "Mount Point:" not in info_line:
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


def x_parse_diskutil_info__mutmut_24(text: str) -> Dict[str, object]:
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
			mount_point = None
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


def x_parse_diskutil_info__mutmut_25(text: str) -> Dict[str, object]:
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
			mount_point = info_line.split(None)[1].strip()
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


def x_parse_diskutil_info__mutmut_26(text: str) -> Dict[str, object]:
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
			mount_point = info_line.split("XXMount Point:XX")[1].strip()
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


def x_parse_diskutil_info__mutmut_27(text: str) -> Dict[str, object]:
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
			mount_point = info_line.split("mount point:")[1].strip()
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


def x_parse_diskutil_info__mutmut_28(text: str) -> Dict[str, object]:
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
			mount_point = info_line.split("MOUNT POINT:")[1].strip()
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


def x_parse_diskutil_info__mutmut_29(text: str) -> Dict[str, object]:
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
			mount_point = info_line.split("Mount Point:")[2].strip()
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


def x_parse_diskutil_info__mutmut_30(text: str) -> Dict[str, object]:
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
		elif "XXDisk Size:XX" in info_line:
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


def x_parse_diskutil_info__mutmut_31(text: str) -> Dict[str, object]:
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
		elif "disk size:" in info_line:
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


def x_parse_diskutil_info__mutmut_32(text: str) -> Dict[str, object]:
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
		elif "DISK SIZE:" in info_line:
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


def x_parse_diskutil_info__mutmut_33(text: str) -> Dict[str, object]:
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
		elif "Disk Size:" not in info_line:
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


def x_parse_diskutil_info__mutmut_34(text: str) -> Dict[str, object]:
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
			size_str, size_bytes = None
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


def x_parse_diskutil_info__mutmut_35(text: str) -> Dict[str, object]:
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
			size_str, size_bytes = _parse_size_bytes(None)
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


def x_parse_diskutil_info__mutmut_36(text: str) -> Dict[str, object]:
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
		elif "Total Size:" in info_line or not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_37(text: str) -> Dict[str, object]:
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
		elif "XXTotal Size:XX" in info_line and not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_38(text: str) -> Dict[str, object]:
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
		elif "total size:" in info_line and not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_39(text: str) -> Dict[str, object]:
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
		elif "TOTAL SIZE:" in info_line and not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_40(text: str) -> Dict[str, object]:
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
		elif "Total Size:" not in info_line and not size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_41(text: str) -> Dict[str, object]:
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
		elif "Total Size:" in info_line and size_str:
			size_str, size_bytes = _parse_size_bytes(info_line)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_42(text: str) -> Dict[str, object]:
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
			size_str, size_bytes = None

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_43(text: str) -> Dict[str, object]:
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
			size_str, size_bytes = _parse_size_bytes(None)

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_44(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("not applicable") and mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_45(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith(None) or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_46(text: str) -> Dict[str, object]:
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

	if mount_point.upper().startswith("not applicable") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_47(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("XXnot applicableXX") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_48(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("NOT APPLICABLE") or mount_point.lower().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_49(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith(None):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_50(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("not applicable") or mount_point.upper().startswith("not mounted"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_51(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("XXnot mountedXX"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_52(text: str) -> Dict[str, object]:
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

	if mount_point.lower().startswith("not applicable") or mount_point.lower().startswith("NOT MOUNTED"):
		mount_point = ""

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_53(text: str) -> Dict[str, object]:
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
		mount_point = None

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_54(text: str) -> Dict[str, object]:
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
		mount_point = "XXXX"

	return {
		"name": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_55(text: str) -> Dict[str, object]:
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
		"XXnameXX": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_56(text: str) -> Dict[str, object]:
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
		"NAME": volume_name or "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_57(text: str) -> Dict[str, object]:
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
		"name": volume_name and "Unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_58(text: str) -> Dict[str, object]:
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
		"name": volume_name or "XXUnknownXX",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_59(text: str) -> Dict[str, object]:
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
		"name": volume_name or "unknown",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_60(text: str) -> Dict[str, object]:
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
		"name": volume_name or "UNKNOWN",
		"mount": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_61(text: str) -> Dict[str, object]:
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
		"XXmountXX": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_62(text: str) -> Dict[str, object]:
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
		"MOUNT": mount_point or "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_63(text: str) -> Dict[str, object]:
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
		"mount": mount_point and "Not Mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_64(text: str) -> Dict[str, object]:
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
		"mount": mount_point or "XXNot MountedXX",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_65(text: str) -> Dict[str, object]:
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
		"mount": mount_point or "not mounted",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_66(text: str) -> Dict[str, object]:
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
		"mount": mount_point or "NOT MOUNTED",
		"size": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_67(text: str) -> Dict[str, object]:
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
		"XXsizeXX": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_68(text: str) -> Dict[str, object]:
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
		"SIZE": size_str or "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_69(text: str) -> Dict[str, object]:
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
		"size": size_str and "Unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_70(text: str) -> Dict[str, object]:
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
		"size": size_str or "XXUnknownXX",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_71(text: str) -> Dict[str, object]:
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
		"size": size_str or "unknown",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_72(text: str) -> Dict[str, object]:
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
		"size": size_str or "UNKNOWN",
		"size_bytes": size_bytes,
	}


def x_parse_diskutil_info__mutmut_73(text: str) -> Dict[str, object]:
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
		"XXsize_bytesXX": size_bytes,
	}


def x_parse_diskutil_info__mutmut_74(text: str) -> Dict[str, object]:
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
		"SIZE_BYTES": size_bytes,
	}

x_parse_diskutil_info__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_diskutil_info__mutmut_1': x_parse_diskutil_info__mutmut_1, 
    'x_parse_diskutil_info__mutmut_2': x_parse_diskutil_info__mutmut_2, 
    'x_parse_diskutil_info__mutmut_3': x_parse_diskutil_info__mutmut_3, 
    'x_parse_diskutil_info__mutmut_4': x_parse_diskutil_info__mutmut_4, 
    'x_parse_diskutil_info__mutmut_5': x_parse_diskutil_info__mutmut_5, 
    'x_parse_diskutil_info__mutmut_6': x_parse_diskutil_info__mutmut_6, 
    'x_parse_diskutil_info__mutmut_7': x_parse_diskutil_info__mutmut_7, 
    'x_parse_diskutil_info__mutmut_8': x_parse_diskutil_info__mutmut_8, 
    'x_parse_diskutil_info__mutmut_9': x_parse_diskutil_info__mutmut_9, 
    'x_parse_diskutil_info__mutmut_10': x_parse_diskutil_info__mutmut_10, 
    'x_parse_diskutil_info__mutmut_11': x_parse_diskutil_info__mutmut_11, 
    'x_parse_diskutil_info__mutmut_12': x_parse_diskutil_info__mutmut_12, 
    'x_parse_diskutil_info__mutmut_13': x_parse_diskutil_info__mutmut_13, 
    'x_parse_diskutil_info__mutmut_14': x_parse_diskutil_info__mutmut_14, 
    'x_parse_diskutil_info__mutmut_15': x_parse_diskutil_info__mutmut_15, 
    'x_parse_diskutil_info__mutmut_16': x_parse_diskutil_info__mutmut_16, 
    'x_parse_diskutil_info__mutmut_17': x_parse_diskutil_info__mutmut_17, 
    'x_parse_diskutil_info__mutmut_18': x_parse_diskutil_info__mutmut_18, 
    'x_parse_diskutil_info__mutmut_19': x_parse_diskutil_info__mutmut_19, 
    'x_parse_diskutil_info__mutmut_20': x_parse_diskutil_info__mutmut_20, 
    'x_parse_diskutil_info__mutmut_21': x_parse_diskutil_info__mutmut_21, 
    'x_parse_diskutil_info__mutmut_22': x_parse_diskutil_info__mutmut_22, 
    'x_parse_diskutil_info__mutmut_23': x_parse_diskutil_info__mutmut_23, 
    'x_parse_diskutil_info__mutmut_24': x_parse_diskutil_info__mutmut_24, 
    'x_parse_diskutil_info__mutmut_25': x_parse_diskutil_info__mutmut_25, 
    'x_parse_diskutil_info__mutmut_26': x_parse_diskutil_info__mutmut_26, 
    'x_parse_diskutil_info__mutmut_27': x_parse_diskutil_info__mutmut_27, 
    'x_parse_diskutil_info__mutmut_28': x_parse_diskutil_info__mutmut_28, 
    'x_parse_diskutil_info__mutmut_29': x_parse_diskutil_info__mutmut_29, 
    'x_parse_diskutil_info__mutmut_30': x_parse_diskutil_info__mutmut_30, 
    'x_parse_diskutil_info__mutmut_31': x_parse_diskutil_info__mutmut_31, 
    'x_parse_diskutil_info__mutmut_32': x_parse_diskutil_info__mutmut_32, 
    'x_parse_diskutil_info__mutmut_33': x_parse_diskutil_info__mutmut_33, 
    'x_parse_diskutil_info__mutmut_34': x_parse_diskutil_info__mutmut_34, 
    'x_parse_diskutil_info__mutmut_35': x_parse_diskutil_info__mutmut_35, 
    'x_parse_diskutil_info__mutmut_36': x_parse_diskutil_info__mutmut_36, 
    'x_parse_diskutil_info__mutmut_37': x_parse_diskutil_info__mutmut_37, 
    'x_parse_diskutil_info__mutmut_38': x_parse_diskutil_info__mutmut_38, 
    'x_parse_diskutil_info__mutmut_39': x_parse_diskutil_info__mutmut_39, 
    'x_parse_diskutil_info__mutmut_40': x_parse_diskutil_info__mutmut_40, 
    'x_parse_diskutil_info__mutmut_41': x_parse_diskutil_info__mutmut_41, 
    'x_parse_diskutil_info__mutmut_42': x_parse_diskutil_info__mutmut_42, 
    'x_parse_diskutil_info__mutmut_43': x_parse_diskutil_info__mutmut_43, 
    'x_parse_diskutil_info__mutmut_44': x_parse_diskutil_info__mutmut_44, 
    'x_parse_diskutil_info__mutmut_45': x_parse_diskutil_info__mutmut_45, 
    'x_parse_diskutil_info__mutmut_46': x_parse_diskutil_info__mutmut_46, 
    'x_parse_diskutil_info__mutmut_47': x_parse_diskutil_info__mutmut_47, 
    'x_parse_diskutil_info__mutmut_48': x_parse_diskutil_info__mutmut_48, 
    'x_parse_diskutil_info__mutmut_49': x_parse_diskutil_info__mutmut_49, 
    'x_parse_diskutil_info__mutmut_50': x_parse_diskutil_info__mutmut_50, 
    'x_parse_diskutil_info__mutmut_51': x_parse_diskutil_info__mutmut_51, 
    'x_parse_diskutil_info__mutmut_52': x_parse_diskutil_info__mutmut_52, 
    'x_parse_diskutil_info__mutmut_53': x_parse_diskutil_info__mutmut_53, 
    'x_parse_diskutil_info__mutmut_54': x_parse_diskutil_info__mutmut_54, 
    'x_parse_diskutil_info__mutmut_55': x_parse_diskutil_info__mutmut_55, 
    'x_parse_diskutil_info__mutmut_56': x_parse_diskutil_info__mutmut_56, 
    'x_parse_diskutil_info__mutmut_57': x_parse_diskutil_info__mutmut_57, 
    'x_parse_diskutil_info__mutmut_58': x_parse_diskutil_info__mutmut_58, 
    'x_parse_diskutil_info__mutmut_59': x_parse_diskutil_info__mutmut_59, 
    'x_parse_diskutil_info__mutmut_60': x_parse_diskutil_info__mutmut_60, 
    'x_parse_diskutil_info__mutmut_61': x_parse_diskutil_info__mutmut_61, 
    'x_parse_diskutil_info__mutmut_62': x_parse_diskutil_info__mutmut_62, 
    'x_parse_diskutil_info__mutmut_63': x_parse_diskutil_info__mutmut_63, 
    'x_parse_diskutil_info__mutmut_64': x_parse_diskutil_info__mutmut_64, 
    'x_parse_diskutil_info__mutmut_65': x_parse_diskutil_info__mutmut_65, 
    'x_parse_diskutil_info__mutmut_66': x_parse_diskutil_info__mutmut_66, 
    'x_parse_diskutil_info__mutmut_67': x_parse_diskutil_info__mutmut_67, 
    'x_parse_diskutil_info__mutmut_68': x_parse_diskutil_info__mutmut_68, 
    'x_parse_diskutil_info__mutmut_69': x_parse_diskutil_info__mutmut_69, 
    'x_parse_diskutil_info__mutmut_70': x_parse_diskutil_info__mutmut_70, 
    'x_parse_diskutil_info__mutmut_71': x_parse_diskutil_info__mutmut_71, 
    'x_parse_diskutil_info__mutmut_72': x_parse_diskutil_info__mutmut_72, 
    'x_parse_diskutil_info__mutmut_73': x_parse_diskutil_info__mutmut_73, 
    'x_parse_diskutil_info__mutmut_74': x_parse_diskutil_info__mutmut_74
}

def parse_diskutil_info(*args, **kwargs):
	result = _mutmut_trampoline(x_parse_diskutil_info__mutmut_orig, x_parse_diskutil_info__mutmut_mutants, args, kwargs)
	return result 

parse_diskutil_info.__signature__ = _mutmut_signature(x_parse_diskutil_info__mutmut_orig)
x_parse_diskutil_info__mutmut_orig.__name__ = 'x_parse_diskutil_info'


def x_list_simulator_disks__mutmut_orig(
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


def x_list_simulator_disks__mutmut_1(
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
	runner = None
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


def x_list_simulator_disks__mutmut_2(
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
	runner = runner and get_default_runner()
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


def x_list_simulator_disks__mutmut_3(
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
	result = None
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


def x_list_simulator_disks__mutmut_4(
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
	result = runner.run(None)
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


def x_list_simulator_disks__mutmut_5(
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
	result = runner.run(["XXdiskutilXX", "list"])
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


def x_list_simulator_disks__mutmut_6(
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
	result = runner.run(["DISKUTIL", "list"])
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


def x_list_simulator_disks__mutmut_7(
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
	result = runner.run(["diskutil", "XXlistXX"])
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


def x_list_simulator_disks__mutmut_8(
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
	result = runner.run(["diskutil", "LIST"])
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


def x_list_simulator_disks__mutmut_9(
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
	lines = None
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


def x_list_simulator_disks__mutmut_10(
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
	lines = result.stdout.split(None)
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


def x_list_simulator_disks__mutmut_11(
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
	lines = result.stdout.split("XX\nXX")
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


def x_list_simulator_disks__mutmut_12(
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
	disk_info: List[Dict[str, object]] = None

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


def x_list_simulator_disks__mutmut_13(
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

	devices = None
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


def x_list_simulator_disks__mutmut_14(
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

	devices = parse_diskutil_list(None)
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


def x_list_simulator_disks__mutmut_15(
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
	for i, device in enumerate(None):
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


def x_list_simulator_disks__mutmut_16(
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
				progress_callback(None)
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


def x_list_simulator_disks__mutmut_17(
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
				progress_callback(int(None))
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


def x_list_simulator_disks__mutmut_18(
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
				progress_callback(int((i / max(1, len(devices))) / 100))
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


def x_list_simulator_disks__mutmut_19(
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
				progress_callback(int((i * max(1, len(devices))) * 100))
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


def x_list_simulator_disks__mutmut_20(
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
				progress_callback(int((i / max(None, len(devices))) * 100))
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


def x_list_simulator_disks__mutmut_21(
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
				progress_callback(int((i / max(1, None)) * 100))
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


def x_list_simulator_disks__mutmut_22(
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
				progress_callback(int((i / max(len(devices))) * 100))
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


def x_list_simulator_disks__mutmut_23(
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
				progress_callback(int((i / max(1, )) * 100))
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


def x_list_simulator_disks__mutmut_24(
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
				progress_callback(int((i / max(2, len(devices))) * 100))
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


def x_list_simulator_disks__mutmut_25(
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
				progress_callback(int((i / max(1, len(devices))) * 101))
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


def x_list_simulator_disks__mutmut_26(
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

		device_path = None
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


def x_list_simulator_disks__mutmut_27(
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
		info_result = None
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


def x_list_simulator_disks__mutmut_28(
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
		info_result = runner.run(None)
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


def x_list_simulator_disks__mutmut_29(
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
		info_result = runner.run(["XXdiskutilXX", "info", device_path])
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


def x_list_simulator_disks__mutmut_30(
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
		info_result = runner.run(["DISKUTIL", "info", device_path])
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


def x_list_simulator_disks__mutmut_31(
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
		info_result = runner.run(["diskutil", "XXinfoXX", device_path])
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


def x_list_simulator_disks__mutmut_32(
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
		info_result = runner.run(["diskutil", "INFO", device_path])
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


def x_list_simulator_disks__mutmut_33(
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
		parsed = None

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


def x_list_simulator_disks__mutmut_34(
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
		parsed = parse_diskutil_info(None)

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


def x_list_simulator_disks__mutmut_35(
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

		if parsed.get("name") and parsed.get("mount"):
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


def x_list_simulator_disks__mutmut_36(
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

		if parsed.get(None) or parsed.get("mount"):
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


def x_list_simulator_disks__mutmut_37(
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

		if parsed.get("XXnameXX") or parsed.get("mount"):
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


def x_list_simulator_disks__mutmut_38(
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

		if parsed.get("NAME") or parsed.get("mount"):
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


def x_list_simulator_disks__mutmut_39(
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

		if parsed.get("name") or parsed.get(None):
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


def x_list_simulator_disks__mutmut_40(
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

		if parsed.get("name") or parsed.get("XXmountXX"):
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


def x_list_simulator_disks__mutmut_41(
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

		if parsed.get("name") or parsed.get("MOUNT"):
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


def x_list_simulator_disks__mutmut_42(
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
				None
			)
	return disk_info


def x_list_simulator_disks__mutmut_43(
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
					"XXdeviceXX": device_path,
					"name": parsed.get("name", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_44(
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
					"DEVICE": device_path,
					"name": parsed.get("name", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_45(
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
					"XXnameXX": parsed.get("name", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_46(
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
					"NAME": parsed.get("name", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_47(
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
					"name": parsed.get(None, "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_48(
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
					"name": parsed.get("name", None),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_49(
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
					"name": parsed.get("Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_50(
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
					"name": parsed.get("name", ),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_51(
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
					"name": parsed.get("XXnameXX", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_52(
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
					"name": parsed.get("NAME", "Unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_53(
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
					"name": parsed.get("name", "XXUnknownXX"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_54(
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
					"name": parsed.get("name", "unknown"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_55(
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
					"name": parsed.get("name", "UNKNOWN"),
					"mount": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_56(
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
					"XXmountXX": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_57(
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
					"MOUNT": parsed.get("mount", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_58(
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
					"mount": parsed.get(None, "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_59(
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
					"mount": parsed.get("mount", None),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_60(
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
					"mount": parsed.get("Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_61(
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
					"mount": parsed.get("mount", ),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_62(
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
					"mount": parsed.get("XXmountXX", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_63(
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
					"mount": parsed.get("MOUNT", "Not Mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_64(
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
					"mount": parsed.get("mount", "XXNot MountedXX"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_65(
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
					"mount": parsed.get("mount", "not mounted"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_66(
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
					"mount": parsed.get("mount", "NOT MOUNTED"),
					"size": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_67(
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
					"XXsizeXX": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_68(
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
					"SIZE": parsed.get("size", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_69(
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
					"size": parsed.get(None, "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_70(
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
					"size": parsed.get("size", None),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_71(
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
					"size": parsed.get("Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_72(
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
					"size": parsed.get("size", ),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_73(
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
					"size": parsed.get("XXsizeXX", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_74(
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
					"size": parsed.get("SIZE", "Unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_75(
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
					"size": parsed.get("size", "XXUnknownXX"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_76(
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
					"size": parsed.get("size", "unknown"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_77(
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
					"size": parsed.get("size", "UNKNOWN"),
					"size_bytes": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_78(
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
					"XXsize_bytesXX": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_79(
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
					"SIZE_BYTES": parsed.get("size_bytes"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_80(
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
					"size_bytes": parsed.get(None),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_81(
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
					"size_bytes": parsed.get("XXsize_bytesXX"),
				}
			)
	return disk_info


def x_list_simulator_disks__mutmut_82(
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
					"size_bytes": parsed.get("SIZE_BYTES"),
				}
			)
	return disk_info

x_list_simulator_disks__mutmut_mutants : ClassVar[MutantDict] = {
'x_list_simulator_disks__mutmut_1': x_list_simulator_disks__mutmut_1, 
    'x_list_simulator_disks__mutmut_2': x_list_simulator_disks__mutmut_2, 
    'x_list_simulator_disks__mutmut_3': x_list_simulator_disks__mutmut_3, 
    'x_list_simulator_disks__mutmut_4': x_list_simulator_disks__mutmut_4, 
    'x_list_simulator_disks__mutmut_5': x_list_simulator_disks__mutmut_5, 
    'x_list_simulator_disks__mutmut_6': x_list_simulator_disks__mutmut_6, 
    'x_list_simulator_disks__mutmut_7': x_list_simulator_disks__mutmut_7, 
    'x_list_simulator_disks__mutmut_8': x_list_simulator_disks__mutmut_8, 
    'x_list_simulator_disks__mutmut_9': x_list_simulator_disks__mutmut_9, 
    'x_list_simulator_disks__mutmut_10': x_list_simulator_disks__mutmut_10, 
    'x_list_simulator_disks__mutmut_11': x_list_simulator_disks__mutmut_11, 
    'x_list_simulator_disks__mutmut_12': x_list_simulator_disks__mutmut_12, 
    'x_list_simulator_disks__mutmut_13': x_list_simulator_disks__mutmut_13, 
    'x_list_simulator_disks__mutmut_14': x_list_simulator_disks__mutmut_14, 
    'x_list_simulator_disks__mutmut_15': x_list_simulator_disks__mutmut_15, 
    'x_list_simulator_disks__mutmut_16': x_list_simulator_disks__mutmut_16, 
    'x_list_simulator_disks__mutmut_17': x_list_simulator_disks__mutmut_17, 
    'x_list_simulator_disks__mutmut_18': x_list_simulator_disks__mutmut_18, 
    'x_list_simulator_disks__mutmut_19': x_list_simulator_disks__mutmut_19, 
    'x_list_simulator_disks__mutmut_20': x_list_simulator_disks__mutmut_20, 
    'x_list_simulator_disks__mutmut_21': x_list_simulator_disks__mutmut_21, 
    'x_list_simulator_disks__mutmut_22': x_list_simulator_disks__mutmut_22, 
    'x_list_simulator_disks__mutmut_23': x_list_simulator_disks__mutmut_23, 
    'x_list_simulator_disks__mutmut_24': x_list_simulator_disks__mutmut_24, 
    'x_list_simulator_disks__mutmut_25': x_list_simulator_disks__mutmut_25, 
    'x_list_simulator_disks__mutmut_26': x_list_simulator_disks__mutmut_26, 
    'x_list_simulator_disks__mutmut_27': x_list_simulator_disks__mutmut_27, 
    'x_list_simulator_disks__mutmut_28': x_list_simulator_disks__mutmut_28, 
    'x_list_simulator_disks__mutmut_29': x_list_simulator_disks__mutmut_29, 
    'x_list_simulator_disks__mutmut_30': x_list_simulator_disks__mutmut_30, 
    'x_list_simulator_disks__mutmut_31': x_list_simulator_disks__mutmut_31, 
    'x_list_simulator_disks__mutmut_32': x_list_simulator_disks__mutmut_32, 
    'x_list_simulator_disks__mutmut_33': x_list_simulator_disks__mutmut_33, 
    'x_list_simulator_disks__mutmut_34': x_list_simulator_disks__mutmut_34, 
    'x_list_simulator_disks__mutmut_35': x_list_simulator_disks__mutmut_35, 
    'x_list_simulator_disks__mutmut_36': x_list_simulator_disks__mutmut_36, 
    'x_list_simulator_disks__mutmut_37': x_list_simulator_disks__mutmut_37, 
    'x_list_simulator_disks__mutmut_38': x_list_simulator_disks__mutmut_38, 
    'x_list_simulator_disks__mutmut_39': x_list_simulator_disks__mutmut_39, 
    'x_list_simulator_disks__mutmut_40': x_list_simulator_disks__mutmut_40, 
    'x_list_simulator_disks__mutmut_41': x_list_simulator_disks__mutmut_41, 
    'x_list_simulator_disks__mutmut_42': x_list_simulator_disks__mutmut_42, 
    'x_list_simulator_disks__mutmut_43': x_list_simulator_disks__mutmut_43, 
    'x_list_simulator_disks__mutmut_44': x_list_simulator_disks__mutmut_44, 
    'x_list_simulator_disks__mutmut_45': x_list_simulator_disks__mutmut_45, 
    'x_list_simulator_disks__mutmut_46': x_list_simulator_disks__mutmut_46, 
    'x_list_simulator_disks__mutmut_47': x_list_simulator_disks__mutmut_47, 
    'x_list_simulator_disks__mutmut_48': x_list_simulator_disks__mutmut_48, 
    'x_list_simulator_disks__mutmut_49': x_list_simulator_disks__mutmut_49, 
    'x_list_simulator_disks__mutmut_50': x_list_simulator_disks__mutmut_50, 
    'x_list_simulator_disks__mutmut_51': x_list_simulator_disks__mutmut_51, 
    'x_list_simulator_disks__mutmut_52': x_list_simulator_disks__mutmut_52, 
    'x_list_simulator_disks__mutmut_53': x_list_simulator_disks__mutmut_53, 
    'x_list_simulator_disks__mutmut_54': x_list_simulator_disks__mutmut_54, 
    'x_list_simulator_disks__mutmut_55': x_list_simulator_disks__mutmut_55, 
    'x_list_simulator_disks__mutmut_56': x_list_simulator_disks__mutmut_56, 
    'x_list_simulator_disks__mutmut_57': x_list_simulator_disks__mutmut_57, 
    'x_list_simulator_disks__mutmut_58': x_list_simulator_disks__mutmut_58, 
    'x_list_simulator_disks__mutmut_59': x_list_simulator_disks__mutmut_59, 
    'x_list_simulator_disks__mutmut_60': x_list_simulator_disks__mutmut_60, 
    'x_list_simulator_disks__mutmut_61': x_list_simulator_disks__mutmut_61, 
    'x_list_simulator_disks__mutmut_62': x_list_simulator_disks__mutmut_62, 
    'x_list_simulator_disks__mutmut_63': x_list_simulator_disks__mutmut_63, 
    'x_list_simulator_disks__mutmut_64': x_list_simulator_disks__mutmut_64, 
    'x_list_simulator_disks__mutmut_65': x_list_simulator_disks__mutmut_65, 
    'x_list_simulator_disks__mutmut_66': x_list_simulator_disks__mutmut_66, 
    'x_list_simulator_disks__mutmut_67': x_list_simulator_disks__mutmut_67, 
    'x_list_simulator_disks__mutmut_68': x_list_simulator_disks__mutmut_68, 
    'x_list_simulator_disks__mutmut_69': x_list_simulator_disks__mutmut_69, 
    'x_list_simulator_disks__mutmut_70': x_list_simulator_disks__mutmut_70, 
    'x_list_simulator_disks__mutmut_71': x_list_simulator_disks__mutmut_71, 
    'x_list_simulator_disks__mutmut_72': x_list_simulator_disks__mutmut_72, 
    'x_list_simulator_disks__mutmut_73': x_list_simulator_disks__mutmut_73, 
    'x_list_simulator_disks__mutmut_74': x_list_simulator_disks__mutmut_74, 
    'x_list_simulator_disks__mutmut_75': x_list_simulator_disks__mutmut_75, 
    'x_list_simulator_disks__mutmut_76': x_list_simulator_disks__mutmut_76, 
    'x_list_simulator_disks__mutmut_77': x_list_simulator_disks__mutmut_77, 
    'x_list_simulator_disks__mutmut_78': x_list_simulator_disks__mutmut_78, 
    'x_list_simulator_disks__mutmut_79': x_list_simulator_disks__mutmut_79, 
    'x_list_simulator_disks__mutmut_80': x_list_simulator_disks__mutmut_80, 
    'x_list_simulator_disks__mutmut_81': x_list_simulator_disks__mutmut_81, 
    'x_list_simulator_disks__mutmut_82': x_list_simulator_disks__mutmut_82
}

def list_simulator_disks(*args, **kwargs):
	result = _mutmut_trampoline(x_list_simulator_disks__mutmut_orig, x_list_simulator_disks__mutmut_mutants, args, kwargs)
	return result 

list_simulator_disks.__signature__ = _mutmut_signature(x_list_simulator_disks__mutmut_orig)
x_list_simulator_disks__mutmut_orig.__name__ = 'x_list_simulator_disks'


def x__get_parent_disk__mutmut_orig(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_1(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith(None):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_2(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("XXdiskXX"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_3(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("DISK"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_4(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = None
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_5(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = None
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_6(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(None, device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_7(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", None)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_8(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_9(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", )
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_10(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"XX(/dev/disk\d+)XX", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_11(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/DEV/DISK\d+)", device)
	return match.group(1) if match else device


def x__get_parent_disk__mutmut_12(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(None) if match else device


def x__get_parent_disk__mutmut_13(device: str) -> str:
	"""Convert disk slice (/dev/disk7s1) to parent disk (/dev/disk7)."""
	if device.startswith("disk"):
		device = f"/dev/{device}"
	match = re.match(r"(/dev/disk\d+)", device)
	return match.group(2) if match else device

x__get_parent_disk__mutmut_mutants : ClassVar[MutantDict] = {
'x__get_parent_disk__mutmut_1': x__get_parent_disk__mutmut_1, 
    'x__get_parent_disk__mutmut_2': x__get_parent_disk__mutmut_2, 
    'x__get_parent_disk__mutmut_3': x__get_parent_disk__mutmut_3, 
    'x__get_parent_disk__mutmut_4': x__get_parent_disk__mutmut_4, 
    'x__get_parent_disk__mutmut_5': x__get_parent_disk__mutmut_5, 
    'x__get_parent_disk__mutmut_6': x__get_parent_disk__mutmut_6, 
    'x__get_parent_disk__mutmut_7': x__get_parent_disk__mutmut_7, 
    'x__get_parent_disk__mutmut_8': x__get_parent_disk__mutmut_8, 
    'x__get_parent_disk__mutmut_9': x__get_parent_disk__mutmut_9, 
    'x__get_parent_disk__mutmut_10': x__get_parent_disk__mutmut_10, 
    'x__get_parent_disk__mutmut_11': x__get_parent_disk__mutmut_11, 
    'x__get_parent_disk__mutmut_12': x__get_parent_disk__mutmut_12, 
    'x__get_parent_disk__mutmut_13': x__get_parent_disk__mutmut_13
}

def _get_parent_disk(*args, **kwargs):
	result = _mutmut_trampoline(x__get_parent_disk__mutmut_orig, x__get_parent_disk__mutmut_mutants, args, kwargs)
	return result 

_get_parent_disk.__signature__ = _mutmut_signature(x__get_parent_disk__mutmut_orig)
x__get_parent_disk__mutmut_orig.__name__ = 'x__get_parent_disk'


def x_force_unmount_disk__mutmut_orig(
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


def x_force_unmount_disk__mutmut_1(
	device: str,
	timeout_seconds: int = 11,
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


def x_force_unmount_disk__mutmut_2(
	device: str,
	timeout_seconds: int = 10,
	runner: CommandRunner | None = None,
) -> Tuple[bool, str]:
	"""
	Force unmount a disk image.
	Uses parent disk for more reliable unmounting.
	"""
	runner = None
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


def x_force_unmount_disk__mutmut_3(
	device: str,
	timeout_seconds: int = 10,
	runner: CommandRunner | None = None,
) -> Tuple[bool, str]:
	"""
	Force unmount a disk image.
	Uses parent disk for more reliable unmounting.
	"""
	runner = runner and get_default_runner()
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


def x_force_unmount_disk__mutmut_4(
	device: str,
	timeout_seconds: int = 10,
	runner: CommandRunner | None = None,
) -> Tuple[bool, str]:
	"""
	Force unmount a disk image.
	Uses parent disk for more reliable unmounting.
	"""
	runner = runner or get_default_runner()
	parent = None
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


def x_force_unmount_disk__mutmut_5(
	device: str,
	timeout_seconds: int = 10,
	runner: CommandRunner | None = None,
) -> Tuple[bool, str]:
	"""
	Force unmount a disk image.
	Uses parent disk for more reliable unmounting.
	"""
	runner = runner or get_default_runner()
	parent = _get_parent_disk(None)
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


def x_force_unmount_disk__mutmut_6(
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
	timeout = None

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


def x_force_unmount_disk__mutmut_7(
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
	timeout = max(None, int(timeout_seconds))

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


def x_force_unmount_disk__mutmut_8(
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
	timeout = max(1, None)

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


def x_force_unmount_disk__mutmut_9(
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
	timeout = max(int(timeout_seconds))

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


def x_force_unmount_disk__mutmut_10(
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
	timeout = max(1, )

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


def x_force_unmount_disk__mutmut_11(
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
	timeout = max(2, int(timeout_seconds))

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


def x_force_unmount_disk__mutmut_12(
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
	timeout = max(1, int(None))

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


def x_force_unmount_disk__mutmut_13(
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
		result = None
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


def x_force_unmount_disk__mutmut_14(
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
			None,
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


def x_force_unmount_disk__mutmut_15(
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
			timeout=None,
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


def x_force_unmount_disk__mutmut_16(
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


def x_force_unmount_disk__mutmut_17(
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


def x_force_unmount_disk__mutmut_18(
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
			["XXdiskutilXX", "unmountDisk", "force", parent],
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


def x_force_unmount_disk__mutmut_19(
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
			["DISKUTIL", "unmountDisk", "force", parent],
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


def x_force_unmount_disk__mutmut_20(
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
			["diskutil", "XXunmountDiskXX", "force", parent],
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


def x_force_unmount_disk__mutmut_21(
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
			["diskutil", "unmountdisk", "force", parent],
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


def x_force_unmount_disk__mutmut_22(
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
			["diskutil", "UNMOUNTDISK", "force", parent],
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


def x_force_unmount_disk__mutmut_23(
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
			["diskutil", "unmountDisk", "XXforceXX", parent],
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


def x_force_unmount_disk__mutmut_24(
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
			["diskutil", "unmountDisk", "FORCE", parent],
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


def x_force_unmount_disk__mutmut_25(
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
		if result.returncode != 0:
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


def x_force_unmount_disk__mutmut_26(
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
		if result.returncode == 1:
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


def x_force_unmount_disk__mutmut_27(
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
			return False, f"Unmounted {parent}"

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


def x_force_unmount_disk__mutmut_28(
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
		result = None
		if result.returncode == 0:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_29(
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
			None,
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


def x_force_unmount_disk__mutmut_30(
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
			timeout=None,
		)
		if result.returncode == 0:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_31(
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


def x_force_unmount_disk__mutmut_32(
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
			)
		if result.returncode == 0:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_33(
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
			["XXhdiutilXX", "detach", "-force", parent],
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


def x_force_unmount_disk__mutmut_34(
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
			["HDIUTIL", "detach", "-force", parent],
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


def x_force_unmount_disk__mutmut_35(
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
			["hdiutil", "XXdetachXX", "-force", parent],
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


def x_force_unmount_disk__mutmut_36(
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
			["hdiutil", "DETACH", "-force", parent],
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


def x_force_unmount_disk__mutmut_37(
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
			["hdiutil", "detach", "XX-forceXX", parent],
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


def x_force_unmount_disk__mutmut_38(
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
			["hdiutil", "detach", "-FORCE", parent],
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


def x_force_unmount_disk__mutmut_39(
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
		if result.returncode != 0:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_40(
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
		if result.returncode == 1:
			return True, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_41(
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
			return False, f"Detached {parent}"

		message = result.stderr.strip() or result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_42(
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

		message = None
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_43(
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

		message = result.stderr.strip() or result.stdout.strip() and f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_44(
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

		message = result.stderr.strip() and result.stdout.strip() or f"Failed to unmount {parent}"
		if "not mounted" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_45(
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
		if "XXnot mountedXX" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_46(
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
		if "NOT MOUNTED" in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_47(
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
		if "not mounted" not in message.lower():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_48(
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
		if "not mounted" in message.upper():
			return True, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_49(
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
			return False, f"{parent} already unmounted"
		return False, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_50(
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
		return True, message
	except Exception as exc:
		return False, f"Exception unmounting {parent}: {exc}"


def x_force_unmount_disk__mutmut_51(
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
		return True, f"Exception unmounting {parent}: {exc}"

x_force_unmount_disk__mutmut_mutants : ClassVar[MutantDict] = {
'x_force_unmount_disk__mutmut_1': x_force_unmount_disk__mutmut_1, 
    'x_force_unmount_disk__mutmut_2': x_force_unmount_disk__mutmut_2, 
    'x_force_unmount_disk__mutmut_3': x_force_unmount_disk__mutmut_3, 
    'x_force_unmount_disk__mutmut_4': x_force_unmount_disk__mutmut_4, 
    'x_force_unmount_disk__mutmut_5': x_force_unmount_disk__mutmut_5, 
    'x_force_unmount_disk__mutmut_6': x_force_unmount_disk__mutmut_6, 
    'x_force_unmount_disk__mutmut_7': x_force_unmount_disk__mutmut_7, 
    'x_force_unmount_disk__mutmut_8': x_force_unmount_disk__mutmut_8, 
    'x_force_unmount_disk__mutmut_9': x_force_unmount_disk__mutmut_9, 
    'x_force_unmount_disk__mutmut_10': x_force_unmount_disk__mutmut_10, 
    'x_force_unmount_disk__mutmut_11': x_force_unmount_disk__mutmut_11, 
    'x_force_unmount_disk__mutmut_12': x_force_unmount_disk__mutmut_12, 
    'x_force_unmount_disk__mutmut_13': x_force_unmount_disk__mutmut_13, 
    'x_force_unmount_disk__mutmut_14': x_force_unmount_disk__mutmut_14, 
    'x_force_unmount_disk__mutmut_15': x_force_unmount_disk__mutmut_15, 
    'x_force_unmount_disk__mutmut_16': x_force_unmount_disk__mutmut_16, 
    'x_force_unmount_disk__mutmut_17': x_force_unmount_disk__mutmut_17, 
    'x_force_unmount_disk__mutmut_18': x_force_unmount_disk__mutmut_18, 
    'x_force_unmount_disk__mutmut_19': x_force_unmount_disk__mutmut_19, 
    'x_force_unmount_disk__mutmut_20': x_force_unmount_disk__mutmut_20, 
    'x_force_unmount_disk__mutmut_21': x_force_unmount_disk__mutmut_21, 
    'x_force_unmount_disk__mutmut_22': x_force_unmount_disk__mutmut_22, 
    'x_force_unmount_disk__mutmut_23': x_force_unmount_disk__mutmut_23, 
    'x_force_unmount_disk__mutmut_24': x_force_unmount_disk__mutmut_24, 
    'x_force_unmount_disk__mutmut_25': x_force_unmount_disk__mutmut_25, 
    'x_force_unmount_disk__mutmut_26': x_force_unmount_disk__mutmut_26, 
    'x_force_unmount_disk__mutmut_27': x_force_unmount_disk__mutmut_27, 
    'x_force_unmount_disk__mutmut_28': x_force_unmount_disk__mutmut_28, 
    'x_force_unmount_disk__mutmut_29': x_force_unmount_disk__mutmut_29, 
    'x_force_unmount_disk__mutmut_30': x_force_unmount_disk__mutmut_30, 
    'x_force_unmount_disk__mutmut_31': x_force_unmount_disk__mutmut_31, 
    'x_force_unmount_disk__mutmut_32': x_force_unmount_disk__mutmut_32, 
    'x_force_unmount_disk__mutmut_33': x_force_unmount_disk__mutmut_33, 
    'x_force_unmount_disk__mutmut_34': x_force_unmount_disk__mutmut_34, 
    'x_force_unmount_disk__mutmut_35': x_force_unmount_disk__mutmut_35, 
    'x_force_unmount_disk__mutmut_36': x_force_unmount_disk__mutmut_36, 
    'x_force_unmount_disk__mutmut_37': x_force_unmount_disk__mutmut_37, 
    'x_force_unmount_disk__mutmut_38': x_force_unmount_disk__mutmut_38, 
    'x_force_unmount_disk__mutmut_39': x_force_unmount_disk__mutmut_39, 
    'x_force_unmount_disk__mutmut_40': x_force_unmount_disk__mutmut_40, 
    'x_force_unmount_disk__mutmut_41': x_force_unmount_disk__mutmut_41, 
    'x_force_unmount_disk__mutmut_42': x_force_unmount_disk__mutmut_42, 
    'x_force_unmount_disk__mutmut_43': x_force_unmount_disk__mutmut_43, 
    'x_force_unmount_disk__mutmut_44': x_force_unmount_disk__mutmut_44, 
    'x_force_unmount_disk__mutmut_45': x_force_unmount_disk__mutmut_45, 
    'x_force_unmount_disk__mutmut_46': x_force_unmount_disk__mutmut_46, 
    'x_force_unmount_disk__mutmut_47': x_force_unmount_disk__mutmut_47, 
    'x_force_unmount_disk__mutmut_48': x_force_unmount_disk__mutmut_48, 
    'x_force_unmount_disk__mutmut_49': x_force_unmount_disk__mutmut_49, 
    'x_force_unmount_disk__mutmut_50': x_force_unmount_disk__mutmut_50, 
    'x_force_unmount_disk__mutmut_51': x_force_unmount_disk__mutmut_51
}

def force_unmount_disk(*args, **kwargs):
	result = _mutmut_trampoline(x_force_unmount_disk__mutmut_orig, x_force_unmount_disk__mutmut_mutants, args, kwargs)
	return result 

force_unmount_disk.__signature__ = _mutmut_signature(x_force_unmount_disk__mutmut_orig)
x_force_unmount_disk__mutmut_orig.__name__ = 'x_force_unmount_disk'


def x_eject_disk__mutmut_orig(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(device, timeout_seconds=timeout_seconds)


def x_eject_disk__mutmut_1(device: str, timeout_seconds: int = 11) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(device, timeout_seconds=timeout_seconds)


def x_eject_disk__mutmut_2(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(None, timeout_seconds=timeout_seconds)


def x_eject_disk__mutmut_3(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(device, timeout_seconds=None)


def x_eject_disk__mutmut_4(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(timeout_seconds=timeout_seconds)


def x_eject_disk__mutmut_5(device: str, timeout_seconds: int = 10) -> Tuple[bool, str]:
	"""
	Eject a disk (alias for force_unmount_disk).

	Args:
		device: Device path (e.g., "/dev/disk7s1").
		timeout_seconds: Timeout for unmount operation.

	Returns:
		Tuple of (success, message).
	"""
	return force_unmount_disk(device, )

x_eject_disk__mutmut_mutants : ClassVar[MutantDict] = {
'x_eject_disk__mutmut_1': x_eject_disk__mutmut_1, 
    'x_eject_disk__mutmut_2': x_eject_disk__mutmut_2, 
    'x_eject_disk__mutmut_3': x_eject_disk__mutmut_3, 
    'x_eject_disk__mutmut_4': x_eject_disk__mutmut_4, 
    'x_eject_disk__mutmut_5': x_eject_disk__mutmut_5
}

def eject_disk(*args, **kwargs):
	result = _mutmut_trampoline(x_eject_disk__mutmut_orig, x_eject_disk__mutmut_mutants, args, kwargs)
	return result 

eject_disk.__signature__ = _mutmut_signature(x_eject_disk__mutmut_orig)
x_eject_disk__mutmut_orig.__name__ = 'x_eject_disk'
