import hashlib
from os import path


def get_secret_key():
    """
    Gets the secret key from the puzzle
    :return:
    """
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        secret_key = puzzle.read().strip()

    return secret_key


def find_number(secret_key):
    """
    Finds the number with which the secret_key + number hashed with md5
    has 6 leading zeros.
    :param secret_key:
    :return:
    """
    i = 0

    while True:
        hash = hashlib.md5(f"{secret_key}{i}".encode()).hexdigest()
        if hash.startswith("0" * 6):
            return i

        i += 1


def main():
    secret_key = get_secret_key()

    number = find_number(secret_key)

    print(number)


if __name__ == "__main__":
    main()
