from os import path
from collections import deque

def parse_route(line):
    contents = line.split(" ")

    start = contents[0]
    end = contents[2]
    distance = int(contents[4])

    return start, end, distance

def create_network(routes):
    network = dict()

    for start, end, distance in routes:
        network.setdefault(start, [])
        network[start].append((end, distance))

        network.setdefault(end, [])
        network[end].append((start, distance))

    return network

def get_network():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return create_network(parse_route(line) for line in lines)

def find_longest_path(network):
    queue = deque([(start, 0, set([start])) for start in network.keys()])
    longest_distance = 0

    while queue:
        start, total_distance, visited = queue.popleft()

        if len(visited) == len(network) and total_distance > longest_distance:
            longest_distance = total_distance
            continue

        for end, distance in network[start]:
            if end in visited:
                continue

            queue.append((end, total_distance + distance, { end, *visited }))

    return longest_distance


def main():
    network = get_network()

    distance = find_longest_path(network)

    print(distance)


if __name__ == "__main__":
    main()
