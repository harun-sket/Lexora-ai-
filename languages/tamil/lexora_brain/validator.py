"""
Lexora AI - Tamil Language Pack

Validator Module v0.1

Checks if refined data meets
basic quality requirements.
"""


def validate_text(text: str) -> dict:
    """
    Validate refined text data.
    """

    result = {
        "is_valid": True,
        "issues": []
    }

    if not text:
        result["is_valid"] = False
        result["issues"].append(
            "Text is empty"
        )

    if len(text.strip()) < 5:
        result["is_valid"] = False
        result["issues"].append(
            "Text is too short"
        )

    return result


def validate_json_records(records: list) -> dict:
    """
    Validate JSON dataset records.
    """

    result = {
        "is_valid": True,
        "issues": []
    }

    if not records:
        result["is_valid"] = False
        result["issues"].append(
            "Dataset contains no records"
        )

    for index, record in enumerate(records):

        if not isinstance(record, dict):
            result["is_valid"] = False
            result["issues"].append(
                f"Record {index} is not an object"
            )

    return result
