"""
Lexora AI
Encoding Validator
"""

from pathlib import Path


def validate_encoding(file_path: str):

    report = {
        "encoding": "utf-8",
        "valid": True,
        "error": None
    }

    try:

        Path(file_path).read_text(
            encoding="utf-8"
        )

    except UnicodeDecodeError as error:

        report["valid"] = False
        report["error"] = str(error)

    return report
