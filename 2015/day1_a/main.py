def get_instructions():
    """
    Returns all instructions in the puzzle
    :return:
    """
    with open("puzzle.txt") as puzzle:
        instructions = puzzle.read()

    return instructions.strip()


def find_floor(instructions):
    """
    Finds the floor that the instructions lead to
    :param instructions:
    :return:
    """
    return sum(1 if instruction == "(" else -1 for instruction in instructions)


def main():
    instructions = get_instructions()

    floor = find_floor(instructions)

    print(floor)


if __name__ == "__main__":
    main()
