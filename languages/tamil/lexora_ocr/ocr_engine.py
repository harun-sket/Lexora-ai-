"""
Lexora AI OCR Engine

Provider: OCR Tamil
"""

from languages.tamil.lexora_ocr.providers.ocr_tamil_provider import (
    extract_text,
)


def process_image(image_path: str):
    """
    Process an image using the OCR Tamil provider.
    """

    text = extract_text(image_path)

    return {
        "raw_ocr": text,
        "provider": "ocr_tamil",
        "image": image_path,
    }


def save_text(text: str, output_path: str):
    """
    Save OCR text to a UTF-8 text file.
    """

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(text)

    return output_path
