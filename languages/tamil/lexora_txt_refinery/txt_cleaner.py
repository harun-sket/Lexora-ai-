"""
Lexora AI
Tamil TXT Refinery

Production Pipeline

File
 ↓
Encoding Validation
 ↓
Unicode Normalization
 ↓
Control Character Removal
 ↓
Whitespace Cleaning
 ↓
Duplicate Removal
 ↓
Language Analysis
 ↓
Noise Detection
 ↓
Quality Report
"""

from pathlib import Path

from languages.tamil.lexora_txt_refinery.modules.encoding import (
    validate_encoding
)

from languages.tamil.lexora_txt_refinery.modules.unicode_normalizer import (
    normalize_unicode
)

from languages.tamil.lexora_txt_refinery.modules.control_chars import (
    remove_control_characters
)

from languages.tamil.lexora_txt_refinery.modules.whitespace import (
    clean_whitespace
)

from languages.tamil.lexora_txt_refinery.modules.duplicates import (
    remove_duplicates
)

from languages.tamil.lexora_txt_refinery.modules.language_validator import (
    analyze_language
)

from languages.tamil.lexora_txt_refinery.modules.noise import (
    detect_noise
)

from languages.tamil.lexora_txt_refinery.modules.quality import (
    generate_quality_report
)


def refine_txt_file(
    file_path: str
):

    encoding_report = validate_encoding(
        file_path
    )

    text = Path(
        file_path
    ).read_text(
        encoding="utf-8"
    )

    text = normalize_unicode(
        text
    )

    text = remove_control_characters(
        text
    )

    text = clean_whitespace(
        text
    )

    clean_text, duplicates_removed = remove_duplicates(
        text
    )

    language = analyze_language(
        clean_text
    )

    noise = detect_noise(
        clean_text
    )

    quality = generate_quality_report(

        duplicate_lines=duplicates_removed,

        language=language,

        noise=noise,

        encoding=encoding_report

    )

    output_dir = Path(
        "storage/outputs"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = output_dir / "clean_output.txt"

    report_file = output_dir / "quality_report.txt"

    output_file.write_text(

        clean_text,

        encoding="utf-8"

    )

    report_lines = [

        "LEXORA AI QUALITY REPORT",
        "=" * 40,
        "",
        f"Encoding           : {encoding_report['encoding']}",
        f"Encoding Valid     : {encoding_report['valid']}",
        f"Duplicates Removed : {duplicates_removed}",
        f"Noise Patterns     : {noise['noise_patterns']}",
        "",
        "Language Analysis",
        "-" * 20,
        f"Tamil    : {language['tamil_percent']}%",
        f"English  : {language['english_percent']}%",
        f"Digits   : {language['digit_percent']}%",
        "",
        f"Quality Score : {quality['quality_score']}%"
    ]

    report_file.write_text(

        "\n".join(report_lines),

        encoding="utf-8"

    )

    return {

        "clean_text":
            clean_text,

        "validation":
            encoding_report,

        "quality_report":
            quality,

        "output_file":
            str(output_file),

        "report_file":
            str(report_file)

    }
