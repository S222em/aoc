from functools import reduce
from operator import mul


def get_boxes():
    """
    Returns all boxes in the puzzle file.
    A single box is a list containing dimensions sorted small-high.
    :return:
    """
    with open("puzzle.txt") as puzzle:
        lines = puzzle.readlines()

    boxes = list()

    for line in lines:
        dimensions = [int(dimension) for dimension in line.split("x")]
        boxes.append(sorted(dimensions))

    return boxes


def get_ribbon_for(box):
    """
    Finds the amount of ribbon needed for the box and the bow.
    :param box:
    :return:
    """
    wrap = box[0] * 2 + box[1] * 2
    bow = reduce(mul, box)

    return wrap + bow


def get_total_ribbon(boxes):
    """
    Returns the total amount of ribbon required for all the boxes.
    :param boxes:
    :return:
    """
    return sum(get_ribbon_for(box) for box in boxes)


def main():
    boxes = get_boxes()

    total = get_total_ribbon(boxes)

    print(total)


if __name__ == "__main__":
    main()
