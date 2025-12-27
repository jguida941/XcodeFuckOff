import json

from xcodefuckoff.services import cleanup


def test_delete_runtimes_calls_simctl_runtime_delete(make_runner):
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.delete_runtimes([runtime_id])
	assert result.commands_ok is True
	assert runner.calls == [
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)),
	]


def test_list_runtimes_passes_simctl_env(make_runner):
	env = {"DEVELOPER_DIR": "/Applications/Xcode.app/Contents/Developer"}
	env_key = (("DEVELOPER_DIR", env["DEVELOPER_DIR"]),)
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j"), env_key): (0, "{}", ""),
	})
	service = cleanup.CleanupService(runner=runner, simctl_env=env)
	runtimes, step, error = service.list_runtimes()
	assert error is None
	assert runtimes == []
	assert runner.calls == [
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j"), env_key),
	]


def test_remove_runtime_backing_files_fails_if_runtime_still_registered(make_runner, fixture_text):
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, runtime_list, ""),
			(0, runtime_list, ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert "Runtime still registered" in (result.error or "")


def test_parse_simctl_runtime_list_dict_mapping():
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	payload = {
		runtime_id: {
			"name": "iOS 18.6",
			"version": "18.6",
			"build": "22A123",
			"state": "Ready",
			"sizeBytes": 123,
		}
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier == runtime_id
	assert runtimes[0].size_bytes == 123


def test_parse_simctl_runtime_list_runtimes_array():
	payload = {
		"runtimes": [
			{
				"identifier": "com.apple.CoreSimulator.SimRuntime.iOS-17-4",
				"name": "iOS 17.4",
				"version": "17.4",
				"build": "21A123",
				"state": "Ready",
				"sizeBytes": 321,
			},
			{"name": "missing-id"},
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier == "com.apple.CoreSimulator.SimRuntime.iOS-17-4"
	assert runtimes[0].size_bytes == 321


def test_parse_simctl_runtime_list_runtimes_key_variants():
	payload = {
		"Runtimes": [
			{
				"id": "com.apple.CoreSimulator.SimRuntime.iOS-16-0",
				"name": "iOS 16.0",
				"version": "16.0",
				"buildversion": "20A123",
				"bundleSize": 999,
			}
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier == "com.apple.CoreSimulator.SimRuntime.iOS-16-0"
	assert runtimes[0].build == "20A123"
	assert runtimes[0].size_bytes == 999


def test_parse_simctl_runtime_list_mapping_identifier_override():
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	payload = {
		runtime_id: {
			"identifier": "override.identifier",
			"name": "iOS 18.6",
			"version": "18.6",
		}
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier == "override.identifier"
	assert runtimes[0].version == "18.6"


def test_parse_simctl_runtime_list_payload_list():
	payload = [
		{
			"identifier": "com.apple.CoreSimulator.SimRuntime.tvOS-17-0",
			"name": "tvOS 17.0",
			"sizeBytes": 10,
		},
		"junk",
	]
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier.endswith("tvOS-17-0")


def test_parse_simctl_runtime_list_continues_after_missing_identifier():
	payload = {
		"runtimes": [
			{"identifier": "", "name": "Missing"},
			{"identifier": "com.apple.CoreSimulator.SimRuntime.iOS-17-0", "name": "iOS 17.0"},
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier.endswith("iOS-17-0")


def test_parse_simctl_runtime_list_uses_id_fallback():
	payload = {
		"runtimes": [
			{"id": "com.apple.CoreSimulator.SimRuntime.watchOS-10-0", "version": "10.0", "state": "Ready"},
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	assert runtimes[0].identifier.endswith("watchOS-10-0")
	assert runtimes[0].version == "10.0"
	assert runtimes[0].state == "Ready"


def test_parse_simctl_runtime_list_invalid_json():
	runtimes, error = cleanup.parse_simctl_runtime_list("not json")
	assert runtimes == []
	assert error is not None


def test_parse_simctl_runtime_list_missing_size_defaults_to_zero():
	payload = {
		"runtimes": [
			{
				"identifier": "com.apple.CoreSimulator.SimRuntime.watchOS-10-0",
				"name": "watchOS 10.0",
			}
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert runtimes[0].size_bytes == 0


def test_parse_simctl_runtime_list_skips_empty_identifier():
	payload = {"runtimes": [{"identifier": "", "name": "Bad"}]}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert runtimes == []


def test_parse_simctl_runtime_list_defaults_fields():
	payload = {
		"runtimes": [
			{
				"identifier": "com.apple.CoreSimulator.SimRuntime.iOS-15-0",
			}
		]
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert len(runtimes) == 1
	runtime = runtimes[0]
	assert runtime.name == "Unknown"
	assert runtime.version == ""
	assert runtime.build == ""
	assert runtime.state == ""
	assert runtime.size_bytes == 0


def test_parse_simctl_runtime_list_mapping_skips_non_dict():
	payload = {
		"com.apple.CoreSimulator.SimRuntime.iOS-14-0": "junk",
	}
	runtimes, error = cleanup.parse_simctl_runtime_list(json.dumps(payload))
	assert error is None
	assert runtimes == []


def test_remove_runtime_backing_files_no_runtimes_still_removes_dirs(
	make_runner, fixture_text, monkeypatch
):
	runtime_list = fixture_text("simctl_runtime_list_empty.txt")
	volume = "/Library/Developer/CoreSimulator/Volumes/iOS_18.6"
	df_output = (
		"Filesystem 512-blocks Used Available Capacity iused ifree %iused Mounted on\n"
		f"/dev/disk7s1 1 1 1 1% 1 1 1% {volume}\n"
	)
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
		(False, True, ("df", volume)): (0, df_output, ""),
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (0, "", ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [volume])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=True)
	assert result.commands_ok is True
	commands = [call[2] for call in runner.calls]
	assert ("xcrun", "simctl", "runtime", "delete", "all") not in commands
	sudo_calls = [call for call in runner.calls if call[0] is True and call[2][0] == "/bin/sh"]
	assert sudo_calls
	assert "CoreSimulator/Cryptex" in sudo_calls[0][2][2]


def test_remove_runtime_backing_files_deletes_remaining(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runtime_empty = fixture_text("simctl_runtime_list_empty.txt")
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, runtime_list, ""),
			(0, runtime_empty, ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is True
	assert any(
		call[2] == ("xcrun", "simctl", "runtime", "delete", runtime_id)
		for call in runner.calls
	)


def test_remove_runtime_backing_files_list_error(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, "not json", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert result.error is not None


def test_remove_runtime_backing_files_list_nonzero(make_runner):
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (1, "", "simctl error"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert "simctl error" in (result.error or "")


def test_remove_runtime_backing_files_list_error_after_delete_all(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, "bad json", ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert "Failed to parse simctl runtime list" in (result.error or "")


def test_remove_runtime_backing_files_list_error_final(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runtime_id = "com.apple.CoreSimulator.SimRuntime.iOS-18-6"
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, runtime_list, ""),
			(0, "bad json", ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", runtime_id)): (0, "", ""),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert "Failed to parse simctl runtime list" in (result.error or "")


def test_remove_runtime_backing_files_skips_remove_dirs_when_disabled(
	make_runner, fixture_text, monkeypatch
):
	runtime_list = fixture_text("simctl_runtime_list_empty.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
	})
	service = cleanup.CleanupService(runner=runner)
	called = {"remove_dirs": False}

	def fake_remove_dirs():
		called["remove_dirs"] = True
		return []

	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	monkeypatch.setattr(service, "_remove_runtime_directories", fake_remove_dirs)
	monkeypatch.setattr(service, "_unmount_simulator_volumes", lambda: [])
	service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert called["remove_dirs"] is False


def test_remove_runtime_backing_files_includes_unmount_steps(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list_empty.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): (0, runtime_list, ""),
	})
	service = cleanup.CleanupService(runner=runner)
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	sentinel = cleanup.StepResult(
		label="unmount sentinel",
		result=cleanup.CmdResult(tuple(), 0, "", ""),
		required=False,
	)
	monkeypatch.setattr(service, "_unmount_simulator_volumes", lambda: [sentinel])
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert any(step.label == "unmount sentinel" for step in result.steps)


def test_remove_runtime_backing_files_delete_all_optional(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runtime_empty = fixture_text("simctl_runtime_list_empty.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, runtime_empty, ""),
			(0, runtime_empty, ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (1, "", "delete all failed"),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is True
	assert result.error is None


def test_remove_runtime_backing_files_delete_runtime_error(make_runner, fixture_text, monkeypatch):
	runtime_list = fixture_text("simctl_runtime_list.txt")
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "runtime", "list", "-j")): [
			(0, runtime_list, ""),
			(0, runtime_list, ""),
		],
		(False, True, ("xcrun", "simctl", "runtime", "delete", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "runtime", "delete", "com.apple.CoreSimulator.SimRuntime.iOS-18-6")): (
			1,
			"",
			"delete failed",
		),
	}, default=(0, "", ""))
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: [])
	service = cleanup.CleanupService(runner=runner)
	result = service.remove_runtime_backing_files(include_system_runtime_files=False)
	assert result.commands_ok is False
	assert "delete failed" in (result.error or "")
