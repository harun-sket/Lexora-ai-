from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from languages.tamil.tokenize.tokenizer import tokenize


def test_simple():
    assert tokenize("தமிழ் மொழி") == [
        "தமிழ்",
        "மொழி",
    ]


def test_punctuation():
    assert tokenize("வணக்கம், உலகம்!") == [
        "வணக்கம்",
        ",",
        "உலகம்",
        "!",
    ]


def test_numbers():
    assert tokenize("2026 தமிழ்") == [
        "2026",
        "தமிழ்",
    ]


def test_english():
    assert tokenize("Lexora தமிழ் AI") == [
        "Lexora",
        "தமிழ்",
        "AI",
    ]


def test_empty():
    assert tokenize("") == []


def test_spaces():
    assert tokenize("   தமிழ்     மொழி   ") == [
        "தமிழ்",
        "மொழி",
    ]


def run():
    tests = [
        test_simple,
        test_punctuation,
        test_numbers,
        test_english,
        test_empty,
        test_spaces,
    ]

    passed = 0

    print("=" * 50)
    print("Running Tamil Tokenizer Tests")
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
