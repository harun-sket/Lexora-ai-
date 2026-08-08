# Lexora V1.0 Hardening Report

## Overview

Lexora V1.0 underwent input-size stress testing to determine how
the unified language intelligence engine behaves under progressively
larger workloads.

The purpose of this testing was not to establish the public API limit
directly, but to identify the practical resource characteristics of
the engine and provide evidence for future API and infrastructure
limits.

---

# Input Stress Testing

## Medium Stress Test

| Words | Tokens | Input Size | Time | Peak Memory | Result |
|---:|---:|---:|---:|---:|:---:|
| 10,000 | 40,000 | 0.70 MB | 2.170 s | 27.72 MB | PASS |
| 25,000 | 100,000 | 1.74 MB | 3.601 s | 47.83 MB | PASS |
| 50,000 | 200,000 | 3.48 MB | 6.511 s | 95.70 MB | PASS |
| 75,000 | 300,000 | 5.22 MB | 9.969 s | 143.87 MB | PASS |
| 100,000 | 400,000 | 6.96 MB | 13.493 s | 191.48 MB | PASS |

## Large Stress Test

| Words | Tokens | Input Size | Time | Peak Memory | Result |
|---:|---:|---:|---:|---:|:---:|
| 250,000 | 1,000,000 | 17.40 MB | 17.777 s | 487.66 MB | PASS |
| 500,000 | 2,000,000 | 34.81 MB | 34.628 s | 958.69 MB | PASS |
| 1,000,000 | 4,000,000 | 69.62 MB | 69.432 s | 1,918.27 MB | PASS |

---

# Maximum Tested Workload

The largest successfully tested workload was:

- 1,000,000 words
- 4,000,000 tokens
- 69.62 MB input
- 69.432 seconds processing time
- 1,918.27 MB peak memory

Result: PASS.

This is the current Lexora single-request stress-test record.

---

# Scaling Observations

Processing time increased approximately linearly with token count
within the tested range.

Peak memory also increased approximately linearly.

---

# Production Safety Interpretation

The successful 1M-word test must NOT be interpreted as a recommended
public API request size.

A single 1M-word request consumed approximately 1.9 GB of peak memory
and required approximately 69 seconds.

Therefore the public API should enforce substantially smaller request
limits.

Potential controls include:

- maximum request size
- maximum token count
- maximum processing time
- request timeout
- concurrency limits
- per-user daily limits
- monthly usage limits
- request queueing
- memory/resource monitoring

---

# Current V1.0 Hardening Status

Core engine                 PASS
Frequency dictionary        PASS
POS                         PASS
NER                         PASS
Unified engine              PASS
Unified output contract     PASS
Medium input stress         PASS
Large input stress          PASS

Largest tested workload:

1,000,000 words / 4,000,000 tokens

Result:

PASS

---

# Important Limitation

These benchmarks demonstrate behavior in the test environment only.

They do not constitute a guarantee of production performance.

Production capacity depends on:

- CPU
- available RAM
- Python/runtime behavior
- deployment configuration
- concurrent requests
- infrastructure limits
- database/network overhead
- other running services

---

# Next Hardening Stage

After input-size testing, Lexora should be tested against:

1. Empty input
2. Whitespace-only input
3. Unicode edge cases
4. Combining characters
5. Zero-width characters
6. Emoji
7. Mixed scripts
8. Numbers
9. Punctuation-heavy input
10. Extremely long individual tokens
11. Invalid or unexpected input types
12. Concurrent requests
13. Repeated requests
14. Timeout behavior
15. API rate limiting

The objective is to convert every discovered weakness into a
regression test before the V1.0 release.
