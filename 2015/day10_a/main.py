from os import path

ITERATIONS = 40

def get_digits():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        digits = puzzle.read().strip()

    return digits

def next_sequence(digits):
    sequence = ""
    last_seen = None
    count = 0

    for char in digits:
        if last_seen is None or char == last_seen:
            last_seen = char
            count += 1
            continue

        sequence += f"{count}{last_seen}"

        last_seen = char
        count = 1

    sequence += f"{count}{last_seen}"

    return sequence

def get_length_of_sequence(digits):
    sequence = digits

    for i in range(ITERATIONS):
        sequence = next_sequence(sequence)

    return len(sequence)

def main():
    digits = get_digits()

    length = get_length_of_sequence(digits)

    print(length)


if __name__ == "__main__":
    main()
