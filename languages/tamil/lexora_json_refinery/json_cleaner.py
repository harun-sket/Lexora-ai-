"""
Lexora AI - Tamil Language Pack

JSON Refinery v0.1

Processes raw JSON datasets and creates
clean AI-ready JSON data.
"""

import json
from pathlib import Path


def clean_text(text: str) -> str:
    """
    Clean text fields safely.
    """

    return " ".join(
        text.strip().split()
    )


def remove_empty_records(records: list) -> list:
    """
    Remove empty JSON objects.
    """

    cleaned = []

    for record in records:

        if isinstance(record, dict) and record:
            cleaned.append(record)

    return cleaned


def remove_duplicate_records(records: list) -> list:
    """
    Remove duplicate JSON records.
    """

    seen = set()
    cleaned = []

    for record in records:

        fingerprint = json.dumps(
            record,
            sort_keys=True,
            ensure_ascii=False
        )

        if fingerprint not in seen:
            seen.add(fingerprint)
            cleaned.append(record)

    return cleaned


def clean_text_fields(records: list) -> list:
    """
    Clean all string values.
    """

    for record in records:

        for key, value in record.items():

            if isinstance(value, str):
                record[key] = clean_text(value)

    return records


def refine_json_file(file_path: str) -> dict:
    """
    Complete JSON refinement pipeline.
    """

    path = Path(file_path)

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        records = json.load(file)


    original_count = len(records)


    records = remove_empty_records(records)

    records = remove_duplicate_records(records)

    records = clean_text_fields(records)


    return {
        "clean_data": records,
        "quality_report": {
            "original_records": original_count,
            "clean_records": len(records),
            "removed_records":
                original_count - len(records)
        }
    }
