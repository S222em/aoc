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
        brightness_change = get_brightness_change(line)

        (start, end) = (parse_range(range_str) for range_str in RANGE_PATTERN.findall(line))

        instructions.append((brightness_change, start, end))

    return instructions

def get_brightness_change(line: str):
    if line.startswith("turn on"):
        return 1
    
    if line.startswith("turn off"):
        return -1

    return 2

def parse_range(range_str: str):
    return tuple(int(number) for number in range_str.split(","))


def main():
    instructions = get_instructions()

    lights: defaultdict[(int, int), int] = defaultdict(lambda: 0)

    lights = do_instructions(instructions, lights)

    print(get_total_brightness(lights))

def do_instructions(instructions, lights):
    for instruction in instructions:
        lights = do_instruction(instruction, lights)

    return lights

def do_instruction(instruction, lights: defaultdict[(int, int), bool]):
    (brightness_change, start, end) = instruction

    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            lights[(x, y)] = max(0, lights[(x, y)] + brightness_change)
            
    return lights

def get_new_state(state, action):
    if action == "toggle":
        return not state
    
    if action == "on":
        return True
    
    return False

def get_total_brightness(lights):
    return sum(brightness for brightness in lights.values())

if __name__ == "__main__":
    main()
