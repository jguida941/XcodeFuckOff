from typing import Optional

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


def x_is_sip_enabled__mutmut_orig(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_1(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = None
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_2(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner and get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_3(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = None
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_4(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(None)
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_5(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["XXcsrutilXX", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_6(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["CSRUTIL", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_7(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "XXstatusXX"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_8(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "STATUS"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_9(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = None
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_10(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().upper()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_11(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "XXenabledXX" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_12(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "ENABLED" in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_13(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" not in output:
			return True
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_14(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return False
		if "disabled" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_15(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "XXdisabledXX" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_16(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "DISABLED" in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_17(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" not in output:
			return False
		return None
	except Exception:
		return None


def x_is_sip_enabled__mutmut_18(runner: CommandRunner | None = None) -> Optional[bool]:
	try:
		runner = runner or get_default_runner()
		result = runner.run(["csrutil", "status"])
		output = result.stdout.strip().lower()
		if "enabled" in output:
			return True
		if "disabled" in output:
			return True
		return None
	except Exception:
		return None

x_is_sip_enabled__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_sip_enabled__mutmut_1': x_is_sip_enabled__mutmut_1, 
    'x_is_sip_enabled__mutmut_2': x_is_sip_enabled__mutmut_2, 
    'x_is_sip_enabled__mutmut_3': x_is_sip_enabled__mutmut_3, 
    'x_is_sip_enabled__mutmut_4': x_is_sip_enabled__mutmut_4, 
    'x_is_sip_enabled__mutmut_5': x_is_sip_enabled__mutmut_5, 
    'x_is_sip_enabled__mutmut_6': x_is_sip_enabled__mutmut_6, 
    'x_is_sip_enabled__mutmut_7': x_is_sip_enabled__mutmut_7, 
    'x_is_sip_enabled__mutmut_8': x_is_sip_enabled__mutmut_8, 
    'x_is_sip_enabled__mutmut_9': x_is_sip_enabled__mutmut_9, 
    'x_is_sip_enabled__mutmut_10': x_is_sip_enabled__mutmut_10, 
    'x_is_sip_enabled__mutmut_11': x_is_sip_enabled__mutmut_11, 
    'x_is_sip_enabled__mutmut_12': x_is_sip_enabled__mutmut_12, 
    'x_is_sip_enabled__mutmut_13': x_is_sip_enabled__mutmut_13, 
    'x_is_sip_enabled__mutmut_14': x_is_sip_enabled__mutmut_14, 
    'x_is_sip_enabled__mutmut_15': x_is_sip_enabled__mutmut_15, 
    'x_is_sip_enabled__mutmut_16': x_is_sip_enabled__mutmut_16, 
    'x_is_sip_enabled__mutmut_17': x_is_sip_enabled__mutmut_17, 
    'x_is_sip_enabled__mutmut_18': x_is_sip_enabled__mutmut_18
}

def is_sip_enabled(*args, **kwargs):
	result = _mutmut_trampoline(x_is_sip_enabled__mutmut_orig, x_is_sip_enabled__mutmut_mutants, args, kwargs)
	return result 

is_sip_enabled.__signature__ = _mutmut_signature(x_is_sip_enabled__mutmut_orig)
x_is_sip_enabled__mutmut_orig.__name__ = 'x_is_sip_enabled'

