"""
Lexora AI - Tamil Language Pack

TXT Refinery v0.1

Processes raw TXT files and creates
clean AI-ready text data.
"""

from pathlib import Path

from languages.tamil.lexora_brain.rules_engine import (
    refine_text
)

from languages.tamil.lexora_brain.validator import (
    validate_text
)

from languages.tamil.lexora_brain.quality_engine import (
    calculate_text_quality
)


def read_txt_file(file_path: str) -> str:
    """
    Read TXT file content.
    """

    path = Path(file_path)

    return path.read_text(
        encoding="utf-8"
    )


def refine_txt_file(file_path: str) -> dict:
    """
    Complete TXT refinement pipeline.
    """

    original_text = read_txt_file(
        file_path
    )

    cleaned_text = refine_text(
        original_text
    )

    validation = validate_text(
        cleaned_text
    )

    quality = calculate_text_quality(
        original_text,
        cleaned_text
    )

    return {
        "clean_text": cleaned_text,
        "validation": validation,
        "quality_report": quality
    }
