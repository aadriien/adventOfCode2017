###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 10 - Knot Hash                                                       ##
###############################################################################


INPUT_FILE = "day10-input.txt"


def read_file(filename: str) -> str:
    with open(filename, "r") as input:
        all_lengths = input.read().strip().split(",")
        return [int(len) for len in all_lengths]



def hash_list(starting_list: list[int], lengths: list[int]) -> list[int]:
    # Helper function to build whatever length list to be reversed
    def reverse_circular(length: int, curr_list: list[int], idx: int) -> list[int]:
        list_len = len(curr_list)

        sublist = [curr_list[(idx + i) % list_len] for i in range(length)]    
        sublist.reverse()
        
        # Write reversed segment back to original list
        for i in range(length):
            curr_list[(idx + i) % list_len] = sublist[i]
        
        return curr_list
    
    curr_pos, skip_size = 0, 0
    hashed_list = starting_list[:]

    # Cycle through length inputs & run reversal process
    for length in lengths:
        hashed_list = reverse_circular(length, hashed_list, curr_pos)

        curr_pos = (curr_pos + length + skip_size) % len(hashed_list)
        skip_size += 1

    return hashed_list



# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (hash_list([0, 1, 2, 3, 4], [3, 4, 1, 5]) == [3, 4, 2, 1, 0])
    


if __name__ == "__main__":
    run_tests()
    
    lengths = read_file(filename=INPUT_FILE)
    starting_list = list(range(256))

    hashed_list = hash_list(starting_list=starting_list, lengths=lengths)
    first_two_product = hashed_list[0] * hashed_list[1]

    print(f"hashed list product: {first_two_product}")

