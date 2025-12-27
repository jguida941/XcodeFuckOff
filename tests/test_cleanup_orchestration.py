from xcodefuckoff.services import cleanup


def test_free_runtime_space_fails_if_simctl_missing(make_runner, fixture_bytes):
	before = fixture_bytes("diskutil_apfs_list_before.txt")
	after = fixture_bytes("diskutil_apfs_list_after.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "shutdown", "all")): (127, "", "xcrun: error"),
		(False, True, ("xcrun", "simctl", "delete", "unavailable")): (127, "", "xcrun: error"),
		(False, False, ("diskutil", "apfs", "list", "-plist")): [
			(0, before, b""),
			(0, after, b""),
		],
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.free_runtime_space(include_system_runtime_files=False, include_user_space=False)
	assert result.commands_ok is False
	assert result.error is not None
	assert "xcrun" in result.error.lower()


def test_free_runtime_space_user_space_deletes_paths(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.free_runtime_space(
		include_system_runtime_files=False,
		include_user_space=True,
		delete_devices=True,
		delete_derived_data=True,
		stop_processes=False,
		measure_space=False,
	)
	assert result.commands_ok is True
	calls = [call[2] for call in runner.calls]
	assert ("xcrun", "simctl", "shutdown", "all") in calls
	assert ("xcrun", "simctl", "delete", "unavailable") in calls
	assert ("rm", "-rf", cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")) in calls
	assert ("rm", "-rf", cleanup.os.path.expanduser("~/Library/Developer/Xcode/DerivedData")) in calls


def test_free_runtime_space_with_system_cleanup_calls_runtime_list(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list_empty.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.free_runtime_space(
		include_system_runtime_files=True,
		include_user_space=False,
		stop_processes=False,
		measure_space=False,
	)
	assert result.error is None
	assert any(call[2] == ("xcrun", "simctl", "runtime", "list", "-j") for call in runner.calls)
	assert any(call[0] is True and call[2][0] == "/bin/sh" for call in runner.calls)


def test_delete_unavailable_sim_devices_requires_shutdown(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "shutdown", "all")): (1, "", "shutdown fail"),
		(False, True, ("xcrun", "simctl", "delete", "unavailable")): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_unavailable_sim_devices()
	assert result.commands_ok is False
	assert "shutdown fail" in (result.error or "")


def test_free_runtime_space_no_process_kill_when_not_system(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.free_runtime_space(
		include_system_runtime_files=False,
		include_user_space=False,
		stop_processes=True,
		measure_space=False,
	)
	commands = [call[2] for call in runner.calls]
	assert not any(cmd[0] == "launchctl" for cmd in commands)


def test_free_runtime_space_include_user_space_defaults_do_not_delete(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.free_runtime_space(
		include_system_runtime_files=False,
		include_user_space=True,
		stop_processes=False,
		measure_space=False,
	)
	commands = [call[2] for call in runner.calls]
	assert ("rm", "-rf", cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")) not in commands
	assert ("rm", "-rf", cleanup.os.path.expanduser("~/Library/Developer/Xcode/DerivedData")) not in commands


def test_free_runtime_space_skips_runtime_cleanup_when_disabled(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	called = {"runtime": False}

	def fake_remove_runtime(*args, **kwargs):
		called["runtime"] = True
		return cleanup.ActionResult(commands_ok=True, steps=[], error=None)

	monkeypatch.setattr(service, "remove_runtime_backing_files", fake_remove_runtime)
	service.free_runtime_space(
		include_system_runtime_files=False,
		include_user_space=False,
		stop_processes=False,
		measure_space=False,
	)
	assert called["runtime"] is False


def test_free_runtime_space_measure_space_false_skips_diskutil(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.free_runtime_space(
		include_system_runtime_files=False,
		include_user_space=False,
		stop_processes=False,
		measure_space=False,
	)
	assert not any(call[2][:3] == ("diskutil", "apfs", "list") for call in runner.calls)


def test_free_runtime_space_runtime_error_propagates(make_runner, monkeypatch):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, "bad json", ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.free_runtime_space(
		include_system_runtime_files=True,
		include_user_space=False,
		stop_processes=False,
		measure_space=False,
	)
	assert result.error is not None
	assert "Failed to parse simctl runtime list" in result.error


def test_free_runtime_space_stop_processes_runs_launchctl(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list_empty.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	service.free_runtime_space(
		include_system_runtime_files=True,
		include_user_space=False,
		stop_processes=True,
		measure_space=False,
	)
	user_scope = f"gui/{cleanup.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = [call[2] for call in runner.calls]
	assert ("launchctl", "bootout", user_scope) in commands
