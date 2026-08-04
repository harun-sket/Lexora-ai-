"""
Lexora AI - Tamil Language Pack

Rules Engine v0.2

Safe text refinement without
destroying dataset structure.
"""


def clean_line(line: str) -> str:
    """
    Clean individual line.
    """

    return " ".join(
        line.strip().split()
    )


def remove_empty_lines(text: str) -> str:
    """
    Remove empty lines while
    preserving sentences.
    """

    lines = text.splitlines()

    cleaned = []

    for line in lines:
        line = clean_line(line)

        if line:
            cleaned.append(line)

    return "\n".join(cleaned)


def remove_duplicate_lines(text: str) -> str:
    """
    Remove duplicate lines.
    """

    lines = text.splitlines()

    seen = set()
    output = []

    for line in lines:

        if line not in seen:
            seen.add(line)
            output.append(line)

    return "\n".join(output)


def refine_text(text: str) -> str:
    """
    Complete refinement pipeline.
    """

    text = remove_empty_lines(text)

    text = remove_duplicate_lines(text)

    return text
