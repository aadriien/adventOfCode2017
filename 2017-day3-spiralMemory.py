###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 3 - Spiral Memory                                                    ##
###############################################################################

from collections import defaultdict


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


# Part 2 of problem
def get_larger_value(starting_square: int) -> int:
    # NOTES:
    # - up to 8 adjacent squares to sum (if already filled)
    # - can map grid position to adjacent sum value
    # - same pattern of right > up > left > down
    # - number of steps to take by direction (adding new square):
    #   - right or up: 1 step
    #   - left or down: 2 steps

    directions = [
        (1, 0), # right
        (0, 1), # up
        (-1, 0), # left
        (0, -1) # down
    ]

    # Instead of position, focus on how to access from center (0, 0)
    adjacent_steps_from_center = [
        (-1, 1), (0, 1), (1, 1), # reach top row (left, center right)
        (-1, 0), (1, 0), # middle row
        (-1, -1), (0, -1), (1, -1) # bottom row
    ]

    spiral_grid = defaultdict(int)
    x, y = 0, 0
    spiral_grid[(x, y)] = 1

    # Track distance to reach square (e.g. 1 step for right vs 2 for left)
    step_offset = 1

    while True:
        for dir_x, dir_y in directions:
            # Determine steps to take based on layer from center
            for i in range(step_offset):
                x += dir_x
                y += dir_y

                # Max of 8 possible neighbors
                adjacent_sum = 0
                for adj_x, adj_y in adjacent_steps_from_center:
                    neighbor_x, neighbor_y = x + adj_x, y + adj_y
                    adjacent_sum += spiral_grid[(neighbor_x, neighbor_y)]

                # Key as coordinates, value as adjacent sum
                spiral_grid[(x, y)] = adjacent_sum

                # Break out as soon as we pass target
                if adjacent_sum > starting_square:
                    return adjacent_sum

            if dir_x == 0:
                step_offset += 1


if __name__ == "__main__":
    starting_square = read_file(filename=INPUT_FILE)

    steps = calculate_steps(starting_square=starting_square)
    larger_val = get_larger_value(starting_square=starting_square)


    print(f"steps: {steps} ... larger value: {larger_val}")

