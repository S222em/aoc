def get_schematics():
    """
    Returns all schematics in the puzzle file
    :return:
    """
    with open("puzzle.txt") as file:
        schematics = file.read().split("\n\n")

    return [[line.strip() for line in schematic.split("\n")] for schematic in schematics]


def is_key(schematic):
    """
    Whether the given schematic is a key
    :param schematic:
    :return:
    """
    return all(char == "#" for char in schematic[-1])


def get_schematic_heights(schematic):
    """
    Parses the schematic into a list of heights
    :param schematic:
    :return:
    """
    heights = list()

    for i in range(len(schematic[0])):
        height = sum(line[i] == "#" for line in schematic)
        heights.append(height)

    return heights


def get_keys_and_locks(schematics):
    """
    Parses the schematics into a list of keys and locks and their respective heights
    :param schematics:
    :return:
    """
    keys = list()
    locks = list()

    for schematic in schematics:
        heights = get_schematic_heights(schematic)

        if is_key(schematic):
            keys.append(heights)
            continue

        locks.append(heights)

    return keys, locks


def fit(key, lock, target):
    """
    Whether a key fits the lock
    Simply if the key height + lock height is less then or equal to target
    :param key:
    :param lock:
    :param target:
    :return:
    """
    return all(kh + lh <= target for kh, lh in zip(key, lock))


def count_unique_pairs(schematics):
    """
    Count the amount of unique key-lock pairs
    :param schematics:
    :return:
    """
    keys, locks = get_keys_and_locks(schematics)

    target = len(schematics[0])

    total = 0

    for key in keys:
        for lock in locks:
            if not fit(key, lock, target):
                continue

            total += 1

    return total


def main():
    schematics = get_schematics()

    total = count_unique_pairs(schematics)

    print(total)


if __name__ == "__main__":
    main()
