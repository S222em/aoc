from os import path

def get_strings():
    """
    Retrieves all the strings from the puzzle
    :return:
    """
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        strings = puzzle.readlines()

    return [string.strip() for string in strings]


def is_nice(string: str):
    """
    Whether the given string is nice.
    :param string:
    :return:
    """
    if sum(char in "aeiou" for char in string) < 3:
        return False

    if any(s in string for s in ("ab", "cd", "pq", "xy")):
        return False

    for i, char in enumerate(string[:-1]):
        if char == string[i + 1]:
            break

        if i == len(string) - 2:
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
