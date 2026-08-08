from __future__ import annotations

import gc
import time
import tracemalloc

from languages.tamil.unified_engine import process


CASES = [
    ("tiny", 10),
    ("small", 100),
    ("medium", 1_000),
    ("large", 10_000),
    ("xlarge", 50_000),
    ("huge", 100_000),
]


def build_text(words: int) -> str:
    sample = "தமிழ் இந்தியா சென்னை தம்பி "
    return sample * words


def run_case(name: str, words: int) -> None:
    text = build_text(words)

    characters = len(text)
    size_kb = len(text.encode("utf-8")) / 1024

    gc.collect()

    tracemalloc.start()
    start = time.perf_counter()

    try:
        result = process(text)

        elapsed = time.perf_counter() - start

        _, peak = tracemalloc.get_traced_memory()
        peak_mb = peak / (1024 * 1024)

        token_count = len(
            result.get("tokens", [])
        )

        print(
            f"{name:8} | "
            f"words={words:7,} | "
            f"chars={characters:9,} | "
            f"size={size_kb:9.2f} KB | "
            f"tokens={token_count:9,} | "
            f"time={elapsed:8.3f}s | "
            f"peak={peak_mb:8.2f} MB | "
            f"PASS 🟢"
        )

    except Exception as exc:
        elapsed = time.perf_counter() - start

        print(
            f"{name:8} | "
            f"words={words:7,} | "
            f"chars={characters:9,} | "
            f"size={size_kb:9.2f} KB | "
            f"time={elapsed:8.3f}s | "
            f"FAIL 🔴 | "
            f"{type(exc).__name__}: {exc}"
        )

    finally:
        tracemalloc.stop()
        gc.collect()


def main() -> None:
    print("=" * 120)
    print("LEXORA INPUT LIMIT STRESS TEST")
    print("=" * 120)

    print(
        "CASE     | "
        "WORDS   | "
        "CHARS     | "
        "SIZE       | "
        "TOKENS    | "
        "TIME     | "
        "PEAK MEM | STATUS"
    )

    print("-" * 120)

    for name, words in CASES:
        run_case(name, words)

    print("=" * 120)
    print("STRESS TEST COMPLETE")
    print("=" * 120)


if __name__ == "__main__":
    main()
