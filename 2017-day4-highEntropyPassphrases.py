###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 4 - High-Entropy Passphrases                                         ##
###############################################################################


INPUT_FILE = "day4-input.txt"


def read_file(filename: str) -> list[list[str]]:
    # Open file, ingest each line as str, & store as str arrays
    passphrase_lists = []
    with open(filename, "r") as input:
        for line in input:
            passphrase_lists.append(line.split())

    # Return array of those str arrays
    return passphrase_lists


# Part 1 of problem
def count_valid(passphrase_lists: list[list[str]]) -> int:
    valid_count = 0
    for passphrase in passphrase_lists:
        # Convert to set to check for duplicates within line
        is_valid = len(set(passphrase)) == len(passphrase)
        if is_valid: valid_count += 1

    return valid_count


# Part 2 of problem
def count_non_anagrams(passphrase_lists: list[list[str]]) -> int:
    sorted_passphrase_list = []
    
    for passphrase in passphrase_lists:
        # Check for a match after sorting to assess anagram
        sorted_passphrase = [''.join(sorted(word)) for word in passphrase]
        sorted_passphrase_list.append(sorted_passphrase)

    return count_valid(sorted_passphrase_list)


if __name__ == "__main__":
    passphrase_lists = read_file(filename=INPUT_FILE)

    valid_count = count_valid(passphrase_lists=passphrase_lists)
    valid_non_anagrams_count = count_non_anagrams(passphrase_lists=passphrase_lists)

    print(f"valid count: {valid_count} ... valid non-anagrams: {valid_non_anagrams_count}")

