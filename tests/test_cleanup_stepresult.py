from xcodefuckoff.core.runner import CmdResult
from xcodefuckoff.services.cleanup import StepResult


def test_denied_marker_forces_failure():
	result = CmdResult(("rm", "-rf", "/Library/Developer/CoreSimulator/Cryptex"), 0, "", "Operation not permitted")
	step = StepResult(label="rm -rf Cryptex", result=result, required=True)
	assert step.ok is False


def test_timed_out_forces_failure():
	result = CmdResult(("xcrun", "simctl", "runtime", "list"), 124, "", "timeout", timed_out=True)
	step = StepResult(label="simctl runtime list", result=result, required=True)
	assert step.ok is False


def test_allow_not_mounted_passes_on_not_mounted():
	result = CmdResult(("diskutil", "unmountDisk", "force", "/dev/disk7"), 1, "", "not mounted")
	step = StepResult(label="unmount", result=result, required=True, allow_not_mounted=True)
	assert step.ok is True
