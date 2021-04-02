# Solve the 8 puzzle problem with the DepthFirstSearch algorithm
################################

# init_state = list(n phan tu), moi phan tu
# co gia tri tu 0 - >(k*k-1), doi mot khac nhau
# Trong do, 0 the hien cho o rong

# Su dung deque thay vi list de implement stack
# vi deque thuc hien append va pop trong O(1)
# Con list thuc hien trong O(n)

from collections import deque
from math import sqrt


# Need to fix before make this file into a module
# Solution 1. Bring border into node, but it will waste memory
# index of each cell in N puzzle, with N = k*k - 1
# --------------------------------
# |  0  |   1   |   2   |...|k-1 |
# --------------------------------
# |  k  |  k+1  |  k+2  |...|2k-1|
# --------------------------------
# ...
# --------------------------------
# |k*k-k|k*k-k+1|k*k-k+2|...|k*k |
# --------------------------------
border_top = []
border_bottom = []
border_left = []
border_right = []


def is_puzzle(puzzle):
    # Check if puzzle is a square matrix
    width = sqrt(len(puzzle))
    if not width.is_integer():
        return False

    # Check all items in the puzzle are unique, and from 0 to Length - 1
    goal_list = range(0, len(puzzle))
    for i in goal_list:
        count = puzzle.count(i)
        if count != 1:
            return False

    return True


def create_border(size_of_puzzle):
    global border_top, border_bottom, border_left, border_right
    # The puzzle is a square matrix, then width = height
    width = int(sqrt(size_of_puzzle))
    border_top = list(range(0, width))
    border_left = list(range(0, width*width, width))
    border_right = list(map(lambda x: x + width-1, border_left))
    border_bottom = list(range(border_left[-1], border_right[-1]+1))


class Node:
    def __init__(self, state, parent=[], previous_action="init", depth=0):
        self.state = state
        self.parent = parent
        self.previous_action = previous_action
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth

    def __str__(self):
        puzzle = ""
        return puzzle

    def move_up(self):
        """Moves the blank tile up on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        global border_top
        if blank_index in border_top or self.previous_action == "down":
            return None

        # Swap the values.
        dest_index = blank_index - sqrt(len(self.state))
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Node(new_state, self.state, "up", self.depth+1)


class DepthFirstSearch:
    def __init__(self, init_state, goal_state=None):
        if not is_puzzle(init_state):
            raise ValueError("init_state must be square matrix")

        self.init_state = init_state
        size_of_puzzle = len(self.init_state)

        # Create global border of the puzzle
        create_border(size_of_puzzle)

        # Check goal state is valid.
        # Or create one if goal state is not input
        if goal_state is not None:
            if not is_puzzle(goal_state) or len(goal_state) != size_of_puzzle:
                raise ValueError("invalid goal state")
            self.goal_state = goal_state
        else:
            self.goal_state = list(range(1, size_of_puzzle))
            self.goal_state.append(0)

        self.solution = None


def main():
    pass


if __name__ == "__main__":
    main()
