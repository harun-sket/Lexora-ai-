from __future__ import annotations

import sys
from pathlib import Path

# Add project root
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.normalize.normalizer import (
    TamilNormalizer,
    normalize_text,
)


def test_whitespace():
    assert normalize_text("  தமிழ்   மொழி  ") == "தமிழ் மொழி"


def test_zero_width():
    assert normalize_text("வணக்கம்\u200Bஉலகம்") == "வணக்கம்உலகம்"


def test_quotes():
    assert normalize_text("“தமிழ்”") == '"தமிழ்"'


def test_dash():
    assert normalize_text("தமிழ்—மொழி") == "தமிழ்-மொழி"


def test_ellipsis():
    assert normalize_text("தமிழ்…") == "தமிழ்..."


def test_nfc():
    normalizer = TamilNormalizer()
    text = "தமிழ்"
    assert normalizer.normalize(text) == text


def run():
    tests = [
        test_whitespace,
        test_zero_width,
        test_quotes,
        test_dash,
        test_ellipsis,
        test_nfc,
    ]

    passed = 0

    print("=" * 50)
    print("Running Tamil Normalizer Tests")
    print("=" * 50)

    for test in tests:
        try:
            test()
            print(f"✅ {test.__name__}")
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__}")
            print(e)

    print("=" * 50)
    print(f"Passed {passed}/{len(tests)} tests")
    print("=" * 50)

    if passed != len(tests):
        raise SystemExit(1)


if __name__ == "__main__":
    run()
