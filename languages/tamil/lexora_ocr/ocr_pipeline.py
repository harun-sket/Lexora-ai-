"""
Lexora AI
OCR Pipeline

IMAGE -> OCR -> TXT REFINERY -> CLEAN OUTPUT
"""

from pathlib import Path

from languages.tamil.lexora_ocr.ocr_engine import (
    process_image
)

from languages.tamil.lexora_txt_refinery.txt_cleaner import (
    refine_txt_file
)


def save_file(
    text,
    path
):

    output = Path(path)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    output.write_text(
        text,
        encoding="utf-8"
    )

    return str(output)


def run_ocr_pipeline(
    image_path: str
):

    # OCR
    ocr_result = process_image(
        image_path
    )

    raw_text = ocr_result[
        "extracted_text"
    ]


    # Save temporary OCR text
    temp_file = "storage/uploads/ocr_temp.txt"

    save_file(
        raw_text,
        temp_file
    )


    # Refinery
    clean_result = refine_txt_file(
        temp_file
    )


    # Save final clean output
    clean_output = save_file(
        clean_result["clean_text"],
        "storage/outputs/clean_output.txt"
    )


    # Save quality report
    report_output = save_file(
        str(clean_result["quality_report"]),
        "storage/outputs/quality_report.txt"
    )


    return {
        "raw_ocr": raw_text,
        "clean_output": clean_output,
        "quality_report": report_output
    }
