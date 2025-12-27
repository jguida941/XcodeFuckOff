# Xcode Disk Ejector

A modern PyQt6 macOS utility to manage Xcode Simulator mounts and reclaim disk space. Features native macOS window chrome, multiple color themes, and a clean futuristic UI.

## Features

- Native macOS traffic light buttons with full window management
- 5 color themes: Neon, Cyber Red, Electric Blue, Purple Haze, Matrix
- Real-time process monitoring for simulator processes
- Disk space tracking and cleanup utilities
- Activity logging

## Requirements

- macOS 12+ (Monterey or later)
- Python 3.10+
- Xcode or Xcode Command Line Tools (see [Xcode Requirement](#xcode-requirement) for alternatives)

## Screenshot

![Xcode Disk Ejector Utility](assets/app.py.png)

## Why this exists

Xcode/iOS Simulator can mount disk images (runtimes / Cryptex) that:
- Show up in Finder and Disk Utility
- Reappear after manual eject
- Consume significant disk space (often tens of GB)
- And it's annoying as F***

## Important: Eject ≠ Free Space

**Ejecting a simulator disk only unmounts it.**
The disk space is still consumed by the backing files until you delete them.

### Where the space lives

- **System runtime backing files (largest)**
  - `/Library/Developer/CoreSimulator/Volumes/`
  - `/Library/Developer/CoreSimulator/Cryptex/`
- **User-space simulator data**
  - `~/Library/Developer/CoreSimulator/Devices/`
  - `~/Library/Developer/Xcode/DerivedData/`

## What the app does

| Button | Action |
|--------|--------|
| **Scan Disks** | Find simulator-related mounted volumes |
| **Eject Selected** | Unmount selected simulator volumes (does *not* free space) |
| **Free Runtime Space** | Safe cleanup that actually reclaims space |
| **Nuclear Option** | Aggressive cleanup (kills processes, deletes devices, clears caches) |

### Free Runtime Space performs:
- `xcrun simctl shutdown all`
- `xcrun simctl delete unavailable`
- Deletes user-space simulator devices + DerivedData
- Optionally deletes system runtime files (**requires admin**)

## Installation

### Option A: Launcher (recommended)

```bash
python scripts/launch_xcodecleaner.py
```

Creates a local venv, installs dependencies, and launches the GUI.

### Option B: Manual

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m xcodecleaner
```

## CLI Usage

```bash
# Launch GUI (default)
python -m xcodecleaner

# Run full cleanup headless (no GUI)
python -m xcodecleaner --nuclear
```

## Verify reclaimed space

```bash
df -h /System/Volumes/Data
```

## Development

```bash
pip install -e ".[dev]"
pytest -v
```

## Themes

Switch themes from the **Menu** button in the app:

- **Neon** - Dark with cyan accent
- **Cyber Red** - Dark with red/orange gradient
- **Electric Blue** - Dark with electric blue accent
- **Purple Haze** - Dark purple with gold buttons
- **Matrix** - Terminal style with green/amber

## Xcode Requirement

The app uses `xcrun simctl` commands which require **Xcode** or **Xcode Command Line Tools** to be installed.

**Don't have Xcode installed?** No problem - the app will detect this and offer a **Manual Cleanup** option that directly removes simulator files without needing Xcode commands.

## Known Limitations

- **SIP (System Integrity Protection)**: Some system runtime files are protected. The app uses `xcrun simctl runtime delete` which respects SIP.
- Simulators will be re-created if you open Xcode or run iOS builds.
- Some mounted disk images may reappear after reboot until backing files are deleted.

## Safety Notes

- Deleting `/Library/Developer/CoreSimulator/...` requires admin and removes installed simulator runtimes.
- If unsure, run **Free Runtime Space** and answer **No** to the system-runtime prompt for user-space only cleanup.
- Always verify what you're deleting - the Nuclear Option is aggressive!

## License

MIT

## Author

[@jguida941](https://github.com/jguida941)
