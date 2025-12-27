from xcodefuckoff.services import cleanup


def test_delete_all_runtimes_calls_delete_all_and_specific(make_runner, fixture_text):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_all_runtimes()
	assert result.commands_ok is True
	commands = [call[2] for call in runner.calls]
	assert ("xcrun", "simctl", "runtime", "delete", "all") in commands
	assert ("xcrun", "simctl", "runtime", "delete", runtime_id) in commands


def test_delete_all_runtimes_delete_all_optional(make_runner, fixture_text):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (1, "", "delete all failed"),
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_all_runtimes()
	assert result.commands_ok is True
	assert result.error is None


def test_delete_all_runtimes_list_error(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, "bad json", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_all_runtimes()
	assert result.commands_ok is False
	assert "Failed to parse simctl runtime list" in (result.error or "")


def test_delete_all_sim_devices_delete_failure(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "shutdown", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "delete", "all")): (1, "", "delete failed"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_all_sim_devices()
	assert result.commands_ok is False
	assert "delete failed" in (result.error or "")


def test_delete_unavailable_runtimes_success(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", "unavailable")): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_unavailable_runtimes()
	assert result.commands_ok is True
	assert result.error is None


def test_delete_unavailable_runtimes_failure(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", "unavailable")): (1, "", "fail"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_unavailable_runtimes()
	assert result.commands_ok is False
	assert "fail" in (result.error or "")


def test_remove_device_directories_and_profiles(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_device_directories_and_profiles()
	assert result.commands_ok is True
	commands = [call[2] for call in runner.calls]
	devices = cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")
	profiles = cleanup.os.path.expanduser("~/Library/Developer/CoreSimulator/Profiles")
	assert ("rm", "-rf", devices) in commands
	assert ("rm", "-rf", profiles) in commands


def test_disable_core_simulator_service_uses_sudo(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	result = service.disable_core_simulator_service()
	assert result.commands_ok is True
	assert result.error is None
	assert any(call[0] is True and call[2][0] == "/bin/sh" for call in runner.calls)
	command = next(call[2][2] for call in runner.calls if call[2][0] == "/bin/sh")
	assert "launchctl bootout" in command
	assert "launchctl disable" in command


def test_disable_core_simulator_service_reports_error(make_runner):
	runner = make_runner({}, default=(1, "", "permission denied"))
	service = cleanup.CleanupService(runner=runner)
	result = service.disable_core_simulator_service()
	assert result.commands_ok is False
	assert "permission denied" in (result.error or "")


def test_is_xcode_running_checks_simulator(make_runner):
	runner = make_runner({
		(False, True, ("pgrep", "-x", "Xcode")): (1, "", ""),
		(False, True, ("pgrep", "-x", "Simulator")): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	assert service.is_xcode_running() is True


def test_is_xcode_running_false_when_none(make_runner):
	runner = make_runner({
		(False, True, ("pgrep", "-x", "Xcode")): (1, "", ""),
		(False, True, ("pgrep", "-x", "Simulator")): (1, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	assert service.is_xcode_running() is False


def test_get_mounted_simulator_volumes_filters_lines(make_runner):
	output = (
		"/dev/disk7s1  GUID_partition_scheme\n"
		"/dev/disk7s1s1  Apple_APFS  /Library/Developer/CoreSimulator/Volumes/iOS_18.6\n"
		"/dev/disk8s1  Apple_APFS  /Volumes/Other\n"
		"disk image  /Library/Developer/CoreSimulator/Volumes/tvOS_18.0 Simulator\n"
	)
	runner = make_runner({
		(False, True, ("hdiutil", "info")): (0, output, ""),
	})
	service = cleanup.CleanupService(runner=runner)
	volumes = service.get_mounted_simulator_volumes()
	assert len(volumes) == 2
	assert all("CoreSimulator/Volumes" in line for line in volumes)


def test_nuclear_cleanup_uses_runtime_error(make_runner, monkeypatch):
	runner = make_runner({}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	fake_step = cleanup.StepResult(
		label="runtime cleanup",
		result=cleanup.CmdResult(tuple(), 1, "", "fail"),
		required=True,
	)

	def fake_remove(*args, **kwargs):
		return cleanup.ActionResult(commands_ok=False, steps=[fake_step], error="runtime error")

	monkeypatch.setattr(service, "remove_runtime_backing_files", fake_remove)
	result = service.nuclear_cleanup()
	assert result.error == "runtime error"
	assert any(step.label == "runtime cleanup" for step in result.steps)
