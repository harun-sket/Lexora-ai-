from pathlib import Path

from brain.router import route_file


def main():

    file_path = input(
        "Enter file path: "
    ).strip()

    result = route_file(
        file_path
    )

    print("\n========== RESULT ==========\n")

    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
