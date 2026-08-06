"""
Lexora Tamil Frequency Dictionary Builder

Builds a SymSpell-compatible Tamil frequency dictionary
using the wordfreq dataset.
"""

from pathlib import Path
from wordfreq import top_n_list, zipf_frequency

OUTPUT = Path(
    "languages/common/spelling/dictionaries/lexora_tamil_frequency.txt"
)


def zipf_to_count(zipf: float) -> int:
    """
    Convert Zipf score to an approximate integer frequency.

    SymSpell expects:
        word frequency

    The exact value isn't important.
    Relative ordering is.
    """
    return max(1, int(10 ** zipf))


def build_dictionary(limit: int = 500000):
    print("========================================")
    print(" Lexora Tamil Dictionary Builder")
    print("========================================")
    print()

    print("Loading Tamil vocabulary...")

    words = top_n_list("ta", limit)

    print(f"Loaded {len(words):,} words")
    print()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    written = 0

    with OUTPUT.open("w", encoding="utf-8") as f:
        for word in words:
            score = zipf_frequency(word, "ta")

            if score <= 0:
                continue

            frequency = zipf_to_count(score)

            f.write(f"{word} {frequency}\n")
            written += 1

    print("Dictionary created successfully!")
    print(f"Words written : {written:,}")
    print(f"Output        : {OUTPUT}")


if __name__ == "__main__":
    build_dictionary()
