from os import path


def get_boxes():
    """
    Returns all boxes in the puzzle file.
    A single box is a list containing dimensions sorted small-high.
    :return:
    """
    parent = path.abspath(path.dirname(__file__))

    with open(path.join(parent, "puzzle.txt")) as puzzle:
        lines = puzzle.readlines()

    boxes = list()

    for line in lines:
        dimensions = [int(dimension) for dimension in line.split("x")]
        boxes.append(sorted(dimensions))

    return boxes


def get_wrapping_paper_for(box):
    """
    Finds the amount of wrapping paper needed for the box.
    :param box:
    :return:
    """
    surface = 2 * box[0] * box[1] + 2 * box[0] * box[2] + 2 * box[1] * box[2]
    # The smallest side is the 2 smallest dimensions multiplied by another.
    # As the boxes dimensions are sorted, 0 and 1 will be the smallest dimensions.
    extra = box[0] * box[1]

    return surface + extra


def get_total_wrapping_paper(boxes):
    """
    Returns the total amount of wrapping paper required for all the boxes.
    :param boxes:
    :return:
    """
    return sum(get_wrapping_paper_for(box) for box in boxes)


def main():
    boxes = get_boxes()

    total = get_total_wrapping_paper(boxes)

    print(total)


if __name__ == "__main__":
    main()
