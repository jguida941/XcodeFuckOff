"""
Deprecated aggregator module kept for backward compatibility.
Prefer importing from:
 - xcodecleaner.services.disks
 - xcodecleaner.services.processes
 - xcodecleaner.services.cleanup
 - xcodecleaner.system.sip
"""
from .services.disks import list_simulator_disks, force_unmount_disk, eject_disk
from .services.processes import (
	list_simulator_processes,
	kill_process,
	kill_all_simulators_and_xcode,
)
from .services.cleanup import (
	delete_all_sim_devices,
	remove_device_directories_and_profiles,
	disable_core_simulator_service,
	clear_all_simulator_caches,
)
from .system.sip import is_sip_enabled



