###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 15 - Dueling Generators                                              ##
###############################################################################


INPUT_FILE = "day15-input.txt"


# Fixed values for calculations
DIVISOR = 2147483647
FACTOR_A = 16807
FACTOR_B = 48271


def read_file(filename: str) -> tuple[int, int]:
    generator_vals = []

    with open(filename, "r") as input:
        for line in input:
            # Get last 3 chars for A / B starting values
            generator_vals.append(int(line[-4:]))

    return generator_vals[0], generator_vals[1]


def generate_next(prev_val: int, factor: int) -> int:
    product = prev_val * factor
    return product % DIVISOR


def pairs_match(value_A: int, value_B: int) -> bool:
    binary_str_A, binary_str_B = bin(value_A), bin(value_B)
    return binary_str_A[-16:] == binary_str_B[-16:]


# Part 1 of problem
def get_final_count(starting_A: int, starting_B: int) -> int:
    final_count = 0

    # Generate the 40 mil pairs
    for _ in range(40000000):
        starting_A = generate_next(starting_A, FACTOR_A)
        starting_B = generate_next(starting_B, FACTOR_B)
        
        # Convert decimal to binary & check for match
        if pairs_match(starting_A, starting_B):
            final_count += 1

    return final_count
    

# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (get_final_count(65, 8921) == 588)
    

if __name__ == "__main__":
    run_tests()
    
    starting_A, starting_B = read_file(filename=INPUT_FILE)
    print(starting_A, starting_B)

    final_count = get_final_count(starting_A=starting_A, starting_B=starting_B)

    print(f"final count: {final_count} ... ")

