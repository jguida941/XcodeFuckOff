from xcodecleaner.services import processes


def test_parse_ps_aux_filters_simulator_processes():
	ps_output = (
		"USER       PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND\n"
		"me       1234   0.0  0.1     1234   5678   ??  S    10:01AM  0:00.00 /Applications/Xcode.app/Contents/MacOS/Xcode\n"
		"me       2001   1.0  0.5     1234   5678   ??  S    10:02AM  0:01.00 com.apple.CoreSimulator.CoreSimulatorService\n"
		"me       3001   2.0  0.9     1234   5678   ??  S    10:02AM  0:02.00 iOS Simulator\n"
	)
	result = processes._parse_ps_aux(ps_output)
	assert any("CoreSimulator" in proc["name"] for proc in result)
	assert any("Simulator" in proc["name"] for proc in result)
	assert all("Xcode.app" not in proc["name"] for proc in result)


def test_stop_coresimulator_daemon_calls_launchctl(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	results = processes.stop_coresimulator_daemon(runner=runner)
	assert len(results) == 2
	user_scope = f"gui/{processes.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	commands = [call[2] for call in runner.calls]
	assert ("launchctl", "bootout", user_scope) in commands
	assert ("launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService") in commands


def test_run_commands_no_admin_handles_exception():
	class BoomRunner:
		def __init__(self):
			self.calls = 0

		def run(self, cmd):
			self.calls += 1
			if self.calls == 1:
				raise RuntimeError("boom")
			return processes.CmdResult(tuple(cmd), 0, "", "")

	results = processes._run_commands_no_admin([["cmd1"], ["cmd2"]], runner=BoomRunner())
	assert results[0].returncode == 1
	assert "exception" in results[0].stderr.lower()
	assert results[1].returncode == 0


def test_kill_all_simulators_and_xcode_includes_pkill(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	processes.kill_all_simulators_and_xcode(runner=runner)
	commands = [call[2] for call in runner.calls]
	assert ("pkill", "-9", "-f", "Simulator") in commands
	assert ("pkill", "-9", "-x", "Xcode") in commands


def test_stop_coresimulator_daemon_handles_exceptions():
	class BoomRunner:
		def run(self, cmd):
			raise RuntimeError("boom")

	results = processes.stop_coresimulator_daemon(runner=BoomRunner())
	assert all(result.returncode == 1 for result in results)
	assert all("exception" in result.stderr.lower() for result in results)


def test_kill_all_simulators_and_xcode_returns_all_results(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	results = processes.kill_all_simulators_and_xcode(runner=runner)
	assert len(results) == 2 + 6


def test_parse_ps_aux_skips_incomplete_lines():
	ps_output = "USER PID %CPU %MEM VSZ RSS TT STAT STARTED TIME COMMAND\nbad line\n"
	result = processes._parse_ps_aux(ps_output)
	assert result == []
