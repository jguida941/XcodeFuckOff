from xcodecleaner.services import disks


def test_parses_simulator_disks_from_diskutil_list(fixture_text):
	text = fixture_text("diskutil_list_before.txt")
	found = disks.parse_diskutil_list(text)
	assert "disk7s1" in found
	assert "disk11s1" in found


def test_parses_diskutil_info_size_bytes(fixture_text):
	info = disks.parse_diskutil_info(fixture_text("diskutil_info_disk7s1.txt"))
	assert info["name"] == "iOS 18.6 Simulator"
	assert info["mount"] == "/Library/Developer/CoreSimulator/Volumes/iOS_18.6"
	assert info["size_bytes"] is not None
	assert info["size_bytes"] > 20 * 1024**3


def test_parse_diskutil_info_total_size_and_not_mounted():
	text = (
		"Volume Name: Test Runtime\n"
		"Mount Point: Not Mounted\n"
		"Total Size: 1.0 GB (1000000000 Bytes)\n"
	)
	info = disks.parse_diskutil_info(text)
	assert info["name"] == "Test Runtime"
	assert info["mount"] == "Not Mounted"
	assert info["size_bytes"] == 1000000000


def test_parse_diskutil_info_missing_bytes():
	text = (
		"Volume Name: Test Runtime\n"
		"Mount Point: /Library/Developer/CoreSimulator/Volumes/iOS_Test\n"
		"Disk Size: 1.0 GB\n"
	)
	info = disks.parse_diskutil_info(text)
	assert info["size_bytes"] is None


def test_parse_diskutil_info_disk_size_precedence():
	text = (
		"Volume Name: Test Runtime\n"
		"Mount Point: /Library/Developer/CoreSimulator/Volumes/iOS_Test\n"
		"Disk Size: 2.0 GB (2000000000 Bytes)\n"
		"Total Size: 1.0 GB (1000000000 Bytes)\n"
	)
	info = disks.parse_diskutil_info(text)
	assert info["size_bytes"] == 2000000000


def test_parse_diskutil_info_not_applicable_mount():
	text = (
		"Volume Name: Test Runtime\n"
		"Mount Point: Not Applicable (not mounted)\n"
		"Disk Size: 1.0 GB (1000000000 Bytes)\n"
	)
	info = disks.parse_diskutil_info(text)
	assert info["mount"] == "Not Mounted"


def test_parse_diskutil_info_missing_name_defaults_unknown():
	text = (
		"Mount Point: /Library/Developer/CoreSimulator/Volumes/iOS_Test\n"
		"Disk Size: 1.0 GB (1000000000 Bytes)\n"
	)
	info = disks.parse_diskutil_info(text)
	assert info["name"] == "Unknown"


def test_list_simulator_disks_uses_runner_and_progress(make_runner, fixture_text):
	list_output = fixture_text("diskutil_list_before.txt")
	info_output = fixture_text("diskutil_info_disk7s1.txt")
	runner = make_runner({
		(False, True, ("diskutil", "list")): (0, list_output, ""),
		(False, True, ("diskutil", "info", "/dev/disk7s1")): (0, info_output, ""),
		(False, True, ("diskutil", "info", "/dev/disk11s1")): (0, info_output, ""),
	})
	progress = []

	def callback(value):
		progress.append(value)

	result = disks.list_simulator_disks(progress_callback=callback, runner=runner)
	assert [disk["device"] for disk in result] == ["/dev/disk7s1", "/dev/disk11s1"]
	assert progress == [0, 50]
	commands = [call[2] for call in runner.calls]
	assert ("diskutil", "info", "/dev/disk7s1") in commands
	assert ("diskutil", "info", "/dev/disk11s1") in commands


def test_force_unmount_disk_not_mounted(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk1")): (1, "", "not mounted"),
		(False, True, ("hdiutil", "detach", "-force", "/dev/disk1")): (1, "", "not mounted"),
	}, default=(1, "", "fail"))
	ok, msg = disks.force_unmount_disk("/dev/disk1", runner=runner)
	assert ok is True
	assert "already unmounted" in msg.lower()


def test_force_unmount_disk_falls_back_to_hdiutil(make_runner):
	runner = make_runner({
		(False, True, ("diskutil", "unmountDisk", "force", "/dev/disk1")): (1, "", "diskutil fail"),
		(False, True, ("hdiutil", "detach", "-force", "/dev/disk1")): (0, "", ""),
	}, default=(1, "", "fail"))
	ok, msg = disks.force_unmount_disk("/dev/disk1", runner=runner)
	assert ok is True
	assert "detached" in msg.lower()
