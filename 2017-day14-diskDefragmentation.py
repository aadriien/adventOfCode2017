###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 14 - Disk Defragmentation                                            ##
###############################################################################


INPUT_FILE = "day14-input.txt"


import importlib  
day10_knotHash = importlib.import_module("2017-day10-knotHash")


def read_file(filename: str) -> str:
    with open(filename, "r") as input:
        return input.read().strip()
    

def count_1_bits(hex_str: str) -> int:
    decimal_val = int(hex_str, 16)

    binary_str = bin(decimal_val)
    return binary_str.count("1")


# Part 1 of problem
def count_used_squares(input_str: str) -> int:
    used_spaces = 0

    # hash inputs: f"{input_str}-{row_num}"
        # these form the 128 rows
        # within them, 128 columns for the bits
    for i in range(128):
        hash_input = f"{input_str}-{i}"

        # for each hash input, send to knot hash function (from day 10)
        knot_hash = day10_knotHash.knot_hash(hash_input)
    
        # convert each of the 32 hexadecimal digits to their respective 4 bits
        for hex_digit in knot_hash:
            # among all 128 x 128 bits, count the 1s
            used_spaces += count_1_bits(hex_digit)

    return used_spaces



# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (count_used_squares("flqrgnkx") == 8108)

    # Test part 2

    

if __name__ == "__main__":
    run_tests()
    
    input_str = read_file(filename=INPUT_FILE)

    used_spaces = count_used_squares(input_str=input_str)


    print(f"used squares: {used_spaces} ... ")

