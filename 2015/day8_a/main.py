from os import path

def get_lines():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return lines

def get_code_char_count(line):
    return len(line)

def get_memory_char_count(line):
    count = 0
    i = 1

    while i < len(line) - 1:
        if line[i] == "\\" and line[i + 1] in ["\"", "\\", "x"]:
            i += 4 if line[i + 1] == "x" else 2
        else:
            i += 1

        count += 1

    return count

def get_char_difference(lines):
    total = 0

    for line in lines:
        total += get_code_char_count(line)
        total -= get_memory_char_count(line)

    return total

def main():
    lines = get_lines()

    difference = get_char_difference(lines)

    print(difference)

if __name__ == "__main__":
    main()
