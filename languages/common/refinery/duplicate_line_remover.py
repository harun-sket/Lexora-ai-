"""
Lexora AI

Duplicate Line Remover

Removes duplicate lines while preserving order.
"""

def remove_duplicate_lines(text: str) -> str:
    seen = set()
    cleaned = []

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            cleaned.append("")
            continue

        if stripped not in seen:
            seen.add(stripped)
            cleaned.append(line)

    return "\n".join(cleaned)
