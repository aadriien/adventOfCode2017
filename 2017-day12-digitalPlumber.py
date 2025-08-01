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


def identify_group(input: dict[int, list[int]], start_val: int) -> set:
    dq = deque([start_val])
    group = set()

    while dq:
        key = dq.popleft()
        group.add(key)

        # Cycle through keys & check if part of group 
        for val in input[key]:
            if val not in group:
                # Add values to check later
                dq.append(val)

    return group


def count_0_group(input: dict[int, list[int]]) -> int:
    group_set = identify_group(input, 0)
    return len(group_set)


def count_total_groups(input: dict[int, list[int]]) -> int:
    total_groups = 1
    all_seen = identify_group(input, 0)

    for key in input:
        if key not in all_seen:
            total_groups += 1

            # Identify elems of new group & add to seen aggregate
            new_group_set = identify_group(input, key)
            all_seen |= new_group_set

    return total_groups
    

# Validate examples with unit tests
def run_tests() -> None:
    tc_input_1 = {
        0: [2],
        1: [1],
        2: [0, 3, 4],
        3: [2, 4],
        4: [2, 3, 6],
        5: [6],
        6: [4, 5]
    }
    tc_input_2 = {
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

    # Test part 1
    assert (count_0_group(tc_input_1) == 6)
    assert (count_0_group(tc_input_2) == 5)

    # Test part 2
    assert (count_total_groups(tc_input_1) == 2)
    assert (count_total_groups(tc_input_2) == 3)


if __name__ == "__main__":
    run_tests()
    
    mappings = read_file(filename=INPUT_FILE)

    group_size = count_0_group(input=mappings)
    groups_count = count_total_groups(input=mappings)

    print(f"programs in group: {group_size} ... total unique groups: {groups_count}")


