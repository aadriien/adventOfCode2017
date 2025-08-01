###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 12 - Digital Plumber                                                 ##
###############################################################################


from collections import deque

INPUT_FILE = "day12-input.txt"


def read_file(filename: str) -> dict[int, list[int]]:
    mappings = {}

    with open(filename, "r") as input:
        for line in input:
            key, vals = line.strip().split("<->")
            mappings[int(key)] = [int(val) for val in vals.strip().split(",")]

        return mappings


def count_group(input: dict[int, list[int]]) -> int:
    dq = deque([0])
    group = set()

    while dq:
        key = dq.popleft()
        group.add(key)

        # Cycle through keys & check if part of group 
        for val in input[key]:
            if val not in group:
                # Add values to check later
                dq.append(val)

    return len(group)
    

# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (count_group(
        {
            0: [2],
            1: [1],
            2: [0, 3, 4],
            3: [2, 4],
            4: [2, 3, 6],
            5: [6],
            6: [4, 5]
        }
    ) == 6)

    assert (count_group(
        {
            0: [9],
            1: [2],
            2: [1, 6, 10],
            3: [4],
            4: [3, 5], 
            5: [4, 9],
            6: [2, 7],
            7: [6],
            8: [8],
            9: [0, 5],
            10: [2]
        }
    ) == 5)



if __name__ == "__main__":
    run_tests()
    
    mappings = read_file(filename=INPUT_FILE)

    group_size = count_group(input=mappings)

    print(f"programs in group: {group_size}")


