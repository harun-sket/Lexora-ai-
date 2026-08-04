"""
Lexora AI
Main Command Center v0.3

Automatic routing + unique outputs
"""

import sys
import json
from pathlib import Path

from languages.tamil.lexora_brain.detector import (
    detect_file_type
)

from languages.tamil.lexora_txt_refinery.txt_cleaner import (
    refine_txt_file
)

from languages.tamil.lexora_json_refinery.json_cleaner import (
    refine_json_file
)

from languages.tamil.lexora_output_generator.json_output import (
    save_json_output
)

from core.file_manager import (
    get_unique_filename
)


OUTPUT_DIR = "storage/outputs"
REPORT_DIR = "reports"


def save_txt_output(
    content: str
):
    """
    Save TXT with unique name.
    """

    output_path = get_unique_filename(
        OUTPUT_DIR,
        "clean_output.txt"
    )

    output_path.write_text(
        content,
        encoding="utf-8"
    )

    return output_path


def save_report(
    report: dict
):
    """
    Save quality report with unique name.
    """

    report_path = get_unique_filename(
        REPORT_DIR,
        "quality_report.json"
    )

    report_path.write_text(
        json.dumps(
            report,
            indent=4,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    return report_path


def run_lexora(
    file_path: str
):

    print("\n===== LEXORA AI v0.3 =====\n")

    print(
        "Input:",
        file_path
    )


    file_type = detect_file_type(
        file_path
    )

    print(
        "Detected:",
        file_type
    )


    if file_type == "TXT":

        print(
            "\nRunning TXT Refinery..."
        )

        result = refine_txt_file(
            file_path
        )

        output = save_txt_output(
            result["clean_text"]
        )

        report = save_report(
            result["quality_report"]
        )


    elif file_type == "JSON":

        print(
            "\nRunning JSON Refinery..."
        )

        result = refine_json_file(
            file_path
        )

        output = get_unique_filename(
            OUTPUT_DIR,
            "clean_output.json"
        )

        save_json_output(
            result["clean_data"],
            str(output)
        )

        report = save_report(
            result["quality_report"]
        )


    else:

        print(
            "Unsupported file type"
        )

        return


    print("\n✓ Refinement Complete")

    print(
        "Clean Output:",
        output
    )

    print(
        "Quality Report:",
        report
    )


if __name__ == "__main__":

    if len(sys.argv) < 2:

        print(
            "Usage: python lexora.py <file>"
        )

        sys.exit(1)


    run_lexora(
        sys.argv[1]
    )
