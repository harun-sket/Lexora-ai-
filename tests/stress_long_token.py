from __future__ import annotations

import time

from languages.tamil.unified_engine import process


CASES = [
    ("1K", "அ" * 1_000),
    ("10K", "அ" * 10_000),
    ("100K", "அ" * 100_000),
    ("500K", "அ" * 500_000),
    ("1M", "அ" * 1_000_000),
]


def main() -> None:
    print("=" * 90)
    print("LEXORA LONG TOKEN STRESS TEST")
    print("=" * 90)

    for name, text in CASES:
        print(f"\n🚀 STARTING {name} CHARACTER TOKEN TEST")

        start = time.perf_counter()

        try:
            result = process(text)
            elapsed = time.perf_counter() - start

            assert isinstance(result, dict)
            assert isinstance(result.get("tokens"), list)
            assert isinstance(result.get("analysis"), list)

            print(
                f"{name:6} | "
                f"chars={len(text):9,} | "
                f"time={elapsed:8.3f}s | "
                f"PASS 🟢"
            )

        except Exception as exc:
            elapsed = time.perf_counter() - start

            print(
                f"{name:6} | "
                f"chars={len(text):9,} | "
                f"time={elapsed:8.3f}s | "
                f"FAIL 🔴 | "
                f"{type(exc).__name__}: {exc}"
            )

    print("=" * 90)
    print("LONG TOKEN STRESS TEST COMPLETE")
    print("=" * 90)


if __name__ == "__main__":
    main()
