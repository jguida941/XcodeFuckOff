# ADR 0003: Native macOS Integration via PyObjC

Status: Accepted
Date: 2024-12-27
Developer: Justin Guida

## Context
PyQt6 provides cross-platform widgets, but macOS users expect native behaviors:
- Traffic light buttons (close/minimize/zoom) with proper functionality
- App name in menu bar (not "python" or "__main__.py")
- Native window title bar appearance
- High DPI scaling

Qt's built-in macOS support is limited - it shows "Python" in the menu bar and the Dock when running as a script.

## Decision
Use PyObjC to access native macOS APIs alongside PyQt6:

1. **Window Chrome**: Keep Qt's default window flags (no FramelessWindowHint) to get native traffic lights automatically. Use `NSWindow.setTitleVisibility_()` to hide the title text since we have our own centered title.

2. **Menu Bar App Name**: Use PyObjC to modify:
   - `NSBundle.mainBundle().infoDictionary()` - set CFBundleName
   - `NSApplication.sharedApplication().mainMenu()` - update menu item titles

3. **Timing**: Menu updates use `QTimer.singleShot(100, ...)` to run after Qt has created its default menus.

```python
# In app.py
def _update_macos_menus():
    ns_app = NSApplication.sharedApplication()
    main_menu = ns_app.mainMenu()
    # Update "Quit __main__.py" -> "Quit Xcode Disk Ejector"
```

## Consequences
- Native look and feel on macOS
- PyObjC is an optional dependency - app still works (with degraded UX) if not installed
- All PyObjC usage is wrapped in try/except with `HAS_PYOBJC` checks
- Dock icon still shows as "exec" when running as a script (requires .app bundle to fix fully)
- Menu bar updates may briefly flash the wrong name on startup

## Notes
- PyObjC modules used: AppKit, Foundation, Cocoa
- The `.app` bundle limitation is documented in README
- Future: Consider py2app for proper .app packaging
