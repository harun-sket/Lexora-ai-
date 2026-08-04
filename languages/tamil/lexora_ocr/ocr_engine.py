"""
Lexora AI
Tamil OCR Engine v0.2

Image preprocessing + Tamil OCR
"""

from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract


def preprocess_image(image_path):

    image = Image.open(
        image_path
    )

    # Convert to grayscale
    image = image.convert(
        "L"
    )

    # Increase contrast
    image = ImageEnhance.Contrast(
        image
    ).enhance(2)

    # Sharpen text
    image = image.filter(
        ImageFilter.SHARPEN
    )

    return image


def process_image(
    image_path: str
):

    image = preprocess_image(
        image_path
    )

    config = "--psm 6"

    text = pytesseract.image_to_string(
        image,
        lang="tam+eng",
        config=config
    )

    return {
        "source_image": image_path,
        "extracted_text": text.strip(),
        "character_count": len(text.strip())
    }


def save_text(
    text,
    output_path
):

    path = Path(
        output_path
    )

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        text,
        encoding="utf-8"
    )

    return path
