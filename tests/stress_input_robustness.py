from __future__ import annotations

from languages.tamil.unified_engine import process


def run_case(name: str, text: str) -> None:
    print("=" * 70)
    print(f"CASE: {name}")
    print(f"INPUT: {repr(text)}")

    try:
        result = process(text)

        print("STATUS: PASS")
        print(f"OUTPUT TYPE: {type(result).__name__}")
        print(f"OUTPUT: {result}")

    except Exception as exc:
        print("STATUS: FAIL")
        print(f"ERROR TYPE: {type(exc).__name__}")
        print(f"ERROR: {exc}")


def main() -> None:
    cases = [
        ("empty", ""),
        ("space", " "),
        ("spaces", "     "),
        ("newline", "\n"),
        ("tabs", "\t\t\t"),
        ("mixed whitespace", " \n\t  \n "),
    ]

    print("=" * 70)
    print("LEXORA INPUT ROBUSTNESS TEST")
    print("=" * 70)

    for name, text in cases:
        run_case(name, text)

    print("=" * 70)
    print("ROBUSTNESS TEST COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()
