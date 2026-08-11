from __future__ import annotations

import time

from languages.tamil.unified_engine import process


CASES = [
    ("tamil_repeat_10k", "தமிழ் " * 10_000),
    ("tamil_repeat_100k", "தமிழ் " * 100_000),
    ("punct_repeat_100k", "!!!???... " * 100_000),
    ("emoji_repeat_100k", "🔥🚀🗿 " * 100_000),
    ("mixed_repeat_100k", "தமிழ்123🔥!!! " * 100_000),
    ("single_char_1m", "அ" * 1_000_000),
    ("alternating_1m", ("அஆ" * 500_000)),
]


def run_case(name: str, text: str) -> None:
    start = time.perf_counter()

    try:
        result = process(text)
        elapsed = time.perf_counter() - start

        assert isinstance(result, dict)
        assert isinstance(result.get("tokens"), list)
        assert isinstance(result.get("analysis"), list)

        print(
            f"{name:22} | "
            f"chars={len(text):10,} | "
            f"time={elapsed:9.3f}s | "
            f"tokens={len(result['tokens']):10,} | "
            f"PASS 🟢"
        )

    except Exception as exc:
        elapsed = time.perf_counter() - start

        print(
            f"{name:22} | "
            f"chars={len(text):10,} | "
            f"time={elapsed:9.3f}s | "
            f"FAIL 🔴 | "
            f"{type(exc).__name__}: {exc}"
        )


def main() -> None:
    print("=" * 110)
    print("LEXORA PATHOLOGICAL INPUT STRESS TEST")
    print("=" * 110)

    for name, text in CASES:
        print(f"\n🚀 STARTING {name}")
        run_case(name, text)

    print("=" * 110)
    print("PATHOLOGICAL INPUT STRESS TEST COMPLETE")
    print("=" * 110)


if __name__ == "__main__":
    main()
