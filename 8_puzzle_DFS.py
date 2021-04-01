# Solve the 8 puzzle problem with the DepthFirstSearch algorithm
################################

# init_state = list(9 phan tu), moi phan tu
# co gia tri tu 0-8, doi mot khac nhau
# Trong do, 0 the hien cho o rong

# Su dung deque thay vi list de implement stack
# vi deque thuc hien append va pop trong O(1)
# Con list thuc hien trong O(n)
from collections import deque
import time
import random

# index of each cell
# -------
# |0|1|2|
# -------
# |3|4|5|
# -------
# |6|7|8|
# -------
BORDER_TOP = [0, 1, 2]
BORDER_BOTTOM = [6, 7, 8]
BORDER_LEFT = [0, 3, 6]
BORDER_RIGHT = [2, 5, 8]

# GOAL_STATE when displayed
# -------
# |1|2|3|
# -------
# |4|5|6|
# -------
# |7|8|0|
# -------
GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

HORIZONTAL_LINE = "-------"
MSG_GOAL_FOUND = "Goal found"
MSG_NO_SOLUTION = "No solution"


class Puzzle_node:
    def __init__(self, state, parent, previous_action="init", depth=0):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.previous_action = previous_action
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth

    def __str__(self):
        puzzle = f'\nStep: {self.depth} - Move: {self.previous_action}'
        puzzle += f'\n{HORIZONTAL_LINE}'
        puzzle += f'\n|{self.state[0]}|{self.state[1]}|{self.state[2]}|'
        puzzle += f'\n{HORIZONTAL_LINE}'
        puzzle += f'\n|{self.state[3]}|{self.state[4]}|{self.state[5]}|'
        puzzle += f'\n{HORIZONTAL_LINE}'
        puzzle += f'\n|{self.state[6]}|{self.state[7]}|{self.state[8]}|'
        puzzle += f'\n{HORIZONTAL_LINE}'
        return puzzle

    def move_up(self):
        """Moves the blank tile up on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in BORDER_TOP or self.previous_action == "down":
            return

        # Swap the values.
        dest_index = blank_index - 3
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "up", self.depth+1)

    def move_down(self):
        """Moves the blank tile down on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in BORDER_BOTTOM or self.previous_action == "up":
            return

        # Swap the values.
        dest_index = blank_index + 3
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "down", self.depth+1)

    def move_left(self):
        """Moves the blank tile left on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in BORDER_LEFT or self.previous_action == "right":
            return

        # Swap the values.
        dest_index = blank_index - 1
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "left", self.depth+1)

    def move_right(self):
        """Moves the blank tile right on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in BORDER_RIGHT or self.previous_action == "left":
            return

        # Swap the values.
        dest_index = blank_index + 1
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "right", self.depth+1)


def expand_node(node):
    children_nodes = deque()
    children_nodes.append(node.move_left())
    children_nodes.append(node.move_up())
    children_nodes.append(node.move_right())
    children_nodes.append(node.move_down())
    # Shuffle to avoid being trapped in a loop
    random.shuffle(children_nodes)
    # Filter the list and remove the nodes that are impossible (move function returned None)
    # list comprehension!
    children_nodes = filter(lambda x: x != None, children_nodes)
    return children_nodes


class DepthFirstSearch:
    def __init__(self, init_state, goal_state):
        self.init_state = init_state
        self.goal_state = goal_state
        self.solution = None

    def print_solution(self):
        if self.solution is None:
            print(MSG_NO_SOLUTION)
            return

        for step in self.solution:
            print(step)

    def search(self):
        """ Process the DepthFirstSearch
            return True if the solution is found
            otherwise, return False"""
        stack = deque()
        stack.append(Puzzle_node(self.init_state, None))

        self.solution = deque()

        while len(stack) > 0:
            node = stack.pop()
            # print(node)
            self.solution.append(node)

            if node.state == self.goal_state:
                print(MSG_GOAL_FOUND)
                return True

            expanded_nodes = expand_node(node)
            stack.extend(expanded_nodes)

        print(MSG_NO_SOLUTION)
        self.solution = None
        return False


def main():
    # 123406758
    new_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]

    DFS = DepthFirstSearch(new_state, GOAL_STATE)
    DFS.search()
    DFS.print_solution()


if __name__ == '__main__':
    main()
