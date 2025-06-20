###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 6 - Memory Reallocation                                              ##
###############################################################################


INPUT_FILE = "day6-input.txt"


def read_file(filename: str) -> list[int]:
    with open(filename, "r") as input:
        banks_strs = input.read().split()
        return [int(bank) for bank in banks_strs]


def unique_redistributions(banks: list[int], part: int) -> int:
    seen = {}
    cycles = 0

    while tuple(banks) not in seen:
        # Record configuration (curr banks as key & count of steps as value)
        seen[tuple(banks)] = cycles

        # Step 1: get index with max blocks (will default to 1st seen if tie)
        max_blocks = max(banks)
        max_blocks_idx = banks.index(max_blocks)
        
        # Step 2: run redistribution cycle
        banks[max_blocks_idx] = 0
        mod_base = len(banks)
        i = (max_blocks_idx + 1) % mod_base

        while max_blocks > 0:
            banks[i] += 1
            max_blocks -= 1
            i = (i + 1) % mod_base

        cycles += 1

    # In the case of part 2, we want index distance
    return cycles if part == 1 else cycles - seen[tuple(banks)]


if __name__ == "__main__":
    banks = read_file(filename=INPUT_FILE)

    cycles = unique_redistributions(banks=banks[:], part=1)
    second_cycles = unique_redistributions(banks=banks[:], part=2)

    print(f"redistribution cycles: {cycles} ... second cycles: {second_cycles}")

