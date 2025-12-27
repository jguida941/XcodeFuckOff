# ADR 0002: GUI Mixin Architecture

Status: Accepted
Date: 2024-12-27
Developer: Justin Guida

## Context
The main application window (EnhancedSimulatorKiller) combines multiple responsibilities:
- Window chrome and native macOS integration
- Tab-based UI layout
- Background monitoring (disk scanning, process monitoring)
- Cleanup actions (eject, free space, nuclear option)
- Activity logging and notifications

A monolithic class would be difficult to maintain and test. Different aspects need different testing approaches.

## Decision
Split the main window into composable mixins, each handling a specific concern:

- **ChromeMixin**: Native macOS window chrome, title bar, traffic light buttons
- **TabsMixin**: Tab-based UI layout (Dashboard, Processes, Settings, Log)
- **MonitoringMixin**: Background QTimer-based disk/process scanning
- **ActionsMixin**: Cleanup operations and their worker threads
- **LoggingMixin**: Activity log, notifications, theme switching, log export

The main class inherits from all mixins:
```python
class EnhancedSimulatorKiller(QWidget, ChromeMixin, TabsMixin, MonitoringMixin, ActionsMixin, LoggingMixin):
```

## Consequences
- Each mixin can be understood in isolation (~100-300 lines each instead of ~1500 in one file)
- Related functionality is grouped together (all logging in one file, all actions in another)
- Mixins share state via `self` - they're not truly independent, but the separation aids readability
- Order of inheritance matters for method resolution (Python MRO)
- Testing individual mixins requires careful mocking of shared state

## Notes
- Mixins are located in `xcodefuckoff/gui/mixins/`
- Each mixin has a class-level docstring explaining its responsibility
- Widget initialization happens in `__init__` of the main class; mixins configure behavior
