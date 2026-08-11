from __future__ import annotations

import concurrent.futures
import time
import tracemalloc

from languages.tamil.unified_engine import process


INPUT = "தமிழ் ஒரு மொழி. Lexora AI 123 🔥 " * 1000

LEVELS = [2, 5, 10, 20]


def worker(_: int) -> tuple[bool, float, str]:
    start = time.perf_counter()

    try:
        result = process(INPUT)

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


def run_level(concurrency: int) -> None:
    print("=" * 90)
    print(f"🚀 STARTING {concurrency} CONCURRENT REQUESTS")
    print("=" * 90)

    tracemalloc.start()

    wall_start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=concurrency
    ) as executor:
        results = list(
            executor.map(worker, range(concurrency))
        )

    wall_time = time.perf_counter() - wall_start

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    passed = sum(result[0] for result in results)
    failed = concurrency - passed

    latencies = [result[1] for result in results]

    average = sum(latencies) / len(latencies)
    slowest = max(latencies)

    print(
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
    print("=" * 90)
    print("LEXORA CONCURRENCY STRESS TEST")
    print("=" * 90)

    for concurrency in LEVELS:
        run_level(concurrency)

    print("=" * 90)
    print("CONCURRENCY STRESS TEST COMPLETE")
    print("=" * 90)


if __name__ == "__main__":
    main()
