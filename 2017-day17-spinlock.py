###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 17 - Spinlock                                                        ##
###############################################################################


INPUT_FILE = "day17-input.txt"


def read_file(filename: str) -> int:
    with open(filename, "r") as input:
        return int(input.read().strip())


# Part 1 of problem
def get_next_val(steps: int) -> int:
    REPEAT_TIMES = 2017
    buffer = [0]
    last_pos = 0

    for i in range(1, REPEAT_TIMES + 1):
        offset = (last_pos + steps + 1) % len(buffer)
        buffer.insert(offset, i)
        last_pos = offset

    # Find index of value 2017
    idx = buffer.index(REPEAT_TIMES)
    return buffer[idx + 1]


# Part 2 of problem
def get_val_after_50mil(steps: int) -> int:
    REPEAT_TIMES = 50000001
    final_res = None
    current_pos = 0

    for i in range(1, REPEAT_TIMES + 1):
        # Track how many iterations completed for mod 
        current_pos = ((current_pos + steps) % i) + 1

        # We only care what happens after idx 0
        if current_pos == 1:
            final_res = i 

    return final_res 


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (get_next_val(3) == 638)


if __name__ == "__main__":
    run_tests()
    
    steps = read_file(filename=INPUT_FILE)

    next_val = get_next_val(steps=steps)
    val_after_50mil = get_val_after_50mil(steps=steps)

    print(f"next val: {next_val} ... fast spin val: {val_after_50mil}")


