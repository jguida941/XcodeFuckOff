import argparse

from .services import cleanup


def cmd_nuclear(password: str | None) -> int:
	result = cleanup.nuclear_cleanup()
	return 0 if result.commands_ok else 1


def gui_main() -> int:
	from .gui.app import main as app_main
	return app_main()


def main() -> int:
	parser = argparse.ArgumentParser(prog="xcodefuckoff", description="Headless utilities for Xcode/Simulator cleanup")
	parser.add_argument("--gui", action="store_true", help="Launch the GUI")
	parser.add_argument("--nuclear", action="store_true", help="Run full cleanup (kills, deletes, clears caches)")
	parser.add_argument("--password", default=None, help="Admin password (optional).")
	args = parser.parse_args()

	if args.gui or (not args.nuclear):
		return gui_main()

	if args.nuclear:
		return cmd_nuclear(args.password)

	parser.print_help()
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
