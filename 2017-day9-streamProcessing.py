###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 9 - Stream Processing                                                ##
###############################################################################


INPUT_FILE = "day9-input.txt"


def read_file(filename: str) -> str:
    with open(filename, "r") as input:
        return input.read().strip()


def calculate_score(stream: str) -> int:
    # QUESTION: how many valid groups within a given group stream?

    # APPROACH:
    #   - maintain garbage flag (activated while `<` unclosed)
    #   - maintain delete next flag (briefly activated by `!`)
    #   - with each new `{` increment score counter if not inside garbage
    #   - if char isn't in [{, }, <, >] then just ignore
    #   - skip over whatever comes next when delete next flag active (`!`)

    total_score, prev_score = 0, 0
    garbage, delete_next = False, False

    for chr in stream:
        # Reset delete_next after 1 iteration
        if delete_next: delete_next = False

        else:
            if chr == "<":
                garbage = True

            elif chr == "!":
                delete_next = True
            
            elif chr == ">":
                garbage = False

            elif chr == "{":
                if not garbage:
                    prev_score += 1
                    total_score += prev_score
                    
            # Reset score nesting upon closed group 
            elif chr == "}":
                prev_score -= 1 if not garbage else 0

    return total_score


if __name__ == "__main__":
    stream_str = read_file(filename=INPUT_FILE)

    score = calculate_score(stream=stream_str)

    print(f"total score: {score}")

