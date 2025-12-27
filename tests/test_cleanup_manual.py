import os

from xcodecleaner.services import cleanup


def test_manual_cleanup_removes_selected_paths(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.manual_cleanup(
		delete_core_simulator=True,
		delete_derived_data=False,
		delete_archives=True,
		delete_caches=True,
		delete_device_support=True,
		stop_processes=False,
		measure_space=False,
	)
	assert result.commands_ok is True

	expected = [
		os.path.expanduser("~/Library/Developer/CoreSimulator"),
		os.path.expanduser("~/Library/Developer/Xcode/Archives"),
		os.path.expanduser("~/Library/Developer/Xcode/iOS DeviceSupport"),
		os.path.expanduser("~/Library/Caches/com.apple.dt.Xcode"),
		os.path.expanduser("~/Library/Caches/org.swift.swiftpm"),
	]
	calls = [call[2] for call in runner.calls]
	for path in expected:
		assert ("rm", "-rf", path) in calls

	derived_path = os.path.expanduser("~/Library/Developer/Xcode/DerivedData")
	assert ("rm", "-rf", derived_path) not in calls


def test_manual_cleanup_no_paths_does_not_rm(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		stop_processes=False,
		measure_space=False,
	)
	assert result.commands_ok is True
	assert runner.calls == []


def test_manual_cleanup_measure_space_false_skips_diskutil(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		stop_processes=False,
		measure_space=False,
	)
	assert not any(call[2][:3] == ("diskutil", "apfs", "list") for call in runner.calls)


def test_manual_cleanup_space_delta_positive(make_runner, fixture_bytes, monkeypatch):
	before = fixture_bytes("diskutil_apfs_list_before.txt")
	after = fixture_bytes("diskutil_apfs_list_after.txt")
	runner = make_runner({
		(False, False, ("diskutil", "apfs", "list", "-plist")): [
			(0, before, b""),
			(0, after, b""),
		],
	})
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		stop_processes=False,
	)
	assert result.space_ok is True


def test_manual_cleanup_stop_processes_runs_launchctl(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		stop_processes=True,
		measure_space=False,
	)
	user_scope = f"gui/{cleanup.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = [call[2] for call in runner.calls]
	assert ("launchctl", "bootout", user_scope) in commands


def test_manual_cleanup_defaults_stop_processes(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		measure_space=False,
	)
	user_scope = f"gui/{cleanup.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = [call[2] for call in runner.calls]
	assert ("launchctl", "bootout", user_scope) in commands


def test_manual_cleanup_defaults_measure_space(make_runner, fixture_bytes, monkeypatch):
	before = fixture_bytes("diskutil_apfs_list_before.txt")
	after = fixture_bytes("diskutil_apfs_list_after.txt")
	runner = make_runner({
		(False, False, ("diskutil", "apfs", "list", "-plist")): [
			(0, before, b""),
			(0, after, b""),
		],
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.manual_cleanup(
		delete_core_simulator=False,
		delete_derived_data=False,
		delete_archives=False,
		delete_caches=False,
		delete_device_support=False,
		stop_processes=False,
	)
	assert any(call[2][:3] == ("diskutil", "apfs", "list") for call in runner.calls)
