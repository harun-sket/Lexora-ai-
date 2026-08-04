"""
Lexora AI - Tamil Language Pack

Quality Engine v0.1

Generates quality reports for refined data.
"""


def calculate_text_quality(
    original_text: str,
    cleaned_text: str
) -> dict:
    """
    Calculate basic text quality metrics.
    """

    original_lines = len(
        original_text.splitlines()
    )

    cleaned_lines = len(
        cleaned_text.splitlines()
    )

    removed_lines = (
        original_lines - cleaned_lines
    )

    score = 100

    if removed_lines > 0:
        score -= min(
            removed_lines,
            20
        )

    if len(cleaned_text.strip()) == 0:
        score = 0

    return {
        "quality_score": score,
        "original_lines": original_lines,
        "cleaned_lines": cleaned_lines,
        "removed_lines": removed_lines
    }


def generate_dataset_report(
    total_records: int,
    cleaned_records: int,
    removed_records: int
) -> dict:
    """
    Generate dataset quality report.
    """

    score = 100

    if total_records > 0:
        removal_rate = (
            removed_records / total_records
        ) * 100

        score -= min(
            int(removal_rate),
            30
        )

    return {
        "total_records": total_records,
        "cleaned_records": cleaned_records,
        "removed_records": removed_records,
        "quality_score": score
    }
