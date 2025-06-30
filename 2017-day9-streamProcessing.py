###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 9 - Stream Processing                                                ##
###############################################################################


INPUT_FILE = "day9-input.txt"


def read_file(filename: str) -> str:
    with open(filename, "r") as input:
        return input.read().strip()


# QUESTION: how many valid groups within a given group stream?
# APPROACH:
#   - maintain garbage flag (activated while `<` unclosed)
#   - maintain delete next flag (briefly activated by `!`)
#   - with each new `{` increment score counter if not inside garbage
#   - if char isn't in [{, }, <, >] then just ignore
#   - skip over whatever comes next when delete next flag active (`!`)

def calculate_score(stream: str) -> tuple[int, int]:
    # Maintain for part 1 of problem
    total_score, prev_score = 0, 0
    garbage, delete_next = False, False

    # Maintain for part 2 of problem
    garbage_count = 0

    for chr in stream:
        # Reset delete_next after 1 iteration
        if delete_next: delete_next = False

        else:
            # Increment garbage count for part 2
            if garbage and chr not in [">", "!"]: garbage_count += 1

            if chr == "<": garbage = True

            elif chr == "!": delete_next = True
            
            elif chr == ">": garbage = False

            elif chr == "{":
                if not garbage:
                    prev_score += 1
                    total_score += prev_score
                    
            # Reset score nesting upon closed group 
            elif chr == "}":
                prev_score -= 1 if not garbage else 0

    return total_score, garbage_count


# Validate examples with unit tests
def run_tests() -> None:
    # Test part 1
    assert (calculate_score("{}")[0] == 1)
    assert (calculate_score("{{{}}}")[0] == 6)
    assert (calculate_score("{{},{}}")[0] == 5)
    assert (calculate_score("{{{},{},{{}}}}")[0] == 16)
    assert (calculate_score("{<a>,<a>,<a>,<a>}")[0] == 1)
    assert (calculate_score("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9)
    assert (calculate_score("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9)
    assert (calculate_score("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3)

    # Test part 2
    assert (calculate_score("<>")[1] == 0)
    assert (calculate_score("<random characters>")[1] == 17)
    assert (calculate_score("<<<<>")[1] == 3)
    assert (calculate_score("<{!>}>")[1] == 2)
    assert (calculate_score("<!!>")[1] == 0)
    assert (calculate_score("<!!>>")[1] == 0)
    assert (calculate_score("<{o'i!a,<{i<a>")[1] == 10)


if __name__ == "__main__":
    run_tests()
    
    stream_str = read_file(filename=INPUT_FILE)
    score, garbage = calculate_score(stream=stream_str)

    print(f"total score: {score} ... garbage count: {garbage}")

