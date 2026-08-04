"""
Lexora AI - Tamil Language Pack
File Detection Module

Responsible for identifying supported input formats.
"""

from pathlib import Path


SUPPORTED_FORMATS = {
    ".txt": "TXT",
    ".json": "JSON"
}


def detect_file_type(file_path: str) -> str:
    """
    Detect the uploaded file type.
    """

    extension = Path(file_path).suffix.lower()

    if extension in SUPPORTED_FORMATS:
        return SUPPORTED_FORMATS[extension]

    raise ValueError(
        f"Unsupported file format: {extension}"
    )
