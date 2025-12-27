"""
Developer Tools availability checks.

This module validates that Xcode and simctl are properly configured before
attempting cleanup operations. Without simctl, the tool cannot permanently
delete runtimes - it can only temporarily unmount disk images.

Common issue: xcode-select points to /Library/Developer/CommandLineTools
instead of /Applications/Xcode.app/Contents/Developer. This causes
"xcrun: error: unable to find utility 'simctl'" errors.

Fix: sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
"""
import os
from typing import Mapping, Tuple, Optional

from xcodecleaner.core.runner import CommandRunner, get_default_runner

DEFAULT_XCODE_DEVELOPER_DIR = "/Applications/Xcode.app/Contents/Developer"
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


def x_get_xcode_select_path__mutmut_orig(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_1(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = None
		result = runner.run(["xcode-select", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_2(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner and get_default_runner()
		result = runner.run(["xcode-select", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_3(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = None
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_4(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(None)
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_5(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["XXxcode-selectXX", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_6(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["XCODE-SELECT", "-p"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_7(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "XX-pXX"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_8(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "-P"])
		if result.returncode == 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_9(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "-p"])
		if result.returncode != 0:
			return result.stdout.strip()
		return None
	except Exception:
		return None


def x_get_xcode_select_path__mutmut_10(runner: CommandRunner | None = None) -> Optional[str]:
	"""Get the current xcode-select path."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcode-select", "-p"])
		if result.returncode == 1:
			return result.stdout.strip()
		return None
	except Exception:
		return None

x_get_xcode_select_path__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_xcode_select_path__mutmut_1': x_get_xcode_select_path__mutmut_1, 
    'x_get_xcode_select_path__mutmut_2': x_get_xcode_select_path__mutmut_2, 
    'x_get_xcode_select_path__mutmut_3': x_get_xcode_select_path__mutmut_3, 
    'x_get_xcode_select_path__mutmut_4': x_get_xcode_select_path__mutmut_4, 
    'x_get_xcode_select_path__mutmut_5': x_get_xcode_select_path__mutmut_5, 
    'x_get_xcode_select_path__mutmut_6': x_get_xcode_select_path__mutmut_6, 
    'x_get_xcode_select_path__mutmut_7': x_get_xcode_select_path__mutmut_7, 
    'x_get_xcode_select_path__mutmut_8': x_get_xcode_select_path__mutmut_8, 
    'x_get_xcode_select_path__mutmut_9': x_get_xcode_select_path__mutmut_9, 
    'x_get_xcode_select_path__mutmut_10': x_get_xcode_select_path__mutmut_10
}

def get_xcode_select_path(*args, **kwargs):
	result = _mutmut_trampoline(x_get_xcode_select_path__mutmut_orig, x_get_xcode_select_path__mutmut_mutants, args, kwargs)
	return result 

get_xcode_select_path.__signature__ = _mutmut_signature(x_get_xcode_select_path__mutmut_orig)
x_get_xcode_select_path__mutmut_orig.__name__ = 'x_get_xcode_select_path'


def x_is_simctl_available__mutmut_orig(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_1(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = None
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_2(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner and get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_3(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = None
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_4(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(None, timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_5(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=None, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_6(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=None)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_7(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_8(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_9(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, )
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_10(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["XXxcrunXX", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_11(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["XCRUN", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_12(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "XXsimctlXX", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_13(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "SIMCTL", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_14(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "XXlistXX"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_15(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "LIST"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_16(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=11, env=env)
		return result.returncode == 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_17(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode != 0
	except Exception:
		return False


def x_is_simctl_available__mutmut_18(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 1
	except Exception:
		return False


def x_is_simctl_available__mutmut_19(
	runner: CommandRunner | None = None,
	env: Mapping[str, str] | None = None,
) -> bool:
	"""Check if xcrun simctl is available and working."""
	try:
		runner = runner or get_default_runner()
		result = runner.run(["xcrun", "simctl", "list"], timeout=10, env=env)
		return result.returncode == 0
	except Exception:
		return True

x_is_simctl_available__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_simctl_available__mutmut_1': x_is_simctl_available__mutmut_1, 
    'x_is_simctl_available__mutmut_2': x_is_simctl_available__mutmut_2, 
    'x_is_simctl_available__mutmut_3': x_is_simctl_available__mutmut_3, 
    'x_is_simctl_available__mutmut_4': x_is_simctl_available__mutmut_4, 
    'x_is_simctl_available__mutmut_5': x_is_simctl_available__mutmut_5, 
    'x_is_simctl_available__mutmut_6': x_is_simctl_available__mutmut_6, 
    'x_is_simctl_available__mutmut_7': x_is_simctl_available__mutmut_7, 
    'x_is_simctl_available__mutmut_8': x_is_simctl_available__mutmut_8, 
    'x_is_simctl_available__mutmut_9': x_is_simctl_available__mutmut_9, 
    'x_is_simctl_available__mutmut_10': x_is_simctl_available__mutmut_10, 
    'x_is_simctl_available__mutmut_11': x_is_simctl_available__mutmut_11, 
    'x_is_simctl_available__mutmut_12': x_is_simctl_available__mutmut_12, 
    'x_is_simctl_available__mutmut_13': x_is_simctl_available__mutmut_13, 
    'x_is_simctl_available__mutmut_14': x_is_simctl_available__mutmut_14, 
    'x_is_simctl_available__mutmut_15': x_is_simctl_available__mutmut_15, 
    'x_is_simctl_available__mutmut_16': x_is_simctl_available__mutmut_16, 
    'x_is_simctl_available__mutmut_17': x_is_simctl_available__mutmut_17, 
    'x_is_simctl_available__mutmut_18': x_is_simctl_available__mutmut_18, 
    'x_is_simctl_available__mutmut_19': x_is_simctl_available__mutmut_19
}

def is_simctl_available(*args, **kwargs):
	result = _mutmut_trampoline(x_is_simctl_available__mutmut_orig, x_is_simctl_available__mutmut_mutants, args, kwargs)
	return result 

is_simctl_available.__signature__ = _mutmut_signature(x_is_simctl_available__mutmut_orig)
x_is_simctl_available__mutmut_orig.__name__ = 'x_is_simctl_available'


def x_is_xcode_path__mutmut_orig(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "Xcode.app" in path


def x_is_xcode_path__mutmut_1(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = None
	if path is None:
		return False
	return "Xcode.app" in path


def x_is_xcode_path__mutmut_2(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=None)
	if path is None:
		return False
	return "Xcode.app" in path


def x_is_xcode_path__mutmut_3(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is not None:
		return False
	return "Xcode.app" in path


def x_is_xcode_path__mutmut_4(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return True
	return "Xcode.app" in path


def x_is_xcode_path__mutmut_5(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "XXXcode.appXX" in path


def x_is_xcode_path__mutmut_6(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "xcode.app" in path


def x_is_xcode_path__mutmut_7(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "XCODE.APP" in path


def x_is_xcode_path__mutmut_8(runner: CommandRunner | None = None) -> bool:
	"""Check if xcode-select points to Xcode.app (not CommandLineTools)."""
	path = get_xcode_select_path(runner=runner)
	if path is None:
		return False
	return "Xcode.app" not in path

x_is_xcode_path__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_xcode_path__mutmut_1': x_is_xcode_path__mutmut_1, 
    'x_is_xcode_path__mutmut_2': x_is_xcode_path__mutmut_2, 
    'x_is_xcode_path__mutmut_3': x_is_xcode_path__mutmut_3, 
    'x_is_xcode_path__mutmut_4': x_is_xcode_path__mutmut_4, 
    'x_is_xcode_path__mutmut_5': x_is_xcode_path__mutmut_5, 
    'x_is_xcode_path__mutmut_6': x_is_xcode_path__mutmut_6, 
    'x_is_xcode_path__mutmut_7': x_is_xcode_path__mutmut_7, 
    'x_is_xcode_path__mutmut_8': x_is_xcode_path__mutmut_8
}

def is_xcode_path(*args, **kwargs):
	result = _mutmut_trampoline(x_is_xcode_path__mutmut_orig, x_is_xcode_path__mutmut_mutants, args, kwargs)
	return result 

is_xcode_path.__signature__ = _mutmut_signature(x_is_xcode_path__mutmut_orig)
x_is_xcode_path__mutmut_orig.__name__ = 'x_is_xcode_path'


def x_get_simctl_env__mutmut_orig(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_1(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = None
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_2(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get(None)
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_3(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("XXDEVELOPER_DIRXX")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_4(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("developer_dir")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_5(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir or os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_6(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(None):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_7(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"XXDEVELOPER_DIRXX": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_8(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"developer_dir": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_9(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = None
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_10(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=None)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_11(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path or "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_12(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "XXXcode.appXX" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_13(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_14(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "XCODE.APP" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_15(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" not in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_16(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(None):
		return {"DEVELOPER_DIR": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_17(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"XXDEVELOPER_DIRXX": DEFAULT_XCODE_DEVELOPER_DIR}

	return None


def x_get_simctl_env__mutmut_18(runner: CommandRunner | None = None) -> Optional[dict[str, str]]:
	"""
	Get an environment override for simctl when xcode-select points to CLT.

	Returns a dict with DEVELOPER_DIR if Xcode exists and is needed; otherwise None.
	"""
	env_dir = os.environ.get("DEVELOPER_DIR")
	if env_dir and os.path.isdir(env_dir):
		return {"DEVELOPER_DIR": env_dir}

	xcode_path = get_xcode_select_path(runner=runner)
	if xcode_path and "Xcode.app" in xcode_path:
		return None

	if os.path.isdir(DEFAULT_XCODE_DEVELOPER_DIR):
		return {"developer_dir": DEFAULT_XCODE_DEVELOPER_DIR}

	return None

x_get_simctl_env__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_simctl_env__mutmut_1': x_get_simctl_env__mutmut_1, 
    'x_get_simctl_env__mutmut_2': x_get_simctl_env__mutmut_2, 
    'x_get_simctl_env__mutmut_3': x_get_simctl_env__mutmut_3, 
    'x_get_simctl_env__mutmut_4': x_get_simctl_env__mutmut_4, 
    'x_get_simctl_env__mutmut_5': x_get_simctl_env__mutmut_5, 
    'x_get_simctl_env__mutmut_6': x_get_simctl_env__mutmut_6, 
    'x_get_simctl_env__mutmut_7': x_get_simctl_env__mutmut_7, 
    'x_get_simctl_env__mutmut_8': x_get_simctl_env__mutmut_8, 
    'x_get_simctl_env__mutmut_9': x_get_simctl_env__mutmut_9, 
    'x_get_simctl_env__mutmut_10': x_get_simctl_env__mutmut_10, 
    'x_get_simctl_env__mutmut_11': x_get_simctl_env__mutmut_11, 
    'x_get_simctl_env__mutmut_12': x_get_simctl_env__mutmut_12, 
    'x_get_simctl_env__mutmut_13': x_get_simctl_env__mutmut_13, 
    'x_get_simctl_env__mutmut_14': x_get_simctl_env__mutmut_14, 
    'x_get_simctl_env__mutmut_15': x_get_simctl_env__mutmut_15, 
    'x_get_simctl_env__mutmut_16': x_get_simctl_env__mutmut_16, 
    'x_get_simctl_env__mutmut_17': x_get_simctl_env__mutmut_17, 
    'x_get_simctl_env__mutmut_18': x_get_simctl_env__mutmut_18
}

def get_simctl_env(*args, **kwargs):
	result = _mutmut_trampoline(x_get_simctl_env__mutmut_orig, x_get_simctl_env__mutmut_mutants, args, kwargs)
	return result 

get_simctl_env.__signature__ = _mutmut_signature(x_get_simctl_env__mutmut_orig)
x_get_simctl_env__mutmut_orig.__name__ = 'x_get_simctl_env'


def x_check_devtools__mutmut_orig(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_1(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = None

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_2(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=None)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_3(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is not None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_4(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return True, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_5(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"XXXcode Command Line Tools not found.\n\nXX"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_6(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"xcode command line tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_7(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"XCODE COMMAND LINE TOOLS NOT FOUND.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_8(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"XXInstall Xcode from the App Store, then run:\nXX"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_9(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"install xcode from the app store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_10(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"INSTALL XCODE FROM THE APP STORE, THEN RUN:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_11(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"XXsudo xcode-select --switch /Applications/Xcode.app/Contents/DeveloperXX"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_12(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /applications/xcode.app/contents/developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_13(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"SUDO XCODE-SELECT --SWITCH /APPLICATIONS/XCODE.APP/CONTENTS/DEVELOPER"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_14(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "XXCommandLineToolsXX" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_15(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "commandlinetools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_16(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "COMMANDLINETOOLS" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_17(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" not in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_18(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = None
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_19(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=None)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_20(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env or is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_21(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=None, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_22(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=None):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_23(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_24(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, ):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_25(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return False, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_26(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['XXDEVELOPER_DIRXX']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_27(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['developer_dir']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_28(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"XXfor simctl via DEVELOPER_DIR override.XX"
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_29(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via developer_dir override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_30(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"FOR SIMCTL VIA DEVELOPER_DIR OVERRIDE."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_31(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return True, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_32(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"XXSimulator management requires full Xcode.\n\nXX"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_33(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"simulator management requires full xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_34(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"SIMULATOR MANAGEMENT REQUIRES FULL XCODE.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_35(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"XXFix with:\nXX"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_36(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_37(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"FIX WITH:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_38(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"XXsudo xcode-select --switch /Applications/Xcode.app/Contents/DeveloperXX"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_39(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /applications/xcode.app/contents/developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_40(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"SUDO XCODE-SELECT --SWITCH /APPLICATIONS/XCODE.APP/CONTENTS/DEVELOPER"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_41(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_42(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=None):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_43(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return True, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_44(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"XXTry:\nXX"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_45(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_46(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"TRY:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_47(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"XXsudo xcode-select --switch /Applications/Xcode.app/Contents/DeveloperXX"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_48(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /applications/xcode.app/contents/developer"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_49(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"SUDO XCODE-SELECT --SWITCH /APPLICATIONS/XCODE.APP/CONTENTS/DEVELOPER"
		)

	return True, "Developer tools configured correctly"


def x_check_devtools__mutmut_50(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return False, "Developer tools configured correctly"


def x_check_devtools__mutmut_51(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "XXDeveloper tools configured correctlyXX"


def x_check_devtools__mutmut_52(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "developer tools configured correctly"


def x_check_devtools__mutmut_53(runner: CommandRunner | None = None) -> Tuple[bool, str]:
	"""
	Check if developer tools are properly configured for simulator management.

	Returns:
		(ok, message) - ok is True if simctl is available, message explains status
	"""
	xcode_path = get_xcode_select_path(runner=runner)

	if xcode_path is None:
		return False, (
			"Xcode Command Line Tools not found.\n\n"
			"Install Xcode from the App Store, then run:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if "CommandLineTools" in xcode_path:
		env = get_simctl_env(runner=runner)
		if env and is_simctl_available(runner=runner, env=env):
			return True, (
				f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
				f"Using Xcode at:\n{env['DEVELOPER_DIR']}\n"
				"for simctl via DEVELOPER_DIR override."
			)
		return False, (
			f"xcode-select points to CommandLineTools:\n{xcode_path}\n\n"
			"Simulator management requires full Xcode.\n\n"
			"Fix with:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	if not is_simctl_available(runner=runner):
		return False, (
			f"xcrun simctl not working.\n"
			f"Current path: {xcode_path}\n\n"
			"Try:\n"
			"sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"
		)

	return True, "DEVELOPER TOOLS CONFIGURED CORRECTLY"

x_check_devtools__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_devtools__mutmut_1': x_check_devtools__mutmut_1, 
    'x_check_devtools__mutmut_2': x_check_devtools__mutmut_2, 
    'x_check_devtools__mutmut_3': x_check_devtools__mutmut_3, 
    'x_check_devtools__mutmut_4': x_check_devtools__mutmut_4, 
    'x_check_devtools__mutmut_5': x_check_devtools__mutmut_5, 
    'x_check_devtools__mutmut_6': x_check_devtools__mutmut_6, 
    'x_check_devtools__mutmut_7': x_check_devtools__mutmut_7, 
    'x_check_devtools__mutmut_8': x_check_devtools__mutmut_8, 
    'x_check_devtools__mutmut_9': x_check_devtools__mutmut_9, 
    'x_check_devtools__mutmut_10': x_check_devtools__mutmut_10, 
    'x_check_devtools__mutmut_11': x_check_devtools__mutmut_11, 
    'x_check_devtools__mutmut_12': x_check_devtools__mutmut_12, 
    'x_check_devtools__mutmut_13': x_check_devtools__mutmut_13, 
    'x_check_devtools__mutmut_14': x_check_devtools__mutmut_14, 
    'x_check_devtools__mutmut_15': x_check_devtools__mutmut_15, 
    'x_check_devtools__mutmut_16': x_check_devtools__mutmut_16, 
    'x_check_devtools__mutmut_17': x_check_devtools__mutmut_17, 
    'x_check_devtools__mutmut_18': x_check_devtools__mutmut_18, 
    'x_check_devtools__mutmut_19': x_check_devtools__mutmut_19, 
    'x_check_devtools__mutmut_20': x_check_devtools__mutmut_20, 
    'x_check_devtools__mutmut_21': x_check_devtools__mutmut_21, 
    'x_check_devtools__mutmut_22': x_check_devtools__mutmut_22, 
    'x_check_devtools__mutmut_23': x_check_devtools__mutmut_23, 
    'x_check_devtools__mutmut_24': x_check_devtools__mutmut_24, 
    'x_check_devtools__mutmut_25': x_check_devtools__mutmut_25, 
    'x_check_devtools__mutmut_26': x_check_devtools__mutmut_26, 
    'x_check_devtools__mutmut_27': x_check_devtools__mutmut_27, 
    'x_check_devtools__mutmut_28': x_check_devtools__mutmut_28, 
    'x_check_devtools__mutmut_29': x_check_devtools__mutmut_29, 
    'x_check_devtools__mutmut_30': x_check_devtools__mutmut_30, 
    'x_check_devtools__mutmut_31': x_check_devtools__mutmut_31, 
    'x_check_devtools__mutmut_32': x_check_devtools__mutmut_32, 
    'x_check_devtools__mutmut_33': x_check_devtools__mutmut_33, 
    'x_check_devtools__mutmut_34': x_check_devtools__mutmut_34, 
    'x_check_devtools__mutmut_35': x_check_devtools__mutmut_35, 
    'x_check_devtools__mutmut_36': x_check_devtools__mutmut_36, 
    'x_check_devtools__mutmut_37': x_check_devtools__mutmut_37, 
    'x_check_devtools__mutmut_38': x_check_devtools__mutmut_38, 
    'x_check_devtools__mutmut_39': x_check_devtools__mutmut_39, 
    'x_check_devtools__mutmut_40': x_check_devtools__mutmut_40, 
    'x_check_devtools__mutmut_41': x_check_devtools__mutmut_41, 
    'x_check_devtools__mutmut_42': x_check_devtools__mutmut_42, 
    'x_check_devtools__mutmut_43': x_check_devtools__mutmut_43, 
    'x_check_devtools__mutmut_44': x_check_devtools__mutmut_44, 
    'x_check_devtools__mutmut_45': x_check_devtools__mutmut_45, 
    'x_check_devtools__mutmut_46': x_check_devtools__mutmut_46, 
    'x_check_devtools__mutmut_47': x_check_devtools__mutmut_47, 
    'x_check_devtools__mutmut_48': x_check_devtools__mutmut_48, 
    'x_check_devtools__mutmut_49': x_check_devtools__mutmut_49, 
    'x_check_devtools__mutmut_50': x_check_devtools__mutmut_50, 
    'x_check_devtools__mutmut_51': x_check_devtools__mutmut_51, 
    'x_check_devtools__mutmut_52': x_check_devtools__mutmut_52, 
    'x_check_devtools__mutmut_53': x_check_devtools__mutmut_53
}

def check_devtools(*args, **kwargs):
	result = _mutmut_trampoline(x_check_devtools__mutmut_orig, x_check_devtools__mutmut_mutants, args, kwargs)
	return result 

check_devtools.__signature__ = _mutmut_signature(x_check_devtools__mutmut_orig)
x_check_devtools__mutmut_orig.__name__ = 'x_check_devtools'


def x_get_fix_command__mutmut_orig() -> str:
	"""Get the terminal command to fix xcode-select."""
	return "sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer"


def x_get_fix_command__mutmut_1() -> str:
	"""Get the terminal command to fix xcode-select."""
	return "XXsudo xcode-select --switch /Applications/Xcode.app/Contents/DeveloperXX"


def x_get_fix_command__mutmut_2() -> str:
	"""Get the terminal command to fix xcode-select."""
	return "sudo xcode-select --switch /applications/xcode.app/contents/developer"


def x_get_fix_command__mutmut_3() -> str:
	"""Get the terminal command to fix xcode-select."""
	return "SUDO XCODE-SELECT --SWITCH /APPLICATIONS/XCODE.APP/CONTENTS/DEVELOPER"

x_get_fix_command__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_fix_command__mutmut_1': x_get_fix_command__mutmut_1, 
    'x_get_fix_command__mutmut_2': x_get_fix_command__mutmut_2, 
    'x_get_fix_command__mutmut_3': x_get_fix_command__mutmut_3
}

def get_fix_command(*args, **kwargs):
	result = _mutmut_trampoline(x_get_fix_command__mutmut_orig, x_get_fix_command__mutmut_mutants, args, kwargs)
	return result 

get_fix_command.__signature__ = _mutmut_signature(x_get_fix_command__mutmut_orig)
x_get_fix_command__mutmut_orig.__name__ = 'x_get_fix_command'
