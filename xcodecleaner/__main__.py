import argparse
from .services import cleanup, processes
from .gui.app import main as gui_main


def cmd_nuclear(password: str | None) -> int:
	# Order mirrors GUI nuclear flow
	processes.kill_all_simulators_and_xcode(password)
	cleanup.delete_all_sim_devices()
	cleanup.remove_device_directories_and_profiles()
	cleanup.disable_core_simulator_service()
	cleanup.clear_all_simulator_caches()
	return 0


def main() -> int:
	parser = argparse.ArgumentParser(prog="xcodecleaner", description="Headless utilities for Xcode/Simulator cleanup")
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


