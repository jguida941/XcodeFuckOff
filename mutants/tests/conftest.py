from __future__ import annotations

from pathlib import Path
from typing import Iterable, Mapping, Tuple

import pytest

from xcodecleaner.core.runner import CmdResult


FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixture_text():
	def _load(name: str) -> str:
		return (FIXTURES_DIR / name).read_text()

	return _load


@pytest.fixture
def fixture_bytes():
	def _load(name: str) -> bytes:
		return (FIXTURES_DIR / name).read_bytes()

	return _load


class FakeRunner:
	def __init__(self, script: dict, default: Tuple[int, str | bytes, str | bytes] | None = None):
		self.script = script
		self.calls: list[tuple] = []
		self.default = default or (127, "", "unexpected command")

	def run(
		self,
		cmd: Iterable[str],
		*,
		sudo: bool = False,
		timeout=None,
		text: bool = True,
		env: Mapping[str, str] | None = None,
	) -> CmdResult:
		env_key = tuple(sorted((str(key), str(value)) for key, value in (env or {}).items())) if env else None
		key_with_env = (sudo, text, tuple(cmd), env_key)
		key = (sudo, text, tuple(cmd))
		self.calls.append(key_with_env if env_key is not None else key)

		entry = self.script.get(key_with_env)
		if entry is None:
			entry = self.script.get(key, self.default)
		if isinstance(entry, list):
			entry = entry.pop(0) if entry else self.default

		if isinstance(entry, CmdResult):
			return entry

		rc, out, err = entry
		if isinstance(out, bytes):
			stdout_bytes = out
			stdout = out.decode("utf-8", errors="replace")
		else:
			stdout = out
			stdout_bytes = out.encode("utf-8", errors="replace")

		if isinstance(err, bytes):
			stderr_bytes = err
			stderr = err.decode("utf-8", errors="replace")
		else:
			stderr = err
			stderr_bytes = err.encode("utf-8", errors="replace")

		return CmdResult(tuple(cmd), rc, stdout, stderr, stdout_bytes, stderr_bytes)


@pytest.fixture
def make_runner():
	def _make(script: dict, default=None) -> FakeRunner:
		return FakeRunner(script, default=default)

	return _make
