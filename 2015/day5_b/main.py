def get_strings():
    """
    Retrieves all the strings from the puzzle
    :return:
    """
    with open("puzzle.txt") as puzzle:
        strings = puzzle.readlines()

    return [string.strip() for string in strings]


def is_nice(string: str):
    """
    Whether the given string is nice.
    :param string:
    :return:
    """
    for i, char in enumerate(string[:-1]):
        pair = string[i:i + 2]

        if pair in string[i + 2:]:
            break

        if i == len(string) - 2:
            return False

    for i, char in enumerate(string[:-2]):
        if char == string[i + 2]:
            break

        if i == len(string) - 3:
            return False

    return True


def find_nice_strings(strings):
    """
    Finds all nice strings
    :param strings:
    :return:
    """
    return sum(is_nice(string) for string in strings)


def main():
    strings = get_strings()

    total = find_nice_strings(strings)

    print(total)


if __name__ == "__main__":
    main()
