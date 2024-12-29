def get_instructions():
    """
    Returns all instructions in the puzzle
    :return:
    """
    with open("puzzle.txt") as puzzle:
        instructions = puzzle.read()

    return instructions.strip()


def find_basement_enter_position(instructions):
    """
    Finds the position at which the basement is entered.
    The first instruction has position 1.
    :param instructions:
    :return:
    """
    floor = 0

    for i, instruction in enumerate(instructions):
        floor += 1 if instruction == "(" else -1

        if floor < 0:
            return i + 1

    return None


def main():
    instructions = get_instructions()

    position = find_basement_enter_position(instructions)

    print(position)


if __name__ == "__main__":
    main()
