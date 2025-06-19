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
    #   - length of side for any given layer n == 2 * n
    #       - halfway point of side length aligns with 0 of access port..
    #       - so can gauge x/y offset from 0 based on layer position
    #   - max number (bottom right) for any given layer n == ((2 * n) + 1) ^ 2

    # Handle case of center square
    if starting_square == 1:
        return 0

    # Find layer we're currently in
    layer = 0
    while ((2 * layer) + 1) ** 2 < starting_square:
        layer += 1

    # Then determine offset in layer
    max_val = (2 * layer + 1) ** 2
    side_len = 2 * layer

    # Find min distance to midpoints / centers of any side
    side_centers = [max_val - (side_len // 2) - side_len * i for i in range(4)]
    min_dist_to_center = min(abs(starting_square - center) for center in side_centers)

    return layer + min_dist_to_center



if __name__ == "__main__":
    starting_square = read_file(filename=INPUT_FILE)

    steps = calculate_steps(starting_square=starting_square)


    print(f"steps: {steps}")

