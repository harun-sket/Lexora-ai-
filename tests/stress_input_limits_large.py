from __future__ import annotations

import gc
import time
import tracemalloc

from languages.tamil.unified_engine import process


CASES = [
    ("250K", 250_000),
    ("500K", 500_000),
    ("1M", 1_000_000),
]


def build_text(words: int) -> str:
    sample = "தமிழ் இந்தியா சென்னை தம்பி "
    return sample * words


def run_case(name: str, words: int) -> None:
    print(f"\n🚀 STARTING {name} WORD TEST")

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
            f"words={words:10,} | "
            f"size={size_mb:10.2f} MB | "
            f"tokens={tokens:10,} | "
            f"time={elapsed:10.3f}s | "
            f"peak={peak_mb:10.2f} MB | "
            f"PASS 🟢"
        )

    except Exception as exc:
        elapsed = time.perf_counter() - start

        print(
            f"{name:6} | "
            f"words={words:10,} | "
            f"size={size_mb:10.2f} MB | "
            f"time={elapsed:10.3f}s | "
            f"FAIL 🔴 | "
            f"{type(exc).__name__}: {exc}"
        )

    finally:
        tracemalloc.stop()
        gc.collect()


def main() -> None:
    print("=" * 120)
    print("LEXORA LARGE INPUT STRESS TEST")
    print("=" * 120)

    for name, words in CASES:
        run_case(name, words)

    print("\n" + "=" * 120)
    print("LARGE STRESS TEST COMPLETE")
    print("=" * 120)


if __name__ == "__main__":
    main()
