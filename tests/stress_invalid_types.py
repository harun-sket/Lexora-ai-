from __future__ import annotations

from languages.tamil.unified_engine import process


CASES = [
    ("none", None),
    ("integer", 123),
    ("float", 123.45),
    ("boolean", True),
    ("list", ["தமிழ்"]),
    ("dict", {"text": "தமிழ்"}),
    ("tuple", ("தமிழ்",)),
    ("bytes", "தமிழ்".encode("utf-8")),
]


def main() -> None:
    print("=" * 90)
    print("LEXORA INVALID INPUT TYPE STRESS TEST")
    print("=" * 90)

    for name, value in CASES:
        print(f"\nCASE: {name}")
        print(f"TYPE: {type(value).__name__}")

        try:
            result = process(value)

            print("STATUS: ACCEPTED 🟢")
            print(f"OUTPUT TYPE: {type(result).__name__}")

        except Exception as exc:
            print("STATUS: REJECTED 🟢")
            print(f"ERROR TYPE: {type(exc).__name__}")
            print(f"ERROR: {exc}")

    print("=" * 90)
    print("INVALID INPUT TYPE TEST COMPLETE")
    print("=" * 90)


if __name__ == "__main__":
    main()
