###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 10 - Knot Hash                                                       ##
###############################################################################


INPUT_FILE = "day10-input.txt"


def read_file(filename: str) -> tuple[list[int], str]:
    with open(filename, "r") as input:
        lengths_str = input.read().strip()
        all_lengths = lengths_str.split(",")
        
        return [int(len) for len in all_lengths], lengths_str


# Helper function to build whatever length list to be reversed
def reverse_circular(length: int, curr_list: list[int], idx: int) -> list[int]:
    list_len = len(curr_list)

    sublist = [curr_list[(idx + i) % list_len] for i in range(length)]    
    sublist.reverse()
    
    # Write reversed segment back to original list
    for i in range(length):
        curr_list[(idx + i) % list_len] = sublist[i]
    
    return curr_list
    

# Part 1 of problem
def hash_list(starting_list: list[int], lengths: list[int]) -> list[int]:
    curr_pos, skip_size = 0, 0
    hashed_list = starting_list[:]

    # Cycle through length inputs & run reversal process
    for length in lengths:
        hashed_list = reverse_circular(length, hashed_list, curr_pos)

        curr_pos = (curr_pos + length + skip_size) % len(hashed_list)
        skip_size += 1

    return hashed_list


# Part 2 of problem
def knot_hash(input_str: str) -> str:
    # Convert chars to ASCII equivalent
    lengths = [ord(c) for c in input_str] + [17, 31, 73, 47, 23]

    curr_pos, skip_size = 0, 0
    hashed_list = list(range(256))
    
    for _ in range(64):
        for length in lengths:
            reverse_circular(length, hashed_list, curr_pos)
            curr_pos = (curr_pos + length + skip_size) % len(hashed_list)
            skip_size += 1

    # Hash via XOR of 16-number chunks
    dense_hash = []
    for i in range(0, 256, 16):
        xor = hashed_list[i]
        for n in hashed_list[i+1:i+16]:
            xor ^= n
        dense_hash.append(xor)

    # Convert dense hash to hex string
    return ''.join(f'{n:02x}' for n in dense_hash)


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (hash_list([0, 1, 2, 3, 4], [3, 4, 1, 5]) == [3, 4, 2, 1, 0])

    # Test part 2
    assert (knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert (knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd")
    assert (knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d")
    assert (knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e")
    


if __name__ == "__main__":
    run_tests()
    
    lengths, lengths_str = read_file(filename=INPUT_FILE)
    starting_list = list(range(256))

    hashed_list = hash_list(starting_list=starting_list, lengths=lengths)
    first_two_product = hashed_list[0] * hashed_list[1]

    knotted_hash = knot_hash(input_str=lengths_str)

    print(f"hashed list product: {first_two_product} ... fully knotted hash: {knotted_hash}")

