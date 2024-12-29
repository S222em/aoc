#!/usr/bin/env python3
import os.path
import sys


def main():
    year = sys.argv[1]

    directory = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(directory, "template.py")) as file:
        template = file.read()

    for i in range(1, 26):
        parts = ("a", "b") if i < 25 else ("a",)

        for part in parts:
            day_directory = os.path.join(directory, year, f"day{i}_{part}")

            if os.path.exists(day_directory):
                continue

            os.makedirs(day_directory)
            open(os.path.join(day_directory, "puzzle.txt"), "w").close()
            with open(os.path.join(day_directory, "main.py"), "w") as file:
                file.write(template)


if __name__ == "__main__":
    main()
