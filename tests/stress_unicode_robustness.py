from __future__ import annotations

from languages.tamil.unified_engine import process


CASES = [
    ("tamil", "தமிழ்"),
    ("tamil_sentence", "தமிழ் ஒரு அழகான மொழி"),
    ("mixed_english", "தமிழ் Tamil Lexora"),
    ("mixed_scripts", "தமிழ் English 日本語 العربية हिन्दी"),
    ("emoji", "🔥 🚀 🗿 ❤️ 😂"),
    ("numbers", "123 456 789 2026"),
    ("punctuation", "!!! ??? ... ,,, ;; :::"),
    ("combining", "த்\u200dமிழ்"),
    ("zero_width", "தமிழ்\u200bதமிழ்"),
    ("mixed_everything", "தமிழ் Lexora 123 🔥 日本語 العربية !!!"),
]


def main() -> None:
    print("=" * 70)
    print("LEXORA UNICODE ROBUSTNESS TEST")
    print("=" * 70)

    for name, text in CASES:
        print("=" * 70)
        print(f"CASE: {name}")
        print(f"INPUT: {repr(text)}")

        try:
            result = process(text)

            assert isinstance(result, dict)
            assert isinstance(result.get("tokens"), list)
            assert isinstance(result.get("analysis"), list)

            print("STATUS: PASS")
            print(f"OUTPUT: {result}")

        except Exception as exc:
            print("STATUS: FAIL")
            print(f"ERROR TYPE: {type(exc).__name__}")
            print(f"ERROR: {exc}")

    print("=" * 70)
    print("UNICODE ROBUSTNESS TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
