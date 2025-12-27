# ADR 0001: CommandRunner and APFS Space Accounting

Status: Accepted  
Date: 2025-12-27  
Developer: Justin Guida  

## Context
XcodeFuckOff needs to orchestrate system commands (diskutil, hdiutil, xcrun, rm, launchctl) to unmount simulator disks and reclaim storage. The original implementation issued subprocess calls directly, which caused several problems:

- Unit tests could not reliably simulate system commands.
- Failures were not consistently surfaced, so the UI could report success when commands failed.
- APFS space accounting used df-style metrics or mounted volume sizes, which do not reflect true free space in APFS containers.
- simulator runtime deletion via simctl could fail silently, leaving runtimes registered.

## Decision
Introduce a CommandRunner abstraction and route all external commands through it. This enables deterministic tests with fixture-driven outputs and removes direct subprocess usage in services. Key elements:

- CommandRunner.run(...) returns a CmdResult (cmd, returncode, stdout/stderr text, stdout/stderr bytes, timed_out).
- Services accept a runner via constructor and expose pure parsing helpers.
- APFS space accounting uses `diskutil apfs list -plist` parsed as bytes, and the UI only claims reclaimed space when the APFS delta is positive.
- Runtime deletion verifies registry removal by re-listing runtimes after deletion.
- System-level deletes are performed via a single sudo batch where possible to reduce repeated privilege prompts.

## Consequences
- Tests can mock CommandRunner and validate command sequences, error handling, and parsing without touching the host system.
- UI success is driven by commands_ok and APFS delta, preventing false claims of reclaimed space.
- Some detailed per-path results are collapsed into batch sudo steps to avoid repeated authorization prompts.
- The runner still uses osascript for sudo (best-effort), which is documented and treated as a request rather than a guarantee.

## Notes
- The space metric is APFS container CapacityNotAllocated (preferred), with df output only as a fallback for display.
- The unmount flow targets parent disks (diskX) rather than slices (diskXsY) for reliability.
