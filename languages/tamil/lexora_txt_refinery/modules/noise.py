"""
Lexora AI
Noise Detector
"""

import re


def detect_noise(text: str):

    noise = len(
        re.findall(
            r"[#@%&*_=~^]{2,}",
            text
        )
    )

    return {

        "noise_patterns":
            noise

    }
