DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, 1),
    "^": (0, -1)
}


def get_directions():
    """
    Parses the directions in the puzzle into a list of vectors.
    :return:
    """
    with open("puzzle.txt") as puzzle:
        directions = puzzle.read().strip()

    return [DIRECTIONS[direction] for direction in directions]


def find_visited(directions):
    """
    Finds all the houses that will be visited at least once,
    while following the directions, split between Santa and Robot-Santa
    :param directions:
    :return:
    """
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    visited = {(x1, y1)}

    for i, (dx, dy) in enumerate(directions):
        if i % 2 == 0:
            x1 += dx
            y1 += dy
            visited.add((x1, y1))
            continue

        x2 += dx
        y2 += dy
        visited.add((x2, y2))

    return visited


def main():
    directions = get_directions()

    visited = find_visited(directions)

    print(len(visited))


if __name__ == "__main__":
    main()
