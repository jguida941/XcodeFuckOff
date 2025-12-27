"""GUI mixins that compose the main window functionality."""

__all__ = [
	"ChromeMixin",
	"TabsMixin",
	"MonitoringMixin",
	"ActionsMixin",
	"LoggingMixin",
]

from .actions import ActionsMixin
from .chrome import ChromeMixin
from .logging import LoggingMixin
from .monitoring import MonitoringMixin
from .tabs import TabsMixin


