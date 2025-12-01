from os import path


def get_rotations():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        return [(line[0], int(line[1:])) for line in puzzle.readlines()]


def main():
    rotations = get_rotations()

    zero_count = count_dial_zero(rotations)

    print(zero_count)


def count_dial_zero(rotations: list[tuple[str, int]]):
    position = 50
    zero_count = 0

    for direction, amount in rotations:
        for _ in range(0, amount):
            move = 1 if direction == "R" else -1
            position += move
            position %= 100
            if position == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    main()
