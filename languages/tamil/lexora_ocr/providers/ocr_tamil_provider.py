"""
Lexora AI

Tamil OCR Provider

Uses OCR Tamil.

OCR Tamil
Copyright (c) 2024 Gnana Prasath

Licensed under the MIT License.
"""

from ocr_tamil.ocr import OCR

_ocr = OCR()


def extract_text(image_path: str) -> str:
    prediction = _ocr.predict(image_path)

    if not prediction:
        return ""

    first = prediction[0]

    if isinstance(first, list):
        return " ".join(str(x) for x in first)

    return str(first)
