"""
Lexora AI
Quality Analyzer
"""


def generate_quality_report(

    duplicate_lines,

    language,

    noise,

    encoding

):

    score = 100

    score -= duplicate_lines

    score -= noise["noise_patterns"] * 2

    if not encoding["valid"]:

        score -= 25

    score = max(
        score,
        0
    )

    return {

        "quality_score":
            score,

        "encoding":
            encoding,

        "language":
            language,

        "duplicates_removed":
            duplicate_lines,

        "noise":
            noise

    }
