from pathlib import Path

from wordfreq import iter_wordlist, zipf_frequency


def main():
    output_dir = Path(__file__).parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "ta_frequency_dictionary.tsv"

    written = 0

    with output_file.open("w", encoding="utf-8") as f:

        f.write("word\tfrequency\tzipf\n")

        for word in iter_wordlist("ta", wordlist="best"):

            zipf = zipf_frequency(
                word,
                "ta",
                wordlist="best",
            )

            if zipf <= 0:
                continue

            frequency = max(
                int(10 ** zipf),
                1,
            )

            f.write(
                f"{word}\t{frequency}\t{zipf:.2f}\n"
            )

            written += 1

    print("=" * 60)
    print(f"Dictionary : {output_file}")
    print(f"Words      : {written}")
    print("=" * 60)


if __name__ == "__main__":
    main()
