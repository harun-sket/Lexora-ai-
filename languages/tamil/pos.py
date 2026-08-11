from __future__ import annotations

from languages.tamil.frequency import lookup


def tag(token: str) -> str:
    token = token.strip()

    if not token:
        return "UNK"

    frequency = lookup(token)

    if isinstance(frequency, int) and frequency > 0:
        return "KNOWN"

    return "UNK"


__all__ = ["tag"]
