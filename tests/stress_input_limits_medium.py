from __future__ import annotations

import gc
import time
import tracemalloc

from languages.tamil.unified_engine import process


CASES = [
    ("10K", 10_000),
    ("25K", 25_000),
    ("50K", 50_000),
    ("75K", 75_000),
    ("100K", 100_000),
]


def build_text(words: int) -> str:
    sample = "தமிழ் இந்தியா சென்னை தம்பி "
    return sample * words


def run_case(name: str, words: int) -> None:
    text = build_text(words)

    size_mb = len(text.encode("utf-8")) / (1024 * 1024)

    gc.collect()
    tracemalloc.start()

    start = time.perf_counter()

    try:
        result = process(text)

        elapsed = time.perf_counter() - start

        _, peak = tracemalloc.get_traced_memory()
        peak_mb = peak / (1024 * 1024)

        tokens = len(result.get("tokens", []))

        print(
            f"{name:6} | "
            f"words={words:7,} | "
            f"size={size_mb:8.2f} MB | "
            f"tokens={tokens:9,} | "
            f"time={elapsed:7.3f}s | "
            f"peak={peak_mb:8.2f} MB | "
            f"PASS 🟢"
        )

    except Exception as exc:
        elapsed = time.perf_counter() - start

        print(
            f"{name:6} | "
            f"words={words:7,} | "
            f"size={size_mb:8.2f} MB | "
            f"time={elapsed:7.3f}s | "
            f"FAIL 🔴 | "
            f"{type(exc).__name__}: {exc}"
        )

    finally:
        tracemalloc.stop()
        gc.collect()


def main() -> None:
    print("=" * 100)
    print("LEXORA MEDIUM INPUT STRESS TEST")
    print("=" * 100)

    print(
        "CASE   | WORDS   | SIZE     | TOKENS    | TIME    | PEAK MEM | STATUS"
    )
    print("-" * 100)

    for name, words in CASES:
        run_case(name, words)

    print("=" * 100)
    print("MEDIUM STRESS TEST COMPLETE")
    print("=" * 100)


if __name__ == "__main__":
    main()
