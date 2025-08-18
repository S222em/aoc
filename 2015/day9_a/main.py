from os import path

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

def find_shortest_path(network):
    queue = [(start, 0, set([start])) for start in network.keys()]

    while queue:
        current = min(queue, key=lambda item: item[1])
        queue.remove(current)
        start, total_distance, visited = current

        if len(visited) == len(network):
            return total_distance

        for end, distance in network[start]:
            if end in visited:
                continue

            queue.append((end, total_distance + distance, { end, *visited }))

    return None


def main():
    network = get_network()

    distance = find_shortest_path(network)

    print(distance)


if __name__ == "__main__":
    main()
