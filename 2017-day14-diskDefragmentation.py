###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 14 - Disk Defragmentation                                            ##
###############################################################################


INPUT_FILE = "day14-input.txt"


import importlib  
day10_knotHash = importlib.import_module("2017-day10-knotHash")

from collections import deque


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

    # Hash inputs: f"{input_str}-{row_num}"
        # These form the 128 rows
        # Within them, 128 columns for the bits
    for i in range(128):
        hash_input = f"{input_str}-{i}"

        # For each hash input, send to knot hash function (from day 10)
        knot_hash = day10_knotHash.knot_hash(hash_input)
    
        # Convert each of the 32 hexadecimal digits to their respective 4 bits
        for hex_digit in knot_hash:
            # Among all 128 x 128 bits, count the 1s
            used_spaces += count_1_bits(hex_digit)

    return used_spaces


def convert_hex_to_bin(hex_str: str) -> str:
    decimal_val = int(hex_str, 16)

    binary_str_prefix = bin(decimal_val)
    binary_str = binary_str_prefix[2:]

    # Use `zfill` to populate with leading zeroes
    binary_padded = binary_str.zfill(len(hex_str) * 4)
    return binary_padded


def is_valid_neighbor(
        visited: list[list[str]], 
        bit_grid: list[list[str]], 
        row: int, col: int
    ) -> bool:
    # Check bounds for validity
    if row < 0 or row > 127 or col < 0 or col > 127:
        return False
    
    return not visited[row][col] and bit_grid[row][col] == "1"


def bfs_2d_regions(
        visited: list[list[str]], 
        bit_grid: list[list[str]],
        start_row: int, start_col: int
    ) -> None:
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    
    # Check neighbors in 4 directions: up, down, left, right
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        curr_row, curr_col = queue.popleft()
        
        # `dr` == delta row, `dc` == delta column
        for dr, dc in neighbors:
            # `n_row` == new row, `n_col` == new column
            n_row, n_col = curr_row + dr, curr_col + dc
            
            if is_valid_neighbor(visited, bit_grid, n_row, n_col):
                visited[n_row][n_col] = True
                queue.append((n_row, n_col))


# Part 2 of problem
def count_used_regions(input_str: str) -> int:
    # Logic: for any given 1, does it have another 1 above / below / left / right
        # If not, then augment region count

    regions_count = 0
    bit_grid = []
    visited = [[False for i in range(128)] for i in range(128)]

    for i in range(128):
        hash_input = f"{input_str}-{i}"
        knot_hash = day10_knotHash.knot_hash(hash_input)
    
        # Get str of all bits for given 32-digit hex str knot hash
        all_hash_bits = ""
        for hex_digit in knot_hash:
            digit_bits = convert_hex_to_bin(hex_digit)
            all_hash_bits += digit_bits

        # Convert str to arr, then append as new row
        bits_arr = list(all_hash_bits)
        bit_grid.append(bits_arr)            

    # Gross nested loops to check neighbors :( 
    for i in range(128):
        for j in range(128):
            if bit_grid[i][j] == "1" and not visited[i][j]:
                bfs_2d_regions(visited, bit_grid, i, j)
                regions_count += 1

    return regions_count


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (count_used_squares("flqrgnkx") == 8108)

    # Test part 2
    assert (count_used_regions("flqrgnkx") == 1242)
    

if __name__ == "__main__":
    run_tests()
    
    input_str = read_file(filename=INPUT_FILE)

    used_spaces = count_used_squares(input_str=input_str)
    unique_regions = count_used_regions(input_str=input_str)

    print(f"used squares: {used_spaces} ... used regions: {unique_regions}")

