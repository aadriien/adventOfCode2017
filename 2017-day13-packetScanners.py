###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 13 - Packet Scanners                                                 ##
###############################################################################


INPUT_FILE = "day13-input.txt"


def read_file(filename: str) -> dict[int, int]:
    layers = {}

    with open(filename, "r") as input:
        for line in input:
            depth, range = line.strip().split(":")
            layers[int(depth)] = int(range)

        return layers


def is_caught(elapsed_time: int, layer_range: int) -> bool:
    # Notes:
    #   - Complete cycles == time / (layer - 1)
    #   - If even cycles, at top.. otherwise at bottom if odd
    remaining = elapsed_time % (layer_range - 1)
    if remaining != 0: return False

    # Caught if at 0th index
    cycles = elapsed_time / (layer_range - 1)
    return cycles % 2 == 0


def calculate_severity(layers: dict[int, int]) -> int:
    # Keep track of time in picoseconds
    elapsed, severity = 0, 0
    layers_count = max(layers)

    # For each layer, check if caught (with time elapsing)
    for i in range(layers_count + 1):
        if i in layers:
            # If so, add to total severity
            if is_caught(elapsed, layers[i]):
                severity += i * layers[i]

        elapsed += 1
    
    return severity


def determine_delay(layers: dict[int, int]) -> int:
    # Brute force: find earliest picosecond config where not caught
    # IMPORTANT: layer 0 counts as caught even though 0 severity! 
    delay = 0
    while True:
        if all(
            not is_caught(depth + delay, rng) 
            for depth, rng in layers.items()
        ):
            return delay
        delay += 1


# Validate examples with unit tests
def run_tests() -> None:
    tc_input_1 = {
        0: 3,
        1: 2,
        4: 4,
        6: 4,
    }

    # Test part 1
    assert (calculate_severity(tc_input_1) == 24)

    # Test part 2
    assert (determine_delay(tc_input_1) == 10)


if __name__ == "__main__":
    run_tests()
    
    layers = read_file(filename=INPUT_FILE)

    trip_severity = calculate_severity(layers=layers)
    picosecond_delay = determine_delay(layers=layers)

    print(f"trip severity: {trip_severity} ... picosecond delay: {picosecond_delay}")


