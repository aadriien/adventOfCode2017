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
    o_row, o_col = origin
    d_row, d_col = dest

    return (
        abs(d_row - o_row) + 
        abs(d_col - o_col) + 
        abs(d_row + d_col - o_row - o_col)
    ) / 2


def min_steps(path: list[str]) -> int:
    # Based on hex grids, view through lens of rows x columns 
    row, col = 0, 0

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

    return calculate_distance([0, 0], [row, col])       


# Validate examples with unit tests
def run_tests() -> None:
     # Test part 1
    assert (min_steps(["ne", "ne", "ne"]) == 3)
    assert (min_steps(["ne", "ne", "sw", "sw"]) == 0)
    assert (min_steps(["ne", "ne", "s", "s"]) == 2)
    assert (min_steps(["se", "sw", "se", "sw", "sw"]) == 3)

    # Test part 2
    # assert (min_steps(["ne", "ne", "ne"]) == 3)


if __name__ == "__main__":
    run_tests()
    
    path = read_file(filename=INPUT_FILE)

    steps = min_steps(path=path)

    print(f"min steps: {steps}")


