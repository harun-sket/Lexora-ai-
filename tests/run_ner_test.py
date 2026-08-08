from languages.tamil.ner import analyze


def main():
    words = [
        "இந்தியா",
        "தமிழ்நாடு",
        "சென்னை",
        "மதுரை",
        "தமிழ்",
        "தம்பி",
        "OpenAI",
    ]

    print("=" * 60)
    print("LEXORA NER TEST")
    print("=" * 60)

    for word in words:
        result = analyze(word)

        print(
            f"{word} -> "
            f"known={result['known']} | "
            f"frequency={result['frequency']} | "
            f"entity={result['entity']}"
        )

    print("=" * 60)


if __name__ == "__main__":
    main()
