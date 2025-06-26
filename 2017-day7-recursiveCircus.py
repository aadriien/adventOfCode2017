###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 7 - Recursive Circus                                                 ##
###############################################################################


import re 

INPUT_FILE = "day7-input.txt"


class Node:
    def __init__(self, name: str, weight: int, children_names=None):
        self.name = name
        self.weight = weight
        self.children_names = children_names or [] 

        self.children = [] # actual node objects to be populated later


def read_file(filename: str) -> dict:
    # Hold created nodes with str name mapping
    programs = {}

    with open(filename, "r") as input:
        for line in input:
            # Example input lines: 
                # pbga (66)
                # fwft (72) -> ktlj, cntj, xhth
            input_parts = line.split("->")
            consistent = input_parts[0].strip()
            remaining = input_parts[1] if len(input_parts) > 1 else ""

            match = re.search(r"(\w+)\s*\((\d+)\)", consistent)

            # Parse str input to build node (with children array, if exists)
            if match:
                name = match.group(1)
                weight = int(match.group(2))

                children_names = [name.strip() for name in remaining.split(",")] if remaining else []
                
                # Map program name to node object for easy lookup later
                curr_program = Node(name, weight, children_names)
                programs[name] = curr_program

        return programs


def find_bottom(programs: dict) -> str:
    # Connect str children names to actual node objects
    for node in programs.values():
        node.children = [programs[child_name] for child_name in node.children_names]

    # Approach: get all names, determine which are children, then find non-child
    node_names = set(programs.keys())
    all_children = set()

    for node in programs.values():
        # Use `update` in context of set to add multiple elements / children
        all_children.update(node.children_names)

    not_child = (node_names - all_children).pop()
    return not_child


if __name__ == "__main__":
    programs = read_file(filename=INPUT_FILE)

    bottom = find_bottom(programs=programs)

    print(f"bottom program: {bottom}")

