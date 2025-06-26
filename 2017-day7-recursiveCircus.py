###############################################################################
##  Advent of Code (2017)                                                    ##
##                                                                           ##
##  Day 7 - Recursive Circus                                                 ##
###############################################################################


import re 
from collections import Counter

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


# Part 1 of problem
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


# Part 2 of problem
def find_weight(programs: dict, bottom_name: str) -> int:
    # Helper function to get program's total weight (stacked tower)
    def check_weights(node: Node) -> tuple[int, int]:
        if not node.children:
            return node.weight, None

        children_weights = [check_weights(child) for child in node.children]

        for total_weight, fix in children_weights:
            if fix is not None:
                return 0, fix

        child_weights = [weight for weight, _ in children_weights]

        # Check for consistent weights
        if len(set(child_weights)) > 1:
            weight_counts = Counter(child_weights)

            # We know there's an imbalance, so now determine which one
            correct_weight = [w for w in weight_counts if weight_counts[w] > 1][0]
            wrong_weight = [w for w in weight_counts if weight_counts[w] == 1][0]

            for i in range(len(node.children)):
                if child_weights[i] == wrong_weight:
                    # Determine difference from wrong child 
                    wrong_child = node.children[i]
                    diff = correct_weight - wrong_weight

                    fixed_weight = wrong_child.weight + diff
                    return 0, fixed_weight 

        return node.weight + sum(child_weights), None

    bottom_node = programs[bottom_name]
    total, fix = check_weights(bottom_node)
    return fix
        

if __name__ == "__main__":
    programs = read_file(filename=INPUT_FILE)

    bottom = find_bottom(programs=programs)
    fixed_weight = find_weight(programs=programs, bottom_name=bottom)

    print(f"bottom program: {bottom} ... balanced weight: {fixed_weight}")

