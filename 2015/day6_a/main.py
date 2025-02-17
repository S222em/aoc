from os import path
from collections import defaultdict
import re

RANGE_PATTERN = re.compile(r"\d+,\d+")

def get_instructions():
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    instructions = []

    for line in lines:
        action = get_action_of(line)

        (start, end) = (parse_range(range_str) for range_str in RANGE_PATTERN.findall(line))

        instructions.append((action, start, end))

    return instructions

def get_action_of(line: str):
    if line.startswith("toggle"):
        return "toggle"
    
    if line.startswith("turn off"):
        return "off"

    return "on"

def parse_range(range_str: str):
    return tuple(int(number) for number in range_str.split(","))


def main():
    instructions = get_instructions()

    lights: defaultdict[(int, int), bool] = defaultdict(lambda: False)

    lights = do_instructions(instructions, lights)

    print(count_lit_lights(lights))

def do_instructions(instructions, lights):
    for instruction in instructions:
        lights = do_instruction(instruction, lights)

    return lights

def do_instruction(instruction, lights: defaultdict[(int, int), bool]):
    (action, start, end) = instruction

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            lights[(x, y)] = get_new_state(lights[(x, y)], action)
            
    return lights

def get_new_state(state, action):
    if action == "toggle":
        return not state
    
    if action == "on":
        return True
    
    return False

def count_lit_lights(lights):
    return sum(lit for lit in lights.values())

if __name__ == "__main__":
    main()
