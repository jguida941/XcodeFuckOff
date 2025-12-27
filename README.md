# XcodeFuckOff

Because uninstalling Xcode apparently isn’t enough.

A PyQt6 macOS utility to manage Xcode Simulator mounts and reclaim disk space.  
Native macOS chrome and a clean, themeable UI.  
Built out of pure hatred for Xcode.  

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Screenshot](#screenshot)
- [Why this exists](#why-this-exists)
- [Important: Eject ≠ Free Space](#important-eject--free-space)
- [What the app does](#what-the-app-does)
- [Installation](#installation)
- [CLI Usage](#cli-usage)
- [Development](#development)
- [Themes](#themes)
- [Xcode Requirement](#xcode-requirement)
- [Known Limitations](#known-limitations)
- [Safety Notes](#safety-notes)
- [Architecture](#architecture)
- [License](#license)

## Features

- Native macOS traffic light buttons with full window management
- 5 color themes: Neon, Cyber Red, Electric Blue, Purple Haze, Forest & Gold
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
python scripts/launch_xcodefuckoff.py
```

Creates a local venv, installs dependencies, and launches the GUI.

### Option B: Manual

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m xcodefuckoff
```

## CLI Usage

```bash
# Launch GUI (default)
python -m xcodefuckoff

# Run full cleanup headless (no GUI)
python -m xcodefuckoff --nuclear
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

- **Neon** - Dark with cyan/teal accent (default)
- **Cyber Red** - Dark with red/orange gradient
- **Electric Blue** - Dark with electric blue accent
- **Purple Haze** - Dark purple with gold accents
- **Forest & Gold** - Luxe forest green with gold buttons

## Xcode Requirement

The app uses `xcrun simctl` commands which require **Xcode** or **Xcode Command Line Tools** to be installed.

**Don't have Xcode installed?** No problem - the app will detect this and offer a **Manual Cleanup** option that directly removes simulator files without needing Xcode commands.

## Known Limitations

- **SIP (System Integrity Protection)**: SIP does not usually block `/Library/Developer/...` cleanup. Failures are typically permissions/ownership or CoreSimulator locks. `xcrun simctl runtime delete` is the supported removal path.
- Xcode can recreate default devices and re-download runtimes when you open Xcode or build iOS apps.
- Unmount-only cleanup is temporary; disk images can reattach until runtimes are unregistered and backing files are deleted.

## Safety Notes

- Deleting `/Library/Developer/CoreSimulator/...` requires admin and removes installed simulator runtimes.
- If unsure, run **Free Runtime Space** and answer **No** to the system-runtime prompt for user-space only cleanup.
- Always verify what you're deleting - the Nuclear Option is aggressive!

## Architecture

### Project Structure

```
XcodeFuckOff/
├── assets/                  # App icons and screenshots
├── docs/
│   └── adr/                 # Architecture Decision Records
├── scripts/
│   └── launch_xcodefuckoff.py  # Auto-venv launcher
├── tests/
│   ├── fixtures/            # Test data (diskutil output, etc.)
│   ├── conftest.py          # Pytest fixtures
│   └── test_*.py            # Unit tests
├── xcodefuckoff/
│   ├── __main__.py          # CLI entry point
│   ├── core/
│   │   └── runner.py        # CommandRunner abstraction
│   ├── services/
│   │   ├── cleanup.py       # Cleanup orchestration
│   │   ├── disks.py         # Disk detection/unmounting
│   │   ├── processes.py     # Process management
│   │   └── space.py         # APFS space measurement
│   ├── system/
│   │   ├── devtools.py      # Xcode/simctl detection
│   │   └── sip.py           # SIP status checking
│   └── gui/
│       ├── app.py           # Application entry point
│       ├── main_window.py   # Main window (composes mixins)
│       ├── styles.py        # Theme definitions
│       ├── threads.py       # Background workers
│       ├── widgets.py       # Reusable widgets
│       └── mixins/          # UI functionality by concern
│           ├── chrome.py    # Native macOS window chrome
│           ├── tabs.py      # Tab layout
│           ├── actions.py   # Cleanup actions
│           ├── monitoring.py # Background scanning
│           └── logging.py   # Activity log & notifications
├── pyproject.toml           # Package config & dependencies
├── requirements.txt         # Runtime dependencies
└── README.md
```

### Architecture Decision Records

| ADR | Title | Summary |
|-----|-------|---------|
| [0001](docs/adr/0001-command-runner-and-space-accounting.md) | CommandRunner & Space Accounting | Subprocess abstraction for testability; APFS-based space metrics |
| [0002](docs/adr/0002-gui-mixin-architecture.md) | GUI Mixin Architecture | Main window split into composable mixins |
| [0003](docs/adr/0003-native-macos-integration.md) | Native macOS Integration | PyObjC for window chrome and menu bar |
| [0004](docs/adr/0004-devtools-fallback.md) | DevTools Fallback | Manual cleanup when Xcode isn't installed |
| [0005](docs/adr/0005-theme-system.md) | Theme System | Qt Stylesheets with theme dictionaries |

## License

MIT

## Author

[@jguida941](https://github.com/jguida941)
