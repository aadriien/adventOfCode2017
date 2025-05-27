###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 2 - Corruption Checksum                                              ##
###############################################################################


INPUT_FILE = "day2-input.txt"


def read_file(filename: str) -> list[list[int]]:
    # Open file, ingest each line as str, & store as num arrays
    nums_lists = []
    with open(filename, "r") as input:
        for line in input:
            line_nums = [int(num) for num in line.split()]
            nums_lists.append(line_nums)

    # Return array of those num arrays
    return nums_lists


# Part 1 of problem
def calculate_checksum(nums_lists: list[list[int]]) -> int:
    checksum = 0
    for nums in nums_lists:
        min_num, max_num = min(nums), max(nums)
        checksum += max_num - min_num

    return checksum


# Part 2 of problem
def calculate_divsum(nums_lists: list[list[int]]) -> int:
    divsum = 0
    for nums in nums_lists:
        # Sort beforehand to reduce iteration load
        sorted_nums = sorted(nums)
        arr_len = len(sorted_nums)

        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                # Break if found match to reduce load
                if sorted_nums[j] % sorted_nums[i] == 0:
                    divsum += sorted_nums[j] // sorted_nums[i]
                    break

    return divsum


if __name__ == "__main__":
    nums_lists = read_file(filename=INPUT_FILE)

    checksum = calculate_checksum(nums_lists=nums_lists)
    divsum = calculate_divsum(nums_lists=nums_lists)

    print(f"checksum: {checksum} ... divsum: {divsum}")

