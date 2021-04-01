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


class NPuzzle:
    def __init__(self, puzzle):
        if not is_puzzle(puzzle):
            raise ValueError
        self.puzzle = puzzle

    def __str__(self):
        displayed_puzzle = ""
        return displayed_puzzle


class Node:
    def __init__(self, state, parent=[], previous_action="init", depth=0):
        # Contains the state of the node
        self.state = NPuzzle(state)
        # Contains the node that generated this node
        self.parent = NPuzzle(parent)
        # Contains the operation that generated this node from the parent
        self.previous_action = previous_action
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth

    def __str__(self):
        return str(self.state)

    def move_up(self):
        """Moves the blank tile up on the board. Returns new node as a child node."""
