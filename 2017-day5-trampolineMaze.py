###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 5 - Maze of Twisty Trampolines                                       ##
###############################################################################


INPUT_FILE = "day5-input.txt"


def read_file(filename: str) -> list[int]:
    nums = []
    with open(filename, "r") as input:
        for line in input:
            nums.append(int(line.strip()))
    return nums


def jump_steps(nums: list[int], part: int) -> int:
    steps = 0
    curr_index, max_index = 0, len(nums) - 1

    while 0 <= curr_index <= max_index:
        jump_distance = nums[curr_index]

        if (part == 2 and jump_distance >= 3):
            nums[curr_index] -= 1
        else:
            nums[curr_index] += 1
        
        curr_index += jump_distance
        steps += 1

    return steps


if __name__ == "__main__":
    # Copy input to pass along for 2nd portion (avoid direct array edit)
    nums = read_file(filename=INPUT_FILE)
    nums_copy = nums.copy()

    steps_part1 = jump_steps(nums=nums, part=1)
    steps_part2 = jump_steps(nums=nums_copy, part=2)

    print(f"maze steps: {steps_part1} ... strange maze steps: {steps_part2}")

