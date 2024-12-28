START = "A"
DEPTH = 3


def get_codes():
    with open("puzzle.txt") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


def find_sequence_for(keypad, target):
    positions = set(keypad.values())

    i = 0
    x, y = keypad[START]
    char = ""
    sequence = ""

    while i < len(target):
        tx, ty = keypad[target[i]]
        dx = tx - x
        dy = ty - y

        if dx == 0 and dy == 0:
            sequence += "A"
            i += 1
            continue

        x_possible = dx != 0 and (x + dx, y) in positions
        # y_preferred = dy != 0 and (x, y + dy) in positions and ((dy < 0 and char == "^") or (dy > 0 and char == "v"))

        if x_possible:
            # Move along the x-axis
            char = ">" if dx > 0 else "<"
            sequence += char * abs(dx)
            x += dx

        # Move along the y-axis
        char = "v" if dy > 0 else "^"
        sequence += char * abs(dy)
        y += dy

    return sequence


# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
NUMERIC_KEYPAD = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3)
}


def find_numeric_sequence_for(sequence):
    return find_sequence_for(NUMERIC_KEYPAD, sequence)


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
DIRECTIONAL_KEYPAD = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def find_directional_sequence_for(sequence):
    return find_sequence_for(DIRECTIONAL_KEYPAD, sequence)


def find_code_complexity(code):
    sequence = find_numeric_sequence_for(code)
    print(code)
    print(sequence)

    for _ in range(DEPTH - 1):
        sequence = find_directional_sequence_for(sequence)
        print(sequence)

    print("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")

    complexity = len(sequence) * int(code[:-1])

    return complexity


def find_total_complexity(codes):
    return sum(find_code_complexity(code) for code in codes)


def main():
    codes = get_codes()

    total = find_total_complexity(codes)

    print(total)


if __name__ == "__main__":
    main()
