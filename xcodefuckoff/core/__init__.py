"""
Deprecated aggregator module kept for backward compatibility.
Prefer importing from:
 - xcodefuckoff.services.disks
 - xcodefuckoff.services.processes
 - xcodefuckoff.services.cleanup
 - xcodefuckoff.system.sip
"""
from xcodefuckoff.core.runner import CmdResult, CommandRunner, SubprocessRunner, get_default_runner

__all__ = [
	"list_simulator_disks",
	"force_unmount_disk",
	"eject_disk",
	"list_simulator_processes",
	"kill_process",
	"kill_all_simulators_and_xcode",
	"stop_coresimulator_daemon",
	"delete_all_sim_devices",
	"remove_device_directories_and_profiles",
	"disable_core_simulator_service",
	"clear_all_simulator_caches",
	"list_runtimes",
	"delete_runtime",
	"delete_all_runtimes",
	"get_apfs_available_bytes",
	"is_sip_enabled",
	"CmdResult",
	"CommandRunner",
	"SubprocessRunner",
	"get_default_runner",
]


def __getattr__(name: str):
	if name in {"CmdResult", "CommandRunner", "SubprocessRunner", "get_default_runner"}:
		return globals()[name]

	if name in {"list_simulator_disks", "force_unmount_disk", "eject_disk"}:
		from xcodefuckoff.services import disks

		return getattr(disks, name)
	if name in {"list_simulator_processes", "kill_process", "kill_all_simulators_and_xcode", "stop_coresimulator_daemon"}:
		from xcodefuckoff.services import processes

		return getattr(processes, name)
	if name in {
		"delete_all_sim_devices",
		"remove_device_directories_and_profiles",
		"disable_core_simulator_service",
		"clear_all_simulator_caches",
		"list_runtimes",
		"delete_runtime",
		"delete_all_runtimes",
		"get_apfs_available_bytes",
	}:
		from xcodefuckoff.services import cleanup

		return getattr(cleanup, name)
	if name == "is_sip_enabled":
		from xcodefuckoff.system import sip

		return getattr(sip, name)
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
