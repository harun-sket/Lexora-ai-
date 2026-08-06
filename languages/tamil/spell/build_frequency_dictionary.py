from pathlib import Path

from wordfreq import iter_wordlist, zipf_frequency


def main():
    output_dir = Path(__file__).parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "ta_frequency_dictionary.txt"

    written = 0

    with output_file.open("w", encoding="utf-8") as f:
        for word in iter_wordlist("ta"):
            score = zipf_frequency(word, "ta")

            if score <= 0:
                continue

            # Convert Zipf score into an integer frequency.
            frequency = int(10 ** score)

            if frequency < 1:
                frequency = 1

            f.write(f"{word} {frequency}\n")
            written += 1

    print("=" * 60)
    print(f"Dictionary written to: {output_file}")
    print(f"Words written: {written}")
    print("=" * 60)


if __name__ == "__main__":
    main()
