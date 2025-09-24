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


def process_instruction(
        instruction: dict[str],
        registers: dict[str, int],
        sounds_played: list[int], recovered: list[int],
        curr: int = 0,
        part: int = 1
    ) -> tuple[bool, int]:
    # Extract values from dict
    command = instruction["command"]
    reg_x = instruction["reg_x"]
    input_y = instruction["input_y"]

    # Flexibly support explicit int value AND value in register
    val_x = registers[reg_x] if reg_x.isalpha() else int(reg_x)
    if input_y:
        int_y = registers[input_y] if input_y.isalpha() else int(input_y)
    
    match command:
        case "snd":
            sounds_played.append(val_x)

            # Increment counter for part 2
            registers["_sent"] += 1

        case "set":
            registers[reg_x] = int_y

        case "add":
            registers[reg_x] += int_y

        case "mul":
            registers[reg_x] *= int_y

        case "mod":
            registers[reg_x] %= int_y

        case "rcv":
            if part == 1:
                # Handle part 1 of problem with break case
                if sounds_played and sounds_played[-1] > 0:
                    recovered.append(sounds_played[-1])
                    return False, -1
            else:
                # Otherwise, handle case for part 2 (check empty queue)
                if recovered:
                    registers[reg_x] = recovered.pop(0)
                    return True, curr + 1
                else: 
                    return False, curr

        case "jgz":
            if val_x > 0:
                return True, curr + int_y

    return True, curr + 1


# Part 1 of problem
def get_frequency_val(instructions: list[dict[str]]) -> int:
    registers = defaultdict(int)
    sounds_played, recovered = [], []

    # Determine bounds for valid range
    curr, total_len = 0, len(instructions)

    # Iterate through instructions (or jump around) so long as within bounds
    while 0 <= curr < total_len:
        _, curr = process_instruction(
            instructions[curr], 
            registers, 
            sounds_played, recovered, 
            curr
        )
        if curr == -1:
            break

    return recovered[0] if recovered else -1


# Part 2 of problem
def do_program_exchange(instructions: list[dict[str]]) -> int:
    sent_by_0, sent_by_1 = [], []

    prog_0_reg, prog_1_reg = defaultdict(int), defaultdict(int)
    prog_0_reg["p"], prog_1_reg["p"] = 0, 1

    curr_0 = curr_1 = 0
    total_len = len(instructions)
    
    successful_0 = successful_1 = True

    # Run processing for both programs
    while True:
        while 0 <= curr_0 < total_len and successful_0:
            successful_0, curr_0 = process_instruction(
                instructions[curr_0],
                prog_0_reg, 
                sent_by_0, sent_by_1,
                curr=curr_0, part=2
            )

        while 0 <= curr_1 < total_len and successful_1:
            successful_1, curr_1 = process_instruction(
                instructions[curr_1],
                prog_1_reg, 
                sent_by_1, sent_by_0,
                curr=curr_1, part=2
            )

        # Determine states
        p0_active = 0 <= curr_0 < total_len
        p1_active = 0 <= curr_1 < total_len

        blocked_0 = p0_active and (not successful_0)
        blocked_1 = p1_active and (not successful_1)

        queues_empty = (not sent_by_0) and (not sent_by_1)

        # Queues empty & both programs either blocked or terminated
        deadlock_condition = queues_empty and (
            (not p0_active or blocked_0) and 
            (not p1_active or blocked_1)
        )
        
        if deadlock_condition:
            break

        # Otherwise, allow both to resume progress
        successful_0 = True
        successful_1 = True

    return prog_1_reg["_sent"]


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

    tc_input_2_raw = [
        "snd 1",
        "snd 2",
        "snd p",
        "rcv a",
        "rcv b",
        "rcv c",
        "rcv d",
    ]
    tc_input_2 = [parse_instruction(line) for line in tc_input_2_raw]

    # Test part 1
    assert (get_frequency_val(tc_input_1) == 4)

    # Test part 2
    assert (do_program_exchange(tc_input_2) == 3)


if __name__ == "__main__":
    run_tests()
    
    instructions = read_file(filename=INPUT_FILE)

    recovered_frequency = get_frequency_val(instructions=instructions)
    sent_values = do_program_exchange(instructions=instructions)

    print(f"recovered frequency: {recovered_frequency} ... sent values: {sent_values}")


