START = "A"
DEPTH = 26


def get_codes():
    """
    Gets all the codes from the puzzle
    :return:
    """
    with open("puzzle.txt") as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


def find_shortest_path(position, to, positions):
    """
    Finds the shortest path between the current position and target.
    Prevents moving on any position not in positions.
    Also makes sure that the shortest possible sequence is given.
    :param position:
    :param to:
    :param positions:
    :return:
    """
    dx = to[0] - position[0]
    dy = to[1] - position[1]

    horizontal = ">" * abs(dx) if dx > 0 else "<" * abs(dx)
    vertical = "v" * abs(dy) if dy > 0 else "^" * abs(dy)

    if dx > 0 and (position[0], to[1]) in positions:
        return f"{vertical}{horizontal}A"

    if (to[0], position[1]) in positions:
        return f"{horizontal}{vertical}A"

    return f"{vertical}{horizontal}A"


def find_sequence_for(keypad, target):
    """
    Finds the shortest sequence to enter the target sequence on the given keypad
    :param keypad:
    :param target:
    :return:
    """
    positions = set(keypad.values())

    x, y = keypad[START]
    sequence = ""

    for char in target:
        tx, ty = keypad[char]

        sequence += find_shortest_path((x, y), (tx, ty), positions)

        x, y = tx, ty

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


def find_numeric_sequence_for(target):
    """
    Finds the shortest sequence to enter the target sequence on the given keypad
    :param target:
    :return:
    """
    return find_sequence_for(NUMERIC_KEYPAD, target)


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


def find_directional_sequence_for(target):
    """
    Finds the shortest sequence to enter the target sequence on the given keypad
    :param target:
    :return:
    """
    return find_sequence_for(DIRECTIONAL_KEYPAD, target)


def find_code_complexity(code, directions, depth):
    """
    Finds a codes total complexity for the given depth
    :param code:
    :param depth:
    :return:
    """
    sequence = find_numeric_sequence_for(code)

    for _ in range(depth - 1):
        sequence = find_directional_sequence_for(sequence)

    complexity = len(sequence) * int(code[:-1])

    return complexity


def find_total_complexity(codes, depth):
    """
    Finds the sum of all codes complexity for the given depth
    :param codes:
    :param depth:
    :return:
    """
    return sum(find_code_complexity(code, depth) for code in codes)


def main():
    codes = get_codes()

    total = find_total_complexity(codes, DEPTH)

    print(total)


if __name__ == "__main__":
    main()
