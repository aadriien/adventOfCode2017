###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 8 - I Heard You Like Registers                                       ##
###############################################################################


import operator
from collections import defaultdict

INPUT_FILE = "day8-input.txt"


operators = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}


def read_file(filename: str) -> list[str]:
    instructions = []
    with open(filename, "r") as input:
        for line in input:
            instructions.append(line.strip())
    return instructions


# Helper function to extract commands
def parse_instruction(instruction: str) -> dict:
    pieces = instruction.split()
    return {
        # Example str format: b inc 5 if a > 1
        "register": pieces[0],
        "action": pieces[1],
        "amount": int(pieces[2]),
        "conditional": {
            "register_check": pieces[4],
            "comparison_check": pieces[5],
            "amount_check": int(pieces[6])
        }
    }


def get_largest_value(instructions: list[str]) -> tuple[int, int]:
    # Parse each str into usable command
    parsed = [parse_instruction(instruction) for instruction in instructions]

    register_values = defaultdict(int)
    highest_ever = float('-inf')

    for command in parsed:
        reg_check = command["conditional"]["register_check"]
        comp_check = command["conditional"]["comparison_check"]
        amnt_check = command["conditional"]["amount_check"]

        # Use operator mapping to run comparison
        if (operators[comp_check](register_values[reg_check], amnt_check)):
            reg = command["register"]
            act = command["action"]
            amnt = command["amount"]

            register_values[reg] += amnt if act == "inc" else -amnt

            # Update record of highest ever value if applicable (for part 2)
            highest_ever = max(highest_ever, register_values[reg])

    return max(register_values.values()), highest_ever


if __name__ == "__main__":
    instructions = read_file(filename=INPUT_FILE)

    largest_value, highest_ever = get_largest_value(instructions=instructions)

    print(f"largest value: {largest_value} ... highest ever: {highest_ever}")

