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
    while following the directions
    :param directions:
    :return:
    """
    x, y = 0, 0

    visited = {(x, y)}

    for dx, dy in directions:
        x += dx
        y += dy
        visited.add((x, y))

    return visited


def main():
    directions = get_directions()

    visited = find_visited(directions)

    print(len(visited))


if __name__ == "__main__":
    main()
