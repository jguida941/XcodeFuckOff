"""
Cleanup services for XcodeFuckOff.

All external commands go through CommandRunner for testability.
"""
from __future__ import annotations

from dataclasses import dataclass
import glob
import json
import os
import re
import shlex
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from xcodefuckoff.core.runner import CmdResult, CommandRunner, get_default_runner
from xcodefuckoff.services import processes as svc_processes
from xcodefuckoff.services import space as svc_space
from xcodefuckoff.system import devtools as svc_devtools


DENIED_MARKERS = ("operation not permitted", "permission denied")
NOT_MOUNTED_MARKERS = ("not mounted", "not currently mounted", "not a mount point")

RUNTIME_GLOBS = (
	"/Library/Developer/CoreSimulator/Volumes/iOS_*",
	"/Library/Developer/CoreSimulator/Volumes/tvOS_*",
	"/Library/Developer/CoreSimulator/Volumes/watchOS_*",
	"/Library/Developer/CoreSimulator/Volumes/xrOS_*",
)
CRYP_TEX_PATH = "/Library/Developer/CoreSimulator/Cryptex"


@dataclass(frozen=True)
class StepResult:
	label: str
	result: CmdResult
	required: bool = True
	sudo: bool = False
	allow_not_mounted: bool = False

	@property
	def ok(self) -> bool:
		if self.result.timed_out:
			return False
		if _is_denied(self.result):
			return False
		if self.result.returncode == 0:
			return True
		if self.allow_not_mounted and _is_not_mounted(self.result):
			return True
		return False


@dataclass(frozen=True)
class ActionResult:
	commands_ok: bool
	steps: List[StepResult]
	error: Optional[str] = None


@dataclass(frozen=True)
class CleanupResult:
	commands_ok: bool
	space_before: Optional[int]
	space_after: Optional[int]
	space_delta: Optional[int]
	space_ok: Optional[bool]
	steps: List[StepResult]
	error: Optional[str] = None


@dataclass(frozen=True)
class RuntimeInfo:
	identifier: str
	name: str
	version: str
	build: str
	state: str
	size_bytes: int


def _is_denied(result: CmdResult) -> bool:
	message = f"{result.stderr} {result.stdout}".lower()
	return any(marker in message for marker in DENIED_MARKERS)


def _is_not_mounted(result: CmdResult) -> bool:
	message = f"{result.stderr} {result.stdout}".lower()
	return any(marker in message for marker in NOT_MOUNTED_MARKERS)


def _first_required_error(steps: Iterable[StepResult]) -> Optional[str]:
	for step in steps:
		if step.required and not step.ok:
			return step.result.stderr.strip() or step.result.stdout.strip() or f"{step.label} failed"
	return None


def _commands_ok(steps: Iterable[StepResult]) -> bool:
	return all(step.ok for step in steps if step.required)


def _parse_simctl_runtimes(payload: object) -> List[RuntimeInfo]:
	if isinstance(payload, dict):
		if "runtimes" in payload and isinstance(payload["runtimes"], list):
			entries = payload["runtimes"]
		elif "Runtimes" in payload and isinstance(payload["Runtimes"], list):
			entries = payload["Runtimes"]
		else:
			entries = []
			for runtime_id, info in payload.items():
				if isinstance(info, dict):
					info = dict(info)
					info["identifier"] = info.get("identifier", runtime_id)
					entries.append(info)
	elif isinstance(payload, list):
		entries = payload
	else:
		entries = []

	runtimes: List[RuntimeInfo] = []
	for info in entries:
		if not isinstance(info, dict):
			continue
		identifier = info.get("identifier") or info.get("id") or ""
		if not identifier:
			continue
		name = info.get("name", "Unknown")
		version = info.get("version", "")
		build = info.get("build") or info.get("buildversion", "") or ""
		state = info.get("state", "")
		size_bytes = int(info.get("sizeBytes") or info.get("bundleSize") or 0)
		runtimes.append(
			RuntimeInfo(
				identifier=identifier,
				name=name,
				version=version,
				build=build,
				state=state,
				size_bytes=size_bytes,
			)
		)
	return runtimes


def parse_simctl_runtime_list(text: str) -> Tuple[List[RuntimeInfo], Optional[str]]:
	try:
		payload = json.loads(text)
	except Exception as exc:
		return [], f"Failed to parse simctl runtime list: {exc}"
	return _parse_simctl_runtimes(payload), None


class CleanupService:
	def __init__(self, runner: CommandRunner | None = None, simctl_env: Mapping[str, str] | None = None):
		self._runner = runner or get_default_runner()
		self._simctl_env = dict(simctl_env) if simctl_env else None

	def _run_step(
		self,
		label: str,
		cmd: Sequence[str],
		*,
		sudo: bool = False,
		timeout: int | None = None,
		required: bool = True,
		allow_not_mounted: bool = False,
		text: bool = True,
		env: Mapping[str, str] | None = None,
	) -> StepResult:
		result = self._runner.run(cmd, sudo=sudo, timeout=timeout, text=text, env=env)
		return StepResult(
			label=label,
			result=result,
			required=required,
			sudo=sudo,
			allow_not_mounted=allow_not_mounted,
		)

	def _run_simctl_step(
		self,
		label: str,
		cmd: Sequence[str],
		*,
		required: bool = True,
		timeout: int | None = None,
	) -> StepResult:
		return self._run_step(label, cmd, required=required, timeout=timeout, env=self._simctl_env)

	def _run_sudo_batch(
		self,
		label: str,
		commands: Sequence[Sequence[str]],
		*,
		required: bool = True,
	) -> StepResult:
		parts = []
		for cmd in commands:
			parts.append(" ".join(shlex.quote(part) for part in cmd))
		cmd_str = " ; ".join(parts)
		return self._run_step(label, ["/bin/sh", "-c", cmd_str], sudo=True, required=required)

	def _space_snapshot(self) -> Optional[int]:
		return svc_space.get_apfs_available_bytes(runner=self._runner)

	def list_runtimes(self) -> Tuple[List[RuntimeInfo], StepResult, Optional[str]]:
		step = self._run_simctl_step(
			"xcrun simctl runtime list -j",
			["xcrun", "simctl", "runtime", "list", "-j"],
			required=True,
		)
		if step.result.returncode != 0:
			return [], step, step.result.stderr.strip() or "simctl runtime list failed"
		runtimes, parse_error = parse_simctl_runtime_list(step.result.stdout)
		if parse_error:
			return [], step, parse_error
		return runtimes, step, None

	def delete_runtimes(self, runtime_ids: Sequence[str]) -> ActionResult:
		steps: List[StepResult] = []
		for runtime_id in runtime_ids:
			step = self._run_simctl_step(
				f"xcrun simctl runtime delete {runtime_id}",
				["xcrun", "simctl", "runtime", "delete", runtime_id],
				required=True,
			)
			steps.append(step)
		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def delete_all_runtimes(self) -> ActionResult:
		steps: List[StepResult] = []
		delete_all_step = self._run_simctl_step(
			"xcrun simctl runtime delete all",
			["xcrun", "simctl", "runtime", "delete", "all"],
			required=False,
		)
		steps.append(delete_all_step)

		runtimes, list_step, list_error = self.list_runtimes()
		steps.append(list_step)
		if list_error:
			return ActionResult(commands_ok=False, steps=steps, error=list_error)

		delete_result = self.delete_runtimes([runtime.identifier for runtime in runtimes])
		steps.extend(delete_result.steps)
		error = delete_result.error or _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def delete_unavailable_runtimes(self) -> ActionResult:
		step = self._run_simctl_step(
			"xcrun simctl runtime delete unavailable",
			["xcrun", "simctl", "runtime", "delete", "unavailable"],
			required=True,
		)
		error = _first_required_error([step])
		return ActionResult(commands_ok=step.ok, steps=[step], error=error)

	def delete_all_sim_devices(self) -> ActionResult:
		steps = [
			self._run_simctl_step("xcrun simctl shutdown all", ["xcrun", "simctl", "shutdown", "all"], required=True),
			self._run_simctl_step("xcrun simctl delete all", ["xcrun", "simctl", "delete", "all"], required=True),
		]
		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def delete_unavailable_sim_devices(self) -> ActionResult:
		steps = [
			self._run_simctl_step("xcrun simctl shutdown all", ["xcrun", "simctl", "shutdown", "all"], required=True),
			self._run_simctl_step(
				"xcrun simctl delete unavailable",
				["xcrun", "simctl", "delete", "unavailable"],
				required=True,
			),
		]
		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def remove_device_directories_and_profiles(self) -> ActionResult:
		devices_path = os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")
		profiles_path = os.path.expanduser("~/Library/Developer/CoreSimulator/Profiles")
		steps = [
			self._run_step(f"rm -rf {devices_path}", ["rm", "-rf", devices_path], required=True),
			self._run_step(f"rm -rf {profiles_path}", ["rm", "-rf", profiles_path], required=True),
		]
		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def clear_paths(self, paths: Sequence[str], *, sudo: bool = False) -> ActionResult:
		steps: List[StepResult] = []
		for path in paths:
			expanded = os.path.expanduser(path)
			step = self._run_step(
				f"rm -rf {expanded}",
				["rm", "-rf", expanded],
				required=True,
				sudo=sudo,
			)
			steps.append(step)
		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def clear_all_simulator_caches(self) -> ActionResult:
		paths = [
			"~/Library/Developer/CoreSimulator/Caches",
			"~/Library/Developer/CoreSimulator/Temp",
			"~/Library/Caches/com.apple.CoreSimulator",
			"~/Library/Developer/Xcode/DerivedData",
		]
		return self.clear_paths(paths, sudo=False)

	def disable_core_simulator_service(self) -> ActionResult:
		user_scope = f"gui/{os.getuid()}/com.apple.CoreSimulator.CoreSimulatorService"
		step = self._run_sudo_batch(
			"launchctl bootout + disable CoreSimulator service",
			[
				["launchctl", "bootout", user_scope],
				["launchctl", "disable", user_scope],
			],
			required=False,
		)
		error = None if step.ok else (step.result.stderr.strip() or step.result.stdout.strip())
		return ActionResult(commands_ok=step.ok, steps=[step], error=error)

	def is_xcode_running(self) -> bool:
		if self._runner.run(["pgrep", "-x", "Xcode"]).returncode == 0:
			return True
		return self._runner.run(["pgrep", "-x", "Simulator"]).returncode == 0

	def get_mounted_simulator_volumes(self) -> List[str]:
		result = self._runner.run(["hdiutil", "info"])
		mounts = []
		for line in result.stdout.splitlines():
			if "Simulator" in line and "/Library/Developer/CoreSimulator/Volumes" in line:
				mounts.append(line.strip())
		return mounts

	def _get_parent_disk(self, slice_device: str) -> str:
		device = slice_device
		if device.startswith("disk"):
			device = f"/dev/{device}"
		match = re.match(r"(/dev/disk\d+)", device)
		if match:
			return match.group(1)
		return device

	def unmount_simulator_disk(self, device: str) -> ActionResult:
		parent = self._get_parent_disk(device)
		steps: List[StepResult] = []
		step = self._run_step(
			f"diskutil unmountDisk force {parent}",
			["diskutil", "unmountDisk", "force", parent],
			required=False,
			allow_not_mounted=True,
		)
		steps.append(step)
		if step.ok:
			return ActionResult(commands_ok=True, steps=steps, error=None)

		fallback = self._run_step(
			f"hdiutil detach {parent}",
			["hdiutil", "detach", parent, "-force"],
			required=False,
			allow_not_mounted=True,
		)
		steps.append(fallback)
		commands_ok = any(step.ok for step in steps)
		if commands_ok:
			error = None
		else:
			last = steps[-1].result if steps else CmdResult(tuple(), 1, "", "unmount failed")
			error = last.stderr.strip() or last.stdout.strip() or "unmount failed"
		return ActionResult(commands_ok=commands_ok, steps=steps, error=error)

	def _unmount_simulator_volumes(self) -> List[StepResult]:
		results: List[StepResult] = []
		volume_paths: List[str] = []
		for pattern in RUNTIME_GLOBS:
			volume_paths.extend(glob.glob(pattern))
		volume_paths = sorted(set(volume_paths))

		unmounted_parents = set()
		for vol_path in volume_paths:
			df_step = self._run_step(
				f"df {vol_path}",
				["df", vol_path],
				required=False,
			)
			results.append(df_step)
			if df_step.result.returncode != 0:
				continue

			lines = [ln for ln in df_step.result.stdout.splitlines() if ln.strip()]
			if len(lines) < 2:
				continue
			device = lines[1].split()[0]
			parent = self._get_parent_disk(device)
			if parent in unmounted_parents:
				continue

			unmount_result = self.unmount_simulator_disk(device)
			results.extend(unmount_result.steps)
			unmounted_parents.add(parent)

		return results

	def _remove_runtime_directories(self) -> List[StepResult]:
		paths: List[str] = []
		for pattern in RUNTIME_GLOBS:
			paths.extend(glob.glob(pattern))
		paths.append(CRYP_TEX_PATH)

		commands = [["rm", "-rf", path] for path in paths]
		step = self._run_sudo_batch("rm -rf simulator runtime directories", commands, required=True)
		return [step]

	def remove_runtime_backing_files(self, include_system_runtime_files: bool) -> ActionResult:
		steps: List[StepResult] = []

		runtimes_before, list_step, list_error = self.list_runtimes()
		steps.append(list_step)
		if list_error:
			return ActionResult(commands_ok=False, steps=steps, error=list_error)

		if runtimes_before:
			delete_all_step = self._run_simctl_step(
				"xcrun simctl runtime delete all",
				["xcrun", "simctl", "runtime", "delete", "all"],
				required=False,
			)
			steps.append(delete_all_step)

			runtimes_after_bulk, list_step_after, list_error_after = self.list_runtimes()
			steps.append(list_step_after)
			if list_error_after:
				return ActionResult(commands_ok=False, steps=steps, error=list_error_after)

			remaining = {runtime.identifier for runtime in runtimes_after_bulk}
			if remaining:
				delete_result = self.delete_runtimes(sorted(remaining))
				steps.extend(delete_result.steps)
				if delete_result.error:
					return ActionResult(commands_ok=False, steps=steps, error=delete_result.error)

			runtimes_final, list_step_final, list_error_final = self.list_runtimes()
			steps.append(list_step_final)
			if list_error_final:
				return ActionResult(commands_ok=False, steps=steps, error=list_error_final)

			final_ids = {runtime.identifier for runtime in runtimes_final}
			still_present = sorted({runtime.identifier for runtime in runtimes_before} & final_ids)
			if still_present:
				return ActionResult(
					commands_ok=False,
					steps=steps,
					error=f"Runtime still registered: {', '.join(still_present)}",
				)

		steps.extend(self._unmount_simulator_volumes())

		if include_system_runtime_files:
			steps.extend(self._remove_runtime_directories())

		error = _first_required_error(steps)
		return ActionResult(commands_ok=_commands_ok(steps), steps=steps, error=error)

	def manual_cleanup(
		self,
		*,
		delete_core_simulator: bool,
		delete_derived_data: bool,
		delete_archives: bool,
		delete_caches: bool,
		delete_device_support: bool,
		stop_processes: bool = True,
		measure_space: bool = True,
	) -> CleanupResult:
		space_before = self._space_snapshot() if measure_space else None
		steps: List[StepResult] = []

		if stop_processes:
			for result in svc_processes.kill_all_simulators_and_xcode(password=None, runner=self._runner):
				label = " ".join(result.cmd)
				steps.append(StepResult(label=label, result=result, required=False))

		steps.extend(self._unmount_simulator_volumes())

		paths: List[str] = []
		if delete_core_simulator:
			paths.append("~/Library/Developer/CoreSimulator")
		if delete_derived_data:
			paths.append("~/Library/Developer/Xcode/DerivedData")
		if delete_archives:
			paths.append("~/Library/Developer/Xcode/Archives")
		if delete_device_support:
			paths.append("~/Library/Developer/Xcode/iOS DeviceSupport")
		if delete_caches:
			paths.extend(
				[
					"~/Library/Caches/com.apple.dt.Xcode",
					"~/Library/Caches/org.swift.swiftpm",
				]
			)

		if paths:
			clear_result = self.clear_paths(paths, sudo=False)
			steps.extend(clear_result.steps)

		space_after = self._space_snapshot() if measure_space else None
		space_delta = None
		space_ok = None
		if space_before is not None and space_after is not None:
			space_delta = space_after - space_before
			space_ok = space_delta > 0

		error = _first_required_error(steps)
		return CleanupResult(
			commands_ok=_commands_ok(steps),
			space_before=space_before,
			space_after=space_after,
			space_delta=space_delta,
			space_ok=space_ok,
			steps=steps,
			error=error,
		)

	def free_runtime_space(
		self,
		include_system_runtime_files: bool,
		admin_password: Optional[str] = None,
		include_user_space: bool = False,
		delete_devices: bool = False,
		delete_derived_data: bool = False,
		stop_processes: bool = True,
		measure_space: bool = True,
	) -> CleanupResult:
		space_before = self._space_snapshot() if measure_space else None
		steps: List[StepResult] = []

		if stop_processes and include_system_runtime_files:
			for result in svc_processes.kill_all_simulators_and_xcode(password=None, runner=self._runner):
				label = " ".join(result.cmd)
				steps.append(StepResult(label=label, result=result, required=False))

		steps.extend(self.delete_unavailable_sim_devices().steps)

		if include_user_space:
			if delete_devices:
				devices_path = os.path.expanduser("~/Library/Developer/CoreSimulator/Devices")
				steps.append(
					self._run_step(
						f"rm -rf {devices_path}",
						["rm", "-rf", devices_path],
						required=True,
					)
				)
			if delete_derived_data:
				derived_path = os.path.expanduser("~/Library/Developer/Xcode/DerivedData")
				steps.append(
					self._run_step(
						f"rm -rf {derived_path}",
						["rm", "-rf", derived_path],
						required=True,
					)
				)

		if include_system_runtime_files:
			runtime_result = self.remove_runtime_backing_files(include_system_runtime_files=include_system_runtime_files)
			steps.extend(runtime_result.steps)
			if runtime_result.error:
				error = runtime_result.error
			else:
				error = None
		else:
			error = None

		space_after = self._space_snapshot() if measure_space else None
		space_delta = None
		space_ok = None
		if space_before is not None and space_after is not None:
			space_delta = space_after - space_before
			space_ok = space_delta > 0

		if not error:
			error = _first_required_error(steps)

		return CleanupResult(
			commands_ok=_commands_ok(steps),
			space_before=space_before,
			space_after=space_after,
			space_delta=space_delta,
			space_ok=space_ok,
			steps=steps,
			error=error,
		)

	def nuclear_cleanup(self) -> CleanupResult:
		steps: List[StepResult] = []

		for result in svc_processes.kill_all_simulators_and_xcode(password=None, runner=self._runner):
			label = " ".join(result.cmd)
			steps.append(StepResult(label=label, result=result, required=False))

		steps.extend(self.delete_all_sim_devices().steps)
		steps.extend(self.remove_device_directories_and_profiles().steps)
		steps.extend(self.clear_all_simulator_caches().steps)
		steps.extend(self.disable_core_simulator_service().steps)

		runtime_result = self.remove_runtime_backing_files(include_system_runtime_files=True)
		steps.extend(runtime_result.steps)
		error = runtime_result.error

		if not error:
			error = _first_required_error(steps)

		return CleanupResult(
			commands_ok=_commands_ok(steps),
			space_before=None,
			space_after=None,
			space_delta=None,
			space_ok=None,
			steps=steps,
			error=error,
		)


def _default_service() -> CleanupService:
	return CleanupService(simctl_env=svc_devtools.get_simctl_env())


def delete_all_sim_devices() -> bool:
	return _default_service().delete_all_sim_devices().commands_ok


def delete_unavailable_sim_devices() -> bool:
	return _default_service().delete_unavailable_sim_devices().commands_ok


def remove_device_directories_and_profiles() -> bool:
	return _default_service().remove_device_directories_and_profiles().commands_ok


def disable_core_simulator_service() -> bool:
	return _default_service().disable_core_simulator_service().commands_ok


def clear_all_simulator_caches() -> List[Tuple[str, int]]:
	result = _default_service().clear_all_simulator_caches()
	return [(step.label.replace("rm -rf ", ""), step.result.returncode) for step in result.steps]


def get_apfs_available_bytes() -> Optional[int]:
	return svc_space.get_apfs_available_bytes()


def df_bytes(path: str = "/System/Volumes/Data") -> Optional[Dict[str, int]]:
	return svc_space.df_bytes(path=path)


def list_runtimes() -> List[Dict[str, str]]:
	service = _default_service()
	runtimes, _, error = service.list_runtimes()
	if error:
		return []
	return [
		{
			"id": runtime.identifier,
			"name": runtime.name,
			"version": runtime.version,
			"build": runtime.build,
			"state": runtime.state,
			"sizeBytes": runtime.size_bytes,
		}
		for runtime in runtimes
	]


def delete_runtime(runtime_id: str) -> Tuple[bool, str]:
	result = _default_service().delete_runtimes([runtime_id])
	if result.commands_ok:
		return True, f"Deleted runtime {runtime_id}"
	return False, result.error or f"Failed to delete {runtime_id}"


def delete_all_runtimes() -> List[Tuple[str, int]]:
	result = _default_service().delete_all_runtimes()
	return [(step.label, step.result.returncode) for step in result.steps]


def delete_unavailable_runtimes() -> Tuple[bool, str]:
	result = _default_service().delete_unavailable_runtimes()
	if result.commands_ok:
		return True, "Done"
	return False, result.error or "Failed"


def is_xcode_running() -> bool:
	return _default_service().is_xcode_running()


def get_mounted_simulator_volumes() -> List[str]:
	return _default_service().get_mounted_simulator_volumes()


def remove_runtime_backing_files(admin_password: Optional[str] = None) -> List[Tuple[str, int]]:
	result = _default_service().remove_runtime_backing_files(include_system_runtime_files=True)
	return [(step.label, step.result.returncode) for step in result.steps]


def free_runtime_space(
	include_system_runtime_files: bool,
	admin_password: Optional[str] = None,
	include_user_space: bool = False,
	delete_devices: bool = False,
	delete_derived_data: bool = False,
	stop_processes: bool = True,
) -> CleanupResult:
	return _default_service().free_runtime_space(
		include_system_runtime_files=include_system_runtime_files,
		admin_password=admin_password,
		include_user_space=include_user_space,
		delete_devices=delete_devices,
		delete_derived_data=delete_derived_data,
		stop_processes=stop_processes,
	)


def nuclear_cleanup() -> CleanupResult:
	return _default_service().nuclear_cleanup()
