###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 18 - Duet                                                            ##
###############################################################################


from collections import defaultdict


INPUT_FILE = "day18-input.txt"


def read_file(filename: str) -> list[dict[str]]:
    # Data structure:
    #   each instance of instructions == dict
    #   {
    #       command: str,
    #       reg_x: str,
    #       input_y: Optional[str] = ""
    #   }
    instructions = []

    with open(filename, "r") as input:
        for line in input:
            instructions.append(parse_instruction(line))

    return instructions


def parse_instruction(line: str) -> list[dict[str]]:
    pieces = line.split()
    return {
        "command": pieces[0],
        "reg_x": pieces[1],

        # str to support register (str) AND/OR value (int) as input
        "input_y": pieces[2] if len(pieces) > 2 else ""
    }


def process_instructions(
        instructions: list[dict[str]],
        registers: dict[str, int],
        sounds_played: list[int], recovered: list[int],
        breakpoint: bool = True
    ) -> None:
    # Determine bounds for valid range
    curr, total_len = 0, len(instructions)

    # Iterate through instructions (or jump around) so long as within bounds
    while 0 <= curr < total_len:
        command = instructions[curr]["command"]
        reg_x = instructions[curr]["reg_x"]
        input_y = instructions[curr]["input_y"]

        # Flexibly support explicit int value AND value in register
        if input_y:
            int_y = registers[input_y] if input_y.isalpha() else int(input_y)
        
        match command:
            case "snd":
                sounds_played.append(registers[reg_x])

            case "set":
                registers[reg_x] = int_y

            case "add":
                registers[reg_x] += int_y

            case "mul":
                registers[reg_x] *= int_y

            case "mod":
                registers[reg_x] %= int_y

            case "rcv":
                if sounds_played and sounds_played[-1] > 0:
                    recovered.append(sounds_played[-1])

                    # Trigger break case where needed
                    if breakpoint: return

            case "jgz":
                if registers[reg_x] > 0:
                    # Subtract 1 from offset to account for incremental idx
                    curr += int_y - 1

        curr += 1


# Part 1 of problem
def get_frequency_val(instructions: list[dict[str]]) -> int:
    registers = defaultdict(int)
    sounds_played, recovered = [], []

    process_instructions(instructions, registers, sounds_played, recovered)

    return recovered[0] if recovered else -1


# Validate examples with unit tests
def run_tests() -> None:
    tc_input_1_raw = [
        "set a 1",
        "add a 2",
        "mul a a",
        "mod a 5",
        "snd a",
        "set a 0",
        "rcv a",
        "jgz a -1",
        "set a 1",
        "jgz a -2",
    ]
    tc_input_1 = [parse_instruction(line) for line in tc_input_1_raw]

    # Test part 1
    assert (get_frequency_val(tc_input_1) == 4)


if __name__ == "__main__":
    run_tests()
    
    instructions = read_file(filename=INPUT_FILE)

    recovered_frequency = get_frequency_val(instructions=instructions)

    print(f"recovered frequency: {recovered_frequency} ...")


