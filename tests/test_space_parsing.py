import plistlib

from xcodefuckoff.services import space


def test_df_parse_bytes(fixture_text):
	result = space.parse_df_output(fixture_text("df_before.txt"))
	assert result is not None
	assert result["available_bytes"] == 208000000 * 1024


def test_apfs_not_allocated_delta(fixture_bytes):
	before = space.parse_apfs_not_allocated(fixture_bytes("diskutil_apfs_list_before.txt"))
	after = space.parse_apfs_not_allocated(fixture_bytes("diskutil_apfs_list_after.txt"))
	assert before == 100000000000
	assert after == 155000000000
	assert after - before == 55_000_000_000


def test_df_bytes_uses_runner(make_runner, fixture_text):
	runner = make_runner({
		(False, True, ("df", "-k", "/System/Volumes/Data")): (0, fixture_text("df_before.txt"), ""),
	})
	result = space.df_bytes(runner=runner)
	assert result is not None
	assert result["available_bytes"] == 208000000 * 1024


def test_get_apfs_available_bytes_uses_bytes_output(make_runner, fixture_bytes):
	before = fixture_bytes("diskutil_apfs_list_before.txt")
	runner = make_runner({
		(False, False, ("diskutil", "apfs", "list", "-plist")): (0, before, b""),
	})
	assert space.get_apfs_available_bytes(runner=runner) == 100000000000


def test_get_apfs_available_bytes_returns_none_on_error(make_runner):
	runner = make_runner({
		(False, False, ("diskutil", "apfs", "list", "-plist")): (1, b"", b"error"),
	})
	assert space.get_apfs_available_bytes(runner=runner) is None


def test_find_container_for_mount_by_mount_point():
	container = {
		"Volumes": [{"MountPoint": "/System/Volumes/Data"}],
		"CapacityNotAllocated": 123,
	}
	apfs = {"Containers": [container]}
	assert space._find_container_for_mount(apfs, "/System/Volumes/Data") == container


def test_find_container_for_mount_by_role():
	container = {
		"Volumes": [{"Roles": ["Data"], "MountPoint": "/System/Volumes/VM"}],
		"CapacityNotAllocated": 456,
	}
	apfs = {"Containers": [container]}
	assert space._find_container_for_mount(apfs, "/System/Volumes/Data") == container


def test_find_container_for_mount_returns_none():
	apfs = {"Containers": [{"Volumes": [{"MountPoint": "/Other"}]}]}
	assert space._find_container_for_mount(apfs, "/System/Volumes/Data") is None


def test_parse_df_output_invalid_returns_none():
	assert space.parse_df_output("Filesystem") is None
	assert space.parse_df_output("Filesystem\\nnot numbers here") is None
	assert space.parse_df_output("Filesystem 1 2 3 4\\n/dev/disk1 a b c d") is None


def test_parse_df_output_uses_last_line():
	text = (
		"Filesystem 1K-blocks Used Available\n"
		"/dev/disk1 10 2 8\n"
		"/dev/disk2 20 5 15\n"
	)
	result = space.parse_df_output(text)
	assert result is not None
	assert result["blocks_bytes"] == 20 * 1024
	assert result["used_bytes"] == 5 * 1024
	assert result["available_bytes"] == 15 * 1024


def test_parse_df_output_accepts_four_columns():
	text = "Filesystem 1K-blocks Used Available\n/dev/disk1 7 3 4\n"
	result = space.parse_df_output(text)
	assert result is not None
	assert result["blocks_bytes"] == 7 * 1024
	assert result["used_bytes"] == 3 * 1024
	assert result["available_bytes"] == 4 * 1024


def test_parse_apfs_not_allocated_falls_back_to_capacity_free():
	container = {"Volumes": [{"MountPoint": "/System/Volumes/Data"}], "CapacityFree": 123}
	payload = plistlib.dumps({"Containers": [container]})
	assert space.parse_apfs_not_allocated(payload) == 123


def test_parse_apfs_not_allocated_falls_back_to_capacity_available():
	container = {"Volumes": [{"MountPoint": "/System/Volumes/Data"}], "CapacityAvailable": 456}
	payload = plistlib.dumps({"Containers": [container]})
	assert space.parse_apfs_not_allocated(payload) == 456


def test_parse_apfs_not_allocated_returns_none_without_container():
	payload = plistlib.dumps({})
	assert space.parse_apfs_not_allocated(payload) is None


def test_find_container_for_mount_handles_missing_containers():
	assert space._find_container_for_mount({}, "/System/Volumes/Data") is None


def test_find_container_for_mount_ignores_roles_for_other_mounts():
	container = {"Volumes": [{"Roles": ["Data"], "MountPoint": "/System/Volumes/VM"}]}
	apfs = {"Containers": [container]}
	assert space._find_container_for_mount(apfs, "/System/Volumes/Other") is None
