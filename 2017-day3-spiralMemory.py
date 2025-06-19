###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 3 - Spiral Memory                                                    ##
###############################################################################


INPUT_FILE = "day3-input.txt"


def read_file(filename: str) -> list[list[int]]:
    with open(filename, "r") as input:
        starting_square = input.read()

    return int(starting_square)


# Part 1 of problem
def calculate_steps(starting_square: int) -> int:
    # NOTES:
    # - spiral drawing pattern == move right/left x up/down in pairs, e.g..
    #   - move 1 right, 1 up
    #   - move 2 left, 2 down
    #   - move 3 right, 3 up
    #   - move 4 left, 4 down
    # - Manhattan distance == |x1 - x2| + |y1 - y2|, e.g..
    #   - (1, 3) <> (6, 2) == |1 - 6| + |3 - 2| = 5 + 1 = 6
    
    # APPROACH:
    # - treat (0, 0) access port as layer 0
    #   - length of side for any given layer == (2 * n) + 1
    #       - halfway point of side length aligns with 0 of access port..
    #       - so can gauge x/y offset from 0 based on layer position
    #   - max number (bottom right) for any given layer == ((2 * n) + 1) ^ 2

    # Find layer we're currently in
    layer = 0
    while ((2 * layer) + 1) ** 2 < starting_square:
        layer += 1

    # Then determine offset in layer
    base_val = (((2 * (layer - 1)) + 1) ** 2) + 1 # start from prev layer's end
    offset = starting_square - base_val
    side_len, halfway = 2 * layer, (2 * layer) // 2 # subtract 1 since spiral 

    # Determine x, y coordinate based on position in layer
    if offset < side_len: # right edge
        x, y = side_len - offset, -halfway + offset + 1
    elif offset < side_len * 2: # top edge
        x, y = side_len - offset + 1, 0
    elif offset < side_len * 3: # left edge
        pass
    else: # bottom edge
        pass




if __name__ == "__main__":
    starting_square = read_file(filename=INPUT_FILE)

    steps = calculate_steps(starting_square=starting_square)


    print(f"steps: {steps}")

