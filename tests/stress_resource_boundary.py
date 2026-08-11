from __future__ import annotations

import concurrent.futures
import time
import tracemalloc

from languages.tamil.unified_engine import process


BASE = "தமிழ் ஒரு மொழி. Lexora AI 123 🔥 "

# Approximately 250K words.
INPUT_250K = BASE * 25_000

# Approximately 500K words.
INPUT_500K = BASE * 50_000


LEVELS = [
    ("10x250K", 10, INPUT_250K),
    ("10x500K", 10, INPUT_500K),
    ("20x250K", 20, INPUT_250K),
]


def worker(text: str) -> tuple[bool, float, str]:
    start = time.perf_counter()

    try:
        result = process(text)

        elapsed = time.perf_counter() - start

        if not isinstance(result, dict):
            return False, elapsed, "output is not dict"

        if not isinstance(result.get("tokens"), list):
            return False, elapsed, "tokens is not list"

        if not isinstance(result.get("analysis"), list):
            return False, elapsed, "analysis is not list"

        return True, elapsed, ""

    except Exception as exc:
        elapsed = time.perf_counter() - start
        return False, elapsed, f"{type(exc).__name__}: {exc}"


def run_level(name: str, concurrency: int, text: str) -> None:
    print("=" * 100)
    print(f"🚀 STARTING {name}")
    print("=" * 100)

    tracemalloc.start()

    wall_start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=concurrency
    ) as executor:
        futures = [
            executor.submit(worker, text)
            for _ in range(concurrency)
        ]

        results = [future.result() for future in futures]

    wall_time = time.perf_counter() - wall_start

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    passed = sum(result[0] for result in results)
    failed = concurrency - passed

    latencies = [result[1] for result in results]

    average = sum(latencies) / len(latencies)
    slowest = max(latencies)

    print(
        f"LEVEL       : {name}\n"
        f"CONCURRENCY : {concurrency}\n"
        f"PASS        : {passed}\n"
        f"FAIL        : {failed}\n"
        f"WALL TIME   : {wall_time:.3f}s\n"
        f"AVG LATENCY : {average:.3f}s\n"
        f"SLOWEST     : {slowest:.3f}s\n"
        f"PEAK MEMORY : {peak_memory / (1024 * 1024):.2f} MB"
    )

    for index, (success, _, error) in enumerate(results):
        if not success:
            print(f"REQUEST {index}: FAIL — {error}")

    if failed == 0:
        print("STATUS      : PASS 🟢")
    else:
        print("STATUS      : FAIL 🔴")


def main() -> None:
    print("=" * 100)
    print("LEXORA RESOURCE BOUNDARY STRESS TEST — PHASE 3")
    print("=" * 100)

    for name, concurrency, text in LEVELS:
        run_level(name, concurrency, text)

    print("=" * 100)
    print("RESOURCE BOUNDARY STRESS TEST COMPLETE")
    print("=" * 100)


if __name__ == "__main__":
    main()
