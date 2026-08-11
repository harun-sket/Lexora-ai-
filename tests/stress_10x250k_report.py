from __future__ import annotations

import concurrent.futures
import time
import tracemalloc
from pathlib import Path

from languages.tamil.unified_engine import process


CONCURRENCY = 10
WORD_TARGET = 250_000

BASE = "தமிழ் ஒரு மொழி. Lexora AI 123 🔥 "
INPUT = BASE * WORD_TARGET

REPORT = (
    Path(__file__).resolve().parent
    / "10x250k_stress_report.txt"
)


def worker(_: int) -> tuple[bool, float, int, str]:
    start = time.perf_counter()

    try:
        result = process(INPUT)
        elapsed = time.perf_counter() - start

        if not isinstance(result, dict):
            return False, elapsed, 0, "output is not dict"

        if not isinstance(result.get("tokens"), list):
            return False, elapsed, 0, "tokens is not list"

        if not isinstance(result.get("analysis"), list):
            return False, elapsed, 0, "analysis is not list"

        return True, elapsed, len(result["tokens"]), ""

    except Exception as exc:
        elapsed = time.perf_counter() - start
        return False, elapsed, 0, f"{type(exc).__name__}: {exc}"


def main() -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    tracemalloc.start()

    wall_start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=CONCURRENCY
    ) as executor:
        results = list(
            executor.map(worker, range(CONCURRENCY))
        )

    wall_time = time.perf_counter() - wall_start

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    passed = sum(result[0] for result in results)
    failed = CONCURRENCY - passed

    latencies = [result[1] for result in results]

    average_latency = sum(latencies) / len(latencies)
    slowest_latency = max(latencies)

    token_counts = [result[2] for result in results]
    average_tokens = sum(token_counts) / len(token_counts)

    status = "PASS" if failed == 0 else "FAIL"

    report = f"""
================================================================================
LEXORA 10 × 250K CONCURRENCY STRESS TEST
================================================================================

TEST CONFIGURATION
--------------------------------------------------------------------------------
Concurrent requests : {CONCURRENCY}
Target words/request : {WORD_TARGET:,}
Input characters     : {len(INPUT):,}

RESULTS
--------------------------------------------------------------------------------
Passed requests      : {passed}
Failed requests      : {failed}
Average tokens       : {average_tokens:,.0f}

Wall time            : {wall_time:.3f} s
Average latency      : {average_latency:.3f} s
Slowest request      : {slowest_latency:.3f} s
Peak traced memory   : {peak_memory / (1024 * 1024):.2f} MB

STATUS
--------------------------------------------------------------------------------
{status}

REQUEST DETAILS
--------------------------------------------------------------------------------
"""

    for index, (success, elapsed, tokens, error) in enumerate(results, 1):
        request_status = "PASS" if success else "FAIL"

        report += (
            f"Request {index:02d} | "
            f"{request_status:4} | "
            f"time={elapsed:.3f}s | "
            f"tokens={tokens:,}"
        )

        if error:
            report += f" | error={error}"

        report += "\n"

    report += """
================================================================================
END OF REPORT
================================================================================
"""

    REPORT.write_text(report, encoding="utf-8")

    print(report)
    print(f"Report saved to: {REPORT}")


if __name__ == "__main__":
    main()
