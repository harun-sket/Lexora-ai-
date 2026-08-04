"""
Lexora AI
File Manager v0.1

Creates unique filenames
without overwriting previous outputs.
"""

from pathlib import Path


def get_unique_filename(
    folder: str,
    filename: str
):
    """
    Generate a unique file path.
    """

    folder_path = Path(folder)

    folder_path.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = folder_path / filename

    if not file_path.exists():
        return file_path

    counter = 2

    while True:

        new_file = (
            f"{file_path.stem}"
            f"({counter})"
            f"{file_path.suffix}"
        )

        new_path = folder_path / new_file

        if not new_path.exists():
            return new_path

        counter += 1
