from languages.tamil.pos import tag


def main():
    words = [
        "தமிழ்",
        "மொழி",
        "நான்",
        "நீ",
        "ஒரு",
        "மற்றும்",
        "சென்னை",
        "OpenAI",
    ]

    print("=" * 60)
    print("LEXORA POS TEST")
    print("=" * 60)

    for word in words:
        print(f"{word} -> {tag(word)}")

    print("=" * 60)


if __name__ == "__main__":
    main()
