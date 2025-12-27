# ADR 0004: DevTools Fallback for Manual Cleanup

Status: Accepted
Date: 2024-12-27
Developer: Justin Guida

## Context
XcodeFuckOff primarily uses `xcrun simctl` commands to manage simulator runtimes:
- `simctl shutdown all`
- `simctl delete unavailable`
- `simctl runtime delete <identifier>`

However, many users want to reclaim disk space but don't have Xcode installed (they may have uninstalled it, or only have the Command Line Tools). The `simctl` binary requires a full Xcode installation.

## Decision
Implement a two-tier cleanup system:

1. **Primary (simctl available)**: Use `xcrun simctl` for proper runtime unregistration and deletion. This is the preferred path as it correctly updates Xcode's runtime registry.

2. **Fallback (manual cleanup)**: When simctl is unavailable, offer direct file deletion:
   - `~/Library/Developer/CoreSimulator/` - all simulator data
   - `~/Library/Developer/Xcode/DerivedData/` - build artifacts
   - `~/Library/Developer/Xcode/Archives/` - app archives
   - `~/Library/Caches/com.apple.dt.Xcode/` - Xcode caches
   - `~/Library/Developer/Xcode/iOS DeviceSupport/` - device symbols

Detection flow in `_check_devtools_available()`:
```python
if not simctl_ok and allow_manual:
    # Prompt user: "Manual Cleanup" or "Cancel"
    if user_chose_manual:
        return False, True  # (simctl_ok=False, manual_only=True)
```

## Consequences
- Users without Xcode can still reclaim significant disk space
- Manual cleanup cannot unregister runtimes from Xcode's registry (if Xcode is later installed, it may be confused)
- Manual cleanup uses simple `rm -rf` via shutil, no admin privileges needed for user-space paths
- System paths (`/Library/Developer/CoreSimulator/`) still require admin and are not offered in manual mode
- Clear messaging tells users what manual mode can and cannot do

## Notes
- DevTools detection is in `xcodefuckoff/system/devtools.py`
- Manual cleanup worker is `ManualCleanupWorker` in `gui/threads.py`
- README documents the Xcode requirement and manual fallback
