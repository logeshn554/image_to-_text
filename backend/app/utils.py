from pathlib import Path
from .config import ALLOWED_EXTENSIONS


def is_valid_image_file(filename: str) -> bool:
    """Check if file has allowed image extension."""
    ext = Path(filename).suffix.lstrip(".").lower()
    return ext in ALLOWED_EXTENSIONS

