###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 16 - Permutation Promenade                                           ##
###############################################################################


INPUT_FILE = "day16-input.txt"


DANCERS = "abcdefghijklmnop"


def read_file(filename: str) -> dict[int, int]:
    with open(filename, "r") as input:
        moves_str = input.read().strip()
        return moves_str.split(",")


def apply_spin(programs_count: int, dancers: str) -> str:
    tail = dancers[-programs_count:]
    return tail + dancers[:-programs_count]


def apply_exchange(pos_A: int, pos_B: int, dancers: str) -> str:
    dancers_list = list(dancers)
    dancers_list[pos_A], dancers_list[pos_B] = dancers_list[pos_B], dancers_list[pos_A]
    return "".join(dancers_list)


def apply_partner(val_A: int, val_B: int, dancers: str) -> str:
    # Find positions of val_A & val_B in dancers
    index_A = dancers.index(val_A)
    index_B = dancers.index(val_B)

    return apply_exchange(index_A, index_B, dancers)


# Part 1 of problem
def run_dance(dance_moves: list[str], dancers: str = DANCERS) -> str:
    for move in dance_moves:

        if move[0] == "s":
            dancers = apply_spin(int(move[1:]), dancers)

        elif move[0] == "x":
            first, second = move[1:].split("/")
            dancers = apply_exchange(int(first), int(second), dancers)

        elif move[0] == "p":
            first, second = move[1:].split("/")
            dancers = apply_partner(first, second, dancers)

        else: # invalid input
            continue

    return dancers


# Part 2 of problem
def repeat_dance(dance_moves: list[str], dancers: str = DANCERS) -> str:
    seen = {}
    
    for i in range(1000000000):
        if dancers in seen:
            # When cycle detected, calculate steps to reach it
            cycle_start = seen[dancers]
            cycle_length = i - cycle_start
            remaining_steps = (1000000000 - cycle_start) % cycle_length
            
            # Run remaining steps
            for _ in range(remaining_steps):
                dancers = run_dance(dance_moves, dancers)
            
            return dancers
        
        seen[dancers] = i
        dancers = run_dance(dance_moves, dancers)
    
    return dancers


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (run_dance(["s1", "x3/4", "pe/b"], "abcde") == "baedc")


if __name__ == "__main__":
    run_tests()
    
    dance_moves = read_file(filename=INPUT_FILE)

    ending_order = run_dance(dance_moves=dance_moves)
    billion_order = repeat_dance(dance_moves=dance_moves)

    print(f"ending order: {ending_order} ... billion dances order: {billion_order}")


