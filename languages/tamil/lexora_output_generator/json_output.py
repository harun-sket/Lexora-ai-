"""
Lexora AI - Tamil Language Pack

JSON Output Generator v0.1

Creates clean JSON output files.
"""

import json
from pathlib import Path


def save_json_output(
    data: list,
    output_path: str
):
    """
    Save cleaned JSON dataset.
    """

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    return path
