###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 11 - Hex Ed                                                          ##
###############################################################################


INPUT_FILE = "day11-input.txt"


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as input:
        input_str = input.read().strip()
        return input_str.split(",")


def calculate_distance(origin: tuple[int, int], dest: tuple[int, int]) -> int:
    # Axial distance for hex grid
    o_row, o_col = origin
    d_row, d_col = dest

    return (
        abs(d_row - o_row) + 
        abs(d_col - o_col) + 
        abs(d_row + d_col - o_row - o_col)
    ) / 2


def calculate_steps(path: list[str], part: int) -> int:
    # Based on hex grid, view through lens of rows x columns 
    row, col = 0, 0
    max_dist = 0

    for dir in path:
        match dir:
            # From axial coordinates system
            case "n": 
                row -= 1
            case "s": 
                row += 1
            case "ne":
                row -= 1
                col += 1
            case "sw":
                row += 1
                col -= 1
            case "se": 
                col += 1
            case "nw":
                col -= 1

        # Maintain max distance for part 2 of problem
        max_dist = max(max_dist, calculate_distance([0, 0], [row, col]))

    return calculate_distance([0, 0], [row, col]) if part == 1 else max_dist


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (calculate_steps(["ne", "ne", "ne"], 1) == 3)
    assert (calculate_steps(["ne", "ne", "sw", "sw"], 1) == 0)
    assert (calculate_steps(["ne", "ne", "s", "s"], 1) == 2)
    assert (calculate_steps(["se", "sw", "se", "sw", "sw"], 1) == 3)


if __name__ == "__main__":
    run_tests()
    
    path = read_file(filename=INPUT_FILE)

    min_steps = calculate_steps(path=path, part=1)
    max_steps = calculate_steps(path=path, part=2)

    print(f"min steps: {min_steps} ... max steps: {max_steps}")


