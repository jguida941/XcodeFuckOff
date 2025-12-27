import types
from xcodecleaner.services import disks, processes, cleanup
from xcodecleaner.system import sip


class DummyCompleted:
	def __init__(self, returncode=0, stdout="", stderr=""):
		self.returncode = returncode
		self.stdout = stdout
		self.stderr = stderr


def test_is_sip_enabled_enabled(monkeypatch):
	def fake_check_output(cmd, text=True):
		assert "csrutil" in cmd[0]
		return "System Integrity Protection status: enabled."

	monkeypatch.setattr(sip.subprocess, "check_output", fake_check_output)
	assert sip.is_sip_enabled() is True


def test_force_unmount_disk_success(monkeypatch):
	def fake_run(cmd, capture_output=True, text=True, timeout=10):
		assert cmd[:3] == ["hdiutil", "detach", "-force"]
		return DummyCompleted(returncode=0)

	monkeypatch.setattr(disks.subprocess, "run", fake_run)
	ok, msg = disks.force_unmount_disk("/dev/disk1")
	assert ok is True
	assert "Detached" in msg


def test_list_simulator_processes_parsing(monkeypatch):
	ps_output = (
		"USER       PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND\n"
		"me       1234   0.0  0.1     1234   5678   ??  S    10:01AM  0:00.00 /Applications/Xcode.app/Contents/MacOS/Xcode\n"
		"me       2001   1.0  0.5     1234   5678   ??  S    10:02AM  0:01.00 com.apple.CoreSimulator.CoreSimulatorService\n"
		"me       3001   2.0  0.9     1234   5678   ??  S    10:02AM  0:02.00 iOS Simulator\n"
	)

	def fake_run(cmd, capture_output=True, text=True):
		assert cmd[0] == "ps"
		return DummyCompleted(returncode=0, stdout=ps_output)

	monkeypatch.setattr(processes.subprocess, "run", fake_run)
	result = processes.list_simulator_processes()
	assert any("CoreSimulator" in p["name"] for p in result)
	assert any("Simulator" in p["name"] for p in result)


def test_clear_all_simulator_caches_calls(monkeypatch):
	called = []

	def fake_run(cmd, check=False):
		# rm -rf <expanded>
		assert cmd[0] == "rm" and cmd[1] == "-rf"
		called.append(cmd[2])
		return DummyCompleted(returncode=0)

	monkeypatch.setattr(cleanup.subprocess, "run", fake_run)
	results = cleanup.clear_all_simulator_caches()
	assert len(results) >= 3
	assert all(rc == 0 for _, rc in results)
	assert any("/Library/Developer/Xcode/DerivedData" in p for p in called)


def test_kill_all_includes_xcode(monkeypatch):
	seen = []

	def fake_run(cmd, shell=False, check=False):
		seen.append(cmd)
		return DummyCompleted(returncode=0)

	monkeypatch.setattr(processes.subprocess, "run", fake_run)
	processes.kill_all_simulators_and_xcode(password=None)
	assert any("Xcode" in cmd for cmd in seen)


