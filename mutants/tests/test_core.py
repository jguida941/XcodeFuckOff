from xcodecleaner.services import cleanup, disks, processes
from xcodecleaner.system import sip


def test_is_sip_enabled_enabled(make_runner):
	runner = make_runner({
		(False, True, ("csrutil", "status")): (0, "System Integrity Protection status: enabled.", ""),
	})
	assert sip.is_sip_enabled(runner=runner) is True


def test_force_unmount_disk_success(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk1")): (0, "", ""),
	}, default=(1, "", "fail"))
	ok, msg = disks.force_unmount_disk("/dev/disk1", runner=runner)
	assert ok is True
	assert "Unmounted" in msg


def test_clear_all_simulator_caches_calls(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	result = service.clear_all_simulator_caches()
	assert len(result.steps) >= 3
	assert all(step.result.returncode == 0 for step in result.steps)
	assert any("CoreSimulator/Caches" in call[2][2] for call in runner.calls)


def test_kill_all_includes_xcode(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	processes.kill_all_simulators_and_xcode(runner=runner)
	assert any(call[2] == ("pkill", "-9", "-x", "Xcode") for call in runner.calls)


def test_clear_paths_expands_home_and_sudo(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	result = service.clear_paths(["~/Library/TestPath"], sudo=True)
	assert result.commands_ok is True
	expanded = cleanup.os.path.expanduser("~/Library/TestPath")
	assert (True, True, ("rm", "-rf", expanded)) in runner.calls


def test_clear_all_simulator_caches_paths(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	service.clear_all_simulator_caches()
	calls = [call[2] for call in runner.calls]
	expected = [
		cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Caches"),
		cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Temp"),
		cleanup.os.path.expanduser("~/Library/Caches/com.apple.CoreSimulator"),
		cleanup.os.path.expanduser("~/Library/Developer/Xcode/DerivedData"),
	]
	for path in expected:
		assert ("rm", "-rf", path) in calls
