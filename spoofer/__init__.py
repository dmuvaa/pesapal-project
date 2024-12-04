# spoofer/__init__.py

from .logger import log_message
from .validators import is_valid_prefix, allowed_file
from .hashing import calculate_hash
from .pixel_modifier import modify_pixel
from .spoofer_core import ImageHashSpoofer

# Initialize package-level settings or utilities if necessary
log_message("Spoofer package initialized", "info")

__all__ = [
    "log_message",
    "is_valid_prefix",
    "allowed_file",
    "calculate_hash",
    "modify_pixel",
    "ImageHashSpoofer",
]
