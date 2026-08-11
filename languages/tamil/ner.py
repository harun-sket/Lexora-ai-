from __future__ import annotations

from languages.tamil.frequency import lookup


def analyze(token: str) -> dict[str, object]:
    frequency = lookup(token)

    return {
        "known": frequency > 0,
        "frequency": frequency,
        "entity": "KNOWN" if frequency > 0 else "NONE",
    }


__all__ = ["analyze"]
