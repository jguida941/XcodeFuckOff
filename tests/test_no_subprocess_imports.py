from pathlib import Path
import re


def test_no_subprocess_imports_in_xcodefuckoff():
	root = Path(__file__).resolve().parents[1]
	allowed = {root / "xcodefuckoff" / "core" / "runner.py"}
	pattern = re.compile(r"^\s*(import\s+subprocess\b|from\s+subprocess\s+import\b)", re.MULTILINE)
	violations = []

	for path in root.glob("xcodefuckoff/**/*.py"):
		if path in allowed:
			continue
		text = path.read_text()
		if pattern.search(text):
			violations.append(str(path))

	assert violations == [], f"subprocess import found in: {violations}"
