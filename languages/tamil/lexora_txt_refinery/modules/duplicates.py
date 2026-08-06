"""
Lexora AI
Duplicate Line Remover
"""


def remove_duplicates(text: str):

    seen = set()

    output = []

    removed = 0

    for line in text.splitlines():

        clean = line.strip()

        if not clean:
            continue

        if clean not in seen:

            seen.add(clean)

            output.append(clean)

        else:

            removed += 1

    return "\n".join(output), removed
