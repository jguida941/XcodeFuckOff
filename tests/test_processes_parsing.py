from xcodefuckoff.services import processes


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


def test_kill_all_simulators_and_xcode_launchctl_first(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	processes.kill_all_simulators_and_xcode(runner=runner)
	commands = [call[2] for call in runner.calls]
	assert commands[0][0] == "launchctl"
	assert commands[1][0] == "launchctl"


def test_kill_all_simulators_and_xcode_command_list(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	processes.kill_all_simulators_and_xcode(runner=runner)
	user_scope = f"gui/{processes.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	expected = [
		("launchctl", "bootout", user_scope),
		("launchctl", "remove", "com.apple.CoreSimulator.CoreSimulatorService"),
		("pkill", "-9", "-f", "Simulator"),
		("pkill", "-9", "-f", "CoreSimulator"),
		("pkill", "-9", "-f", "SimulatorTrampoline"),
		("pkill", "-9", "-f", "launchd_sim"),
		("killall", "-9", "com.apple.CoreSimulator.CoreSimulatorService"),
		("pkill", "-9", "-x", "Xcode"),
	]
	assert [call[2] for call in runner.calls] == expected


def test_parse_ps_aux_parses_fields():
	ps_output = (
		"USER PID %CPU %MEM VSZ RSS TT STAT STARTED TIME COMMAND\n"
		"user 4321 12.3 4.5 1234 5678 ?? S 10:00AM 0:01.00 "
		"/Applications/Simulator.app/Contents/MacOS/Simulator --foo bar\n"
	)
	result = processes._parse_ps_aux(ps_output)
	assert len(result) == 1
	assert result[0]["pid"] == "4321"
	assert result[0]["cpu"] == "12.3"
	assert result[0]["mem"] == "4.5"
	assert result[0]["name"].endswith("Simulator --foo bar")


def test_kill_all_simulators_and_xcode_admin_combines_commands(make_runner):
	runner = make_runner({}, default=(0, "", ""))
	combined, rc = processes.kill_all_simulators_and_xcode_admin(runner=runner)
	user_scope = f"gui/{processes.os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
	assert rc == 0
	assert f"launchctl bootout {user_scope}" in combined
	assert "pkill -9 -x Xcode" in combined
	assert any(call[0] is True and call[2][0] == "/bin/sh" for call in runner.calls)


def test_kill_process_returns_true_on_success(make_runner):
	runner = make_runner({
		(False, True, ("kill", "-9", "123")): (0, "", ""),
	})
	assert processes.kill_process("123", runner=runner) is True


def test_kill_process_returns_false_on_failure(make_runner):
	runner = make_runner({
		(False, True, ("kill", "-9", "123")): (1, "", "fail"),
	})
	assert processes.kill_process("123", runner=runner) is False
