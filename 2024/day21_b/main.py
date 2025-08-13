from os import path

START = "A"
DEPTH = 26

# Instead of keeping track of an actual sequence,
# this time we treat it as (unordered) vectors.
# This means that the amount of different vectors is limited to X*X,
# where X is the number of buttons in the keypad.
# Then if a amount of occurences is stored allongside with each vector,
# we only have to calculate the next vectors for that specific vector once.
# We also have to keep track of the first key in the sequence,
# as the arm moves from 'A' to the start of the sequence at each new keypad.
# If this is not done, this movement will not be taken into account and thus
# result in a shorter sequence then it actually is.

def get_codes():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return [line.strip() for line in lines]


def find_shortest_path(position, to, positions):
    dx = to[0] - position[0]
    dy = to[1] - position[1]

    horizontal = ">" * abs(dx) if dx > 0 else "<" * abs(dx)
    vertical = "v" * abs(dy) if dy > 0 else "^" * abs(dy)

    if dx > 0 and (position[0], to[1]) in positions:
        return f"{vertical}{horizontal}"

    if (to[0], position[1]) in positions:
        return f"{horizontal}{vertical}"

    return f"{vertical}{horizontal}"

def get_keypad_map(keypad):
    positions = set(keypad.values())
    keypad_map = dict()

    for key_a, position_a in keypad.items():
        for key_b, position_b in keypad.items():
            keypad_map[f"{key_a}{key_b}"] = find_shortest_path(position_a, position_b, positions)

    return keypad_map

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

NUMERIC_KEYPAD_MAP = get_keypad_map(NUMERIC_KEYPAD)

def find_numeric_sequence_for(target):
    sequence = ""

    target = f"{START}{target}"

    for i in range(len(target) - 1):
        sequence += f"{NUMERIC_KEYPAD_MAP[target[i:(i+2)]]}A"

    return sequence

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

DIRECTIONAL_KEYPAD_MAP = get_keypad_map(DIRECTIONAL_KEYPAD)

def calculate_sequence_map_length(vectors):
    return sum(vectors.values()) + 1

def create_sequence_map_from(sequence):
    vectors = dict()

    head = sequence[0]

    for i in range(len(sequence) - 1):
        move = sequence[i:(i + 2)]
        vectors.setdefault(move, 0)
        vectors[move] += 1

    return head, vectors

def next_sequence_map(head, vectors):
    next_vectors = dict()

    head_sequence = f"{DIRECTIONAL_KEYPAD_MAP[f"{START}{head}"]}A"
    next_vectors = add_to_sequence_map(next_vectors, head_sequence)
    next_head = head_sequence[0]

    for move, amount in vectors.items():
        sequence = f"A{DIRECTIONAL_KEYPAD_MAP[move]}A"
        next_vectors = add_to_sequence_map(next_vectors, sequence, amount)

    return next_head, next_vectors

def add_to_sequence_map(vectors, sequence, amount = 1):
    for i in range(len(sequence) - 1):
        next_move = sequence[i:(i + 2)]
        vectors.setdefault(next_move, 0)
        vectors[next_move] += amount

    return vectors

def find_code_complexity(code):
    sequence = find_numeric_sequence_for(code)
    head, vectors = create_sequence_map_from(sequence)

    for _ in range(DEPTH - 1):
        head, vectors = next_sequence_map(head, vectors)

    complexity = calculate_sequence_map_length(vectors) * int(code[:-1])

    return complexity


def find_total_complexity(codes):
    return sum(find_code_complexity(code) for code in codes)


def main():
    codes = get_codes()

    total = find_total_complexity(codes)

    print(total)


if __name__ == "__main__":
    main()
