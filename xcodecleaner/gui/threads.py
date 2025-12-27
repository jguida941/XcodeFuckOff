from PyQt6.QtCore import QThread, pyqtSignal

from xcodecleaner.core.runner import CommandRunner, get_default_runner
from xcodecleaner.services import cleanup as svc_cleanup
from xcodecleaner.services import disks as svc_disks
from xcodecleaner.services import processes as svc_processes


class DiskScanner(QThread):
	update_signal = pyqtSignal(list)
	progress_signal = pyqtSignal(int)

	def __init__(self, runner: CommandRunner | None = None, parent=None):
		super().__init__(parent)
		self._runner = runner or get_default_runner()

	def run(self):
		try:
			disk_info = svc_disks.list_simulator_disks(progress_callback=self.progress_signal.emit, runner=self._runner)
			self.update_signal.emit(disk_info)
		except Exception:
			self.update_signal.emit([])


class ProcessMonitor(QThread):
	update_signal = pyqtSignal(list)

	def __init__(self, runner: CommandRunner | None = None, parent=None):
		super().__init__(parent)
		self._runner = runner or get_default_runner()

	def run(self):
		try:
			processes = svc_processes.list_simulator_processes(runner=self._runner)
			self.update_signal.emit(processes)
		except Exception:
			self.update_signal.emit([])


class FreeRuntimeSpaceWorker(QThread):
	"""
	Run the space-reclaim cleanup off the UI thread so the app doesn't beachball.
	"""

	done_signal = pyqtSignal(object)
	error_signal = pyqtSignal(str)

	def __init__(
		self,
		include_system_runtime_files: bool,
		include_user_space: bool,
		delete_devices: bool,
		delete_derived_data: bool,
		stop_processes: bool,
		simctl_env: dict[str, str] | None = None,
		runner: CommandRunner | None = None,
		parent=None,
	):
		super().__init__(parent)
		self.include_system_runtime_files = include_system_runtime_files
		self.include_user_space = include_user_space
		self.delete_devices = delete_devices
		self.delete_derived_data = delete_derived_data
		self.stop_processes = stop_processes
		self.simctl_env = simctl_env
		self._runner = runner or get_default_runner()

	def run(self):
		try:
			service = svc_cleanup.CleanupService(runner=self._runner, simctl_env=self.simctl_env)
			result = service.free_runtime_space(
				include_system_runtime_files=self.include_system_runtime_files,
				admin_password=None,
				include_user_space=self.include_user_space,
				delete_devices=self.delete_devices,
				delete_derived_data=self.delete_derived_data,
				stop_processes=self.stop_processes,
			)
			self.done_signal.emit(result)
		except Exception as exc:
			self.error_signal.emit(str(exc))


class ManualCleanupWorker(QThread):
	done_signal = pyqtSignal(object)
	error_signal = pyqtSignal(str)

	def __init__(
		self,
		delete_core_simulator: bool,
		delete_derived_data: bool,
		delete_archives: bool,
		delete_caches: bool,
		delete_device_support: bool,
		stop_processes: bool,
		runner: CommandRunner | None = None,
		parent=None,
	):
		super().__init__(parent)
		self.delete_core_simulator = delete_core_simulator
		self.delete_derived_data = delete_derived_data
		self.delete_archives = delete_archives
		self.delete_caches = delete_caches
		self.delete_device_support = delete_device_support
		self.stop_processes = stop_processes
		self._runner = runner or get_default_runner()

	def run(self):
		try:
			service = svc_cleanup.CleanupService(runner=self._runner)
			result = service.manual_cleanup(
				delete_core_simulator=self.delete_core_simulator,
				delete_derived_data=self.delete_derived_data,
				delete_archives=self.delete_archives,
				delete_caches=self.delete_caches,
				delete_device_support=self.delete_device_support,
				stop_processes=self.stop_processes,
			)
			self.done_signal.emit(result)
		except Exception as exc:
			self.error_signal.emit(str(exc))


class NuclearCleanupWorker(QThread):
	done_signal = pyqtSignal(object)
	error_signal = pyqtSignal(str)

	def __init__(self, simctl_env: dict[str, str] | None = None, runner: CommandRunner | None = None, parent=None):
		super().__init__(parent)
		self.simctl_env = simctl_env
		self._runner = runner or get_default_runner()

	def run(self):
		try:
			service = svc_cleanup.CleanupService(runner=self._runner, simctl_env=self.simctl_env)
			result = service.nuclear_cleanup()
			self.done_signal.emit(result)
		except Exception as exc:
			self.error_signal.emit(str(exc))
