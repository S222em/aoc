from os import path

def get_():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        pass


def main():
    pass


if __name__ == "__main__":
    main()
