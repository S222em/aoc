from os import path
from collections import defaultdict


def get_instructions():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    return [line.strip().split(" ") for line in lines]


def main():
    instructions = get_instructions()

    registers: defaultdict[str, int] = defaultdict(lambda: 0)

    registers = do_instructions(instructions, registers)

    print(registers["a"])
    # print(sorted(registers.items(), key=lambda item: item[0]))

def do_instructions(instructions, registers):
    for instruction in instructions:
        registers = do_instruction(instruction, registers)

    return registers

def do_instruction(instruction: list[str], registers):
    result = 0

    parameters = [resolve_parameter(parameter, registers) for parameter in instruction]

    if instruction[0].isnumeric() and not instruction[1].isalpha():
        result = int(instruction[0])

    if instruction[1] == "AND":
        result = parameters[0] & parameters[2]

    if instruction[1] == "OR":
        result = parameters[0] | parameters[2]

    if instruction[1] == "LSHIFT":
        result = parameters[0] << parameters[2]

    if instruction[1] == "RSHIFT":
        result = parameters[0] >> parameters[2]

    if instruction[0] == "NOT":
        result = ~parameters[1]

    registers[instruction[-1]] = result % 65536

    return registers

def resolve_parameter(parameter: str, registers):
    if parameter.isnumeric():
        return int(parameter)

    return registers[parameter]

if __name__ == "__main__":
    main()
