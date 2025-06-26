###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 7 - Recursive Circus                                                 ##
###############################################################################


import re 

INPUT_FILE = "day7-input.txt"


class Node:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children = [] 


def read_file(filename: str) -> Node:
    # Start with placeholder head to hold tower programs
    root = Node("null", 0)

    # Example input lines: 
        # pbga (66)
        # fwft (72) -> ktlj, cntj, xhth
    pattern = r"^\s*(\w+)\s*\(\s*(\d+)\s*\)\s*->\s*(.*)$"

    with open(filename, "r") as input:
        for line in input:
            match = re.search(pattern, line)

            # Parse str input to build node (with children array, if exists)
            if match:
                name = match.group(1)
                weight = int(match.group(2))
                children = match.group(3).split()

                print(f"name: {name}, weight: {weight}, children: {children}")
                
                curr_program = Node(name, weight)
                curr_program.children = children

                root.children.append(curr_program)

        return root


def find_bottom(root_placeholder: Node) -> str:
    return


if __name__ == "__main__":
    root_placeholder = read_file(filename=INPUT_FILE)



