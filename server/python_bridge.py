from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from languages.tamil.unified_engine import process


def make_json_safe(value):
    if value is None:
        return None

    if isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, dict):
        return {
            str(key): make_json_safe(item)
            for key, item in value.items()
        }

    if isinstance(value, (list, tuple, set)):
        return [
            make_json_safe(item)
            for item in value
        ]

    return str(value)


def main() -> None:
    raw_input = sys.stdin.read()

    if not raw_input.strip():
        raise ValueError("No input received.")

    payload = json.loads(raw_input)

    if not isinstance(payload, dict):
        raise TypeError(
            "Input payload must be a JSON object."
        )

    text = payload.get("text")

    if not isinstance(text, str):
        raise TypeError(
            "text must be a string."
        )

    result = process(text)

    print(
        json.dumps(
            make_json_safe(result),
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
