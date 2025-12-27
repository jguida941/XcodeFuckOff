import os

from xcodecleaner.system import devtools


def test_get_simctl_env_prefers_developer_dir_env(monkeypatch):
	path = "/Custom/Xcode.app/Contents/Developer"
	monkeypatch.setenv("DEVELOPER_DIR", path)
	monkeypatch.setattr(devtools.os.path, "isdir", lambda p: p == path)
	assert devtools.get_simctl_env() == {"DEVELOPER_DIR": path}


def test_get_simctl_env_none_when_xcode_selected(make_runner, monkeypatch):
	monkeypatch.delenv("DEVELOPER_DIR", raising=False)
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (0, "/Applications/Xcode.app/Contents/Developer", ""),
	})
	assert devtools.get_simctl_env(runner=runner) is None


def test_check_devtools_allows_clt_with_xcode_env(make_runner, monkeypatch):
	monkeypatch.delenv("DEVELOPER_DIR", raising=False)
	monkeypatch.setattr(
		devtools.os.path,
		"isdir",
		lambda p: p == devtools.DEFAULT_XCODE_DEVELOPER_DIR,
	)
	env_key = (("DEVELOPER_DIR", devtools.DEFAULT_XCODE_DEVELOPER_DIR),)
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (0, "/Library/Developer/CommandLineTools", ""),
		(False, True, ("xcrun", "simctl", "list"), env_key): (0, "", ""),
	})
	ok, message = devtools.check_devtools(runner=runner)
	assert ok is True
	assert "Using Xcode" in message


def test_check_devtools_missing_xcode_select(make_runner):
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (1, "", "not found"),
	})
	ok, message = devtools.check_devtools(runner=runner)
	assert ok is False
	assert "Command Line Tools not found" in message


def test_check_devtools_clt_without_xcode(make_runner, monkeypatch):
	monkeypatch.delenv("DEVELOPER_DIR", raising=False)
	monkeypatch.setattr(devtools.os.path, "isdir", lambda p: False)
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (0, "/Library/Developer/CommandLineTools", ""),
	})
	ok, message = devtools.check_devtools(runner=runner)
	assert ok is False
	assert "CommandLineTools" in message


def test_check_devtools_simctl_unavailable(make_runner):
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (0, "/Applications/Xcode.app/Contents/Developer", ""),
		(False, True, ("xcrun", "simctl", "list")): (72, "", "xcrun: error"),
	})
	ok, message = devtools.check_devtools(runner=runner)
	assert ok is False
	assert "simctl not working" in message


def test_check_devtools_happy_path(make_runner):
	runner = make_runner({
		(False, True, ("xcode-select", "-p")): (0, "/Applications/Xcode.app/Contents/Developer", ""),
		(False, True, ("xcrun", "simctl", "list")): (0, "", ""),
	})
	ok, message = devtools.check_devtools(runner=runner)
	assert ok is True
	assert "Developer tools configured correctly" in message
