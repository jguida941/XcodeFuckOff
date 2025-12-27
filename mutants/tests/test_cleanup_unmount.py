from xcodecleaner.services import cleanup


def test_unmount_disk_fallback_success_marks_ok(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (1, "", "diskutil fail"),
		(False, True, ("hdiutil", "detach", "/dev/disk7", "-force")): (0, "", ""),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.unmount_simulator_disk("/dev/disk7s1")
	assert result.commands_ok is True
	assert result.error is None
	assert runner.calls == [
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")),
		(False, True, ("hdiutil", "detach", "/dev/disk7", "-force")),
	]


def test_unmount_disk_all_fail_reports_last_error(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (1, "", "diskutil fail"),
		(False, True, ("hdiutil", "detach", "/dev/disk7", "-force")): (1, "", "hdiutil fail"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.unmount_simulator_disk("/dev/disk7s1")
	assert result.commands_ok is False
	assert "hdiutil fail" in (result.error or "")


def test_get_parent_disk_strips_slice(make_runner):
	service = cleanup.CleanupService(runner=make_runner({}, default=(0, "", "")))
	assert service._get_parent_disk("disk7s1") == "/dev/disk7"
	assert service._get_parent_disk("/dev/disk7s1") == "/dev/disk7"


def test_unmount_disk_not_mounted_is_ok(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (1, "", "not mounted"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.unmount_simulator_disk("/dev/disk7s1")
	assert result.commands_ok is True
	assert result.error is None


def test_unmount_simulator_volumes_dedup_parent(make_runner, monkeypatch):
	volumes = [
		"/Library/Developer/CoreSimulator/Volumes/iOS_18.6",
		"/Library/Developer/CoreSimulator/Volumes/iOS_18.6_dup",
	]
	monkeypatch.setattr(cleanup.glob, "glob", lambda pattern: volumes)
	df_output = (
		"Filesystem 512-blocks Used Available Capacity iused ifree %iused Mounted on\n"
		"/dev/disk7s1 1 1 1 1% 1 1 1% /Library/Developer/CoreSimulator/Volumes/iOS_18.6\n"
	)
	runner = make_runner({
		(False, True, ("df", volumes[0])): (0, df_output, ""),
		(False, True, ("df", volumes[1])): (0, df_output, ""),
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (0, "", ""),
	}, default=(0, "", ""))
	service = cleanup.CleanupService(runner=runner)
	steps = service._unmount_simulator_volumes()
	assert len(steps) >= 2
	assert runner.calls.count((False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7"))) == 1


def test_unmount_disk_success_skips_hdiutil(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (0, "", ""),
	}, default=(1, "", "fail"))
	service = cleanup.CleanupService(runner=runner)
	result = service.unmount_simulator_disk("/dev/disk7s1")
	assert result.commands_ok is True
	assert not any(call[2][0] == "hdiutil" for call in runner.calls)


def test_unmount_disk_fallback_not_mounted_ok(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk7")): (1, "", "busy"),
		(False, True, ("hdiutil", "detach", "/dev/disk7", "-force")): (1, "", "not mounted"),
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.unmount_simulator_disk("/dev/disk7s1")
	assert result.commands_ok is True
	assert result.error is None
