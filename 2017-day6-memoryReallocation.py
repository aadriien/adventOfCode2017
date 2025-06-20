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


# Part 1 of problem
def unique_redistributions(banks: list[int]) -> int:
    seen = []
    cycles = 0

    def redistribute_new(banks: list[int], seen: list[list[int]]) -> bool:
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

        # Step 3: record configuration
        if banks in seen:
            return True
        else:
            # Store copy to avoid issues with mutating array
            seen.append(banks[:])
            return False

    while not redistribute_new(banks, seen):
        cycles += 1

    return cycles + 1



if __name__ == "__main__":
    banks = read_file(filename=INPUT_FILE)

    cycles = unique_redistributions(banks=banks)

    print(f"redistribution cycles: {cycles} ... redistribution cycles: {cycles}")

