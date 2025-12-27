import pytest

from xcodecleaner.services import cleanup


@pytest.mark.parametrize(
	"before_name, after_name, expected_ok",
	[
		("diskutil_apfs_list_before.txt", "diskutil_apfs_list_before.txt", False),
		("diskutil_apfs_list_before.txt", "diskutil_apfs_list_after_smaller.txt", False),
		("diskutil_apfs_list_before.txt", "diskutil_apfs_list_after.txt", True),
	],
)
def test_space_ok_strictly_positive(make_runner, fixture_bytes, before_name, after_name, expected_ok):
	before = fixture_bytes(before_name)
	after = fixture_bytes(after_name)
	runner = make_runner({
		(False, True, ("xcrun", "simctl", "shutdown", "all")): (0, "", ""),
		(False, True, ("xcrun", "simctl", "delete", "unavailable")): (0, "", ""),
		(False, False, ("diskutil", "apfs", "list", "-plist")): [
			(0, before, b""),
			(0, after, b""),
		],
	})
	service = cleanup.CleanupService(runner=runner)
	result = service.free_runtime_space(include_system_runtime_files=False, include_user_space=False)
	assert result.commands_ok is True
	assert result.space_ok == expected_ok
