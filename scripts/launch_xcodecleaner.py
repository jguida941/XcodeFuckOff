#!/usr/bin/env python3
"""
Launch XcodeCleaner from ANY working directory.

What it does:
1) Finds this repo root (where this script lives)
2) Creates/uses a local venv at .venv/
3) Installs runtime deps (requirements.txt) and installs the project in editable mode
4) Launches the PyQt6 app via `python -m xcodecleaner` using the venv's python
"""

from __future__ import annotations

import os
import subprocess
import sys
import venv
from pathlib import Path


def _venv_python(venv_dir: Path) -> Path:
	if sys.platform == "win32":
		return venv_dir / "Scripts" / "python.exe"
	return venv_dir / "bin" / "python"


def _run(cmd: list[str], cwd: Path) -> None:
	subprocess.run(cmd, cwd=str(cwd), check=True)


def ensure_venv(repo_root: Path) -> Path:
	venv_dir = repo_root / ".venv"
	py = _venv_python(venv_dir)
	if py.exists():
		return py

	print(f"[launcher] creating venv: {venv_dir}")
	venv.EnvBuilder(with_pip=True).create(str(venv_dir))
	if not py.exists():
		raise RuntimeError(f"venv python not found at {py}")
	return py


def install_deps(repo_root: Path, py: Path) -> None:
	print("[launcher] upgrading pip/setuptools/wheel")
	_run([str(py), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"], cwd=repo_root)

	req = repo_root / "requirements.txt"
	if req.exists():
		print("[launcher] installing requirements.txt")
		_run([str(py), "-m", "pip", "install", "-r", str(req)], cwd=repo_root)

	# Install the package itself so imports work regardless of cwd
	print("[launcher] installing project (editable)")
	_run([str(py), "-m", "pip", "install", "-e", str(repo_root)], cwd=repo_root)


def main() -> int:
	repo_root = Path(__file__).resolve().parent.parent
	py = ensure_venv(repo_root)

	try:
		install_deps(repo_root, py)
	except subprocess.CalledProcessError as exc:
		print(f"[launcher] ERROR: dependency install failed: {exc}", file=sys.stderr)
		print("[launcher] Note: this step needs internet access for pip downloads.", file=sys.stderr)
		return exc.returncode or 1

	print("[launcher] starting GUI...")
	os.execv(str(py), [str(py), "-m", "xcodecleaner"])
	return 0


if __name__ == "__main__":
	raise SystemExit(main())


