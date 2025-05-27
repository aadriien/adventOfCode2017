###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 1 - Inverse Captcha                                                  ##
###############################################################################


INPUT_FILE = "day1-input.txt"


def read_file(filename: str) -> str:
    with open(filename, "r") as input:
        input_str = input.read().strip()
    return input_str


def digit_sum(input_str: str, len_range: int, position: int) -> int:
    sum = 0

    for i in range(1, len_range + 1):
        offset = i % len_range
        curr, prev = input_str[offset], input_str[offset - position]

        if curr == prev:
            sum += int(curr)

    return sum


if __name__ == "__main__":
    input_str = read_file(filename=INPUT_FILE)
    str_len, halfway = len(input_str), len(input_str) // 2

    # Part 1 of problem
    next_sum = digit_sum(input_str=input_str, len_range=str_len, position=1)

    # Part 2 of problem
    halfway_sum = digit_sum(input_str=input_str, len_range=str_len, position=halfway)

    print(f"next digit sum: {next_sum} ... halfway digit sum: {halfway_sum}")

