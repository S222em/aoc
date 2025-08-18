from os import path

def get_lines():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return lines

def get_literal_char_count(line):
    return len(line)

def get_encoded_char_count(line):
    # start at 2 as "" is added
    count = 2

    for char in line:
        if char in ["\\", "\""]:
            count += 1

        count += 1

    return count

def get_char_difference(lines):
    total = 0

    for line in lines:
        total += get_encoded_char_count(line)
        total -= get_literal_char_count(line)

    return total

def main():
    lines = get_lines()

    difference = get_char_difference(lines)

    print(difference)

if __name__ == "__main__":
    main()
