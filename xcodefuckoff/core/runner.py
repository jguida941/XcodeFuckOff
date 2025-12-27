"""
Command execution abstraction for XcodeFuckOff.

This module provides a CommandRunner protocol that abstracts subprocess execution,
enabling dependency injection for testability. Tests can provide a mock runner
that returns pre-recorded outputs instead of executing real system commands.

Example usage in tests:
    class FakeRunner:
        def __init__(self, responses: dict):
            self.responses = responses
            self.calls = []

        def run(self, cmd, *, sudo=False, timeout=None, text=True, env=None):
            key = (sudo, bool(text), tuple(cmd), tuple(sorted((env or {}).items())) if env else None)
            self.calls.append(key)
            rc, out, err = self.responses.get(key, (127, "", "not found"))
            stdout = out if isinstance(out, str) else out.decode("utf-8", errors="replace")
            stderr = err if isinstance(err, str) else err.decode("utf-8", errors="replace")
            return CmdResult(tuple(cmd), rc, stdout, stderr, out if isinstance(out, bytes) else b"", err if isinstance(err, bytes) else b"")

    runner = FakeRunner({(False, True, ("diskutil", "list"), None): (0, fixture_output, b"")})
    disks = list_simulator_disks(runner=runner)
"""
from __future__ import annotations

from dataclasses import dataclass
import os
import shlex
import subprocess
from typing import Mapping, Protocol, Sequence


@dataclass(frozen=True)
class CmdResult:
	"""
	Result of a command execution.

	Attributes:
		cmd: The command that was executed as a tuple of strings.
		returncode: Exit code (0 = success, non-zero = failure).
		stdout: Standard output captured from the command as text.
		stderr: Standard error captured from the command as text.
		stdout_bytes: Raw stdout bytes (useful for plist or binary output).
		stderr_bytes: Raw stderr bytes.
		timed_out: True if the command timed out.
	"""
	cmd: tuple[str, ...]
	returncode: int
	stdout: str
	stderr: str
	stdout_bytes: bytes = b""
	stderr_bytes: bytes = b""
	timed_out: bool = False


class CommandRunner(Protocol):
	"""
	Protocol for command execution.

	This abstraction allows tests to inject a mock runner that returns
	pre-recorded outputs instead of executing real system commands.
	All service functions accept an optional runner parameter.
	"""
	def run(
		self,
		cmd: Sequence[str],
		*,
		sudo: bool = False,
		timeout: int | None = None,
		text: bool = True,
		env: Mapping[str, str] | None = None,
	) -> CmdResult: ...


class SubprocessRunner:
	"""
	Default command runner using subprocess.

	Executes commands via subprocess.run(). When sudo=True, uses osascript
	to request admin privileges via macOS system dialog (best-effort).
	"""

	def _coerce_output(
		self,
		stdout: str | bytes | None,
		stderr: str | bytes | None,
	) -> tuple[str, str, bytes, bytes]:
		if stdout is None:
			stdout_bytes = b""
			stdout_text = ""
		elif isinstance(stdout, bytes):
			stdout_bytes = stdout
			stdout_text = stdout.decode("utf-8", errors="replace")
		else:
			stdout_text = stdout
			stdout_bytes = stdout.encode("utf-8", errors="replace")

		if stderr is None:
			stderr_bytes = b""
			stderr_text = ""
		elif isinstance(stderr, bytes):
			stderr_bytes = stderr
			stderr_text = stderr.decode("utf-8", errors="replace")
		else:
			stderr_text = stderr
			stderr_bytes = stderr.encode("utf-8", errors="replace")

		return stdout_text, stderr_text, stdout_bytes, stderr_bytes

	def _merge_env(self, env: Mapping[str, str] | None) -> dict[str, str] | None:
		if env is None:
			return None
		merged = os.environ.copy()
		for key, value in env.items():
			merged[str(key)] = str(value)
		return merged

	def run(
		self,
		cmd: Sequence[str],
		*,
		sudo: bool = False,
		timeout: int | None = None,
		text: bool = True,
		env: Mapping[str, str] | None = None,
	) -> CmdResult:
		"""
		Execute a command and return the result.

		Args:
			cmd: Command and arguments as a sequence of strings.
			sudo: If True, run with admin privileges via osascript.
			timeout: Optional timeout in seconds.

		Returns:
			CmdResult with returncode, stdout, and stderr.
		"""
		cmd_list = [str(part) for part in cmd]
		env_vars = self._merge_env(env)
		try:
			if sudo:
				env_prefix = ""
				if env:
					env_prefix = " ".join(f"{key}={shlex.quote(str(value))}" for key, value in env.items())
				cmd_str = " ".join(shlex.quote(part) for part in cmd_list)
				if env_prefix:
					cmd_str = f"{env_prefix} {cmd_str}"
				escaped = cmd_str.replace("\\", "\\\\").replace('"', '\\"')
				script = f'do shell script "{escaped}" with administrator privileges'
				result = subprocess.run(
					["osascript", "-e", script],
					capture_output=True,
					text=text,
					timeout=timeout,
					check=False,
				)
			else:
				result = subprocess.run(
					cmd_list,
					capture_output=True,
					text=text,
					timeout=timeout,
					check=False,
					env=env_vars,
				)
			stdout_text, stderr_text, stdout_bytes, stderr_bytes = self._coerce_output(result.stdout, result.stderr)
			return CmdResult(
				tuple(cmd_list),
				result.returncode,
				stdout_text,
				stderr_text,
				stdout_bytes,
				stderr_bytes,
				timed_out=False,
			)
		except subprocess.TimeoutExpired as exc:
			stdout_text, stderr_text, stdout_bytes, stderr_bytes = self._coerce_output(exc.stdout, exc.stderr)
			if not stderr_text:
				stderr_text = f"timeout after {timeout}s"
				stderr_bytes = stderr_text.encode("utf-8")
			return CmdResult(
				tuple(cmd_list),
				124,
				stdout_text,
				stderr_text,
				stdout_bytes,
				stderr_bytes,
				timed_out=True,
			)


_DEFAULT_RUNNER: SubprocessRunner | None = None


def get_default_runner() -> SubprocessRunner:
	"""
	Get the cached default runner instance.

	Returns a shared SubprocessRunner instance. Service functions use this
	when no runner is explicitly provided. Tests should pass a runner explicitly.
	"""
	global _DEFAULT_RUNNER
	if _DEFAULT_RUNNER is None:
		_DEFAULT_RUNNER = SubprocessRunner()
	return _DEFAULT_RUNNER
