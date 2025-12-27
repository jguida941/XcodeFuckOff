import re
import subprocess
from PyQt6.QtCore import QThread, pyqtSignal

from xcodecleaner.services import cleanup as svc_cleanup


class DiskScanner(QThread):
	update_signal = pyqtSignal(list)
	progress_signal = pyqtSignal(int)

	def run(self):
		try:
			result = subprocess.run(["diskutil", "list"], capture_output=True, text=True)
			disk_info = []
			lines = result.stdout.split("\n")
			seen = set()
			keywords = ("Simulator", "Xcode", "iOS", "watchOS", "tvOS")
			for i, line in enumerate(lines):
				self.progress_signal.emit(int((i / max(1, len(lines))) * 100))
				if not any(k in line for k in keywords):
					continue
				m = re.search(r"\b(disk\d+s\d+)\b", line)
				if not m:
					continue
				device = f"/dev/{m.group(1)}"
				if device in seen:
					continue
				seen.add(device)

				info_result = subprocess.run(["diskutil", "info", device], capture_output=True, text=True)
				volume_name = ""
				mount_point = ""
				size = ""
				for info_line in info_result.stdout.split("\n"):
					if "Volume Name:" in info_line:
						volume_name = info_line.split("Volume Name:")[1].strip()
					elif "Mount Point:" in info_line:
						mount_point = info_line.split("Mount Point:")[1].strip()
					elif "Disk Size:" in info_line:
						size = info_line.split("Disk Size:")[1].strip().split()[0]
				if mount_point.lower().startswith("not applicable"):
					mount_point = ""
				if volume_name or mount_point:
					disk_info.append(
						{"device": device, "name": volume_name or "Unknown", "mount": mount_point or "Not Mounted", "size": size or "Unknown"}
					)
			self.update_signal.emit(disk_info)
		except Exception:
			self.update_signal.emit([])


class ProcessMonitor(QThread):
	update_signal = pyqtSignal(list)

	def run(self):
		try:
			ps_result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
			processes = []
			keywords = ["Simulator", "CoreSimulator", "SimulatorTrampoline", "launchd_sim"]
			for line in ps_result.stdout.split("\n")[1:]:
				parts = line.split()
				if len(parts) >= 11:
					process_name = " ".join(parts[10:])
					if any(keyword in process_name for keyword in keywords):
						processes.append(
							{
								"pid": parts[1],
								"cpu": parts[2],
								"mem": parts[3],
								"name": process_name[:50] + "..." if len(process_name) > 50 else process_name,
							}
						)
			self.update_signal.emit(processes)
		except Exception:
			self.update_signal.emit([])


class FreeRuntimeSpaceWorker(QThread):
	"""
	Run the space-reclaim cleanup off the UI thread so the app doesn't beachball.
	"""

	done_signal = pyqtSignal(dict)
	error_signal = pyqtSignal(str)

	def __init__(
		self,
		include_system_runtime_files: bool,
		include_user_space: bool,
		delete_devices: bool,
		delete_derived_data: bool,
		stop_processes: bool,
		parent=None,
	):
		super().__init__(parent)
		self.include_system_runtime_files = include_system_runtime_files
		self.include_user_space = include_user_space
		self.delete_devices = delete_devices
		self.delete_derived_data = delete_derived_data
		self.stop_processes = stop_processes

	def run(self):
		try:
			result = svc_cleanup.free_runtime_space(
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


