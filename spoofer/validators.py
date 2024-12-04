import re

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def is_valid_prefix(prefix: str) -> bool:
    """Validate if the target prefix is a valid hexadecimal string."""
    return bool(re.fullmatch(r"0x[a-fA-F0-9]+", prefix))

def allowed_file(filename: str) -> bool:
    """Check if the file has a valid image extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
