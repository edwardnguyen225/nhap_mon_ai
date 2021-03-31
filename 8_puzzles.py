# Giai bai toan 8-puzzle bang giai thuat DFS
################################

# init_state = list(9 phan tu), moi phan tu
# co gia tri tu 0-8, doi mot khac nhau
# Trong do, 0 the hien cho o rong


GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]
HORIZONTAL_LINE = "-------"


class Puzzle_node:
    def __init__(self, state, parent, previous_action="init"):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.previous_action = previous_action

    def __str__(self):
        puzzle = f'\nMove: {self.previous_action}'
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
        if blank_index in [0, 1, 2] or self.previous_action == "down":
            return

        # Swap the values.
        dest_index = blank_index - 3
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "up")

    def move_down(self):
        """Moves the blank tile down on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in [6, 7, 8] or self.previous_action == "up":
            return

        # Swap the values.
        dest_index = blank_index + 3
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "down")

    def move_left(self):
        """Moves the blank tile left on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in [0,3,6] or self.previous_action == "right":
            return

        # Swap the values.
        dest_index = blank_index - 1
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "left")

    def move_right(self):
        """Moves the blank tile right on the board. Returns new node as a child node."""
        new_state = self.state[:]
        blank_index = new_state.index(0)
        # Sanity check
        if blank_index in [2,5,8] or self.previous_action == "left":
            return

        # Swap the values.
        dest_index = blank_index + 1
        new_state[blank_index], new_state[dest_index] = new_state[dest_index], new_state[blank_index]
        return Puzzle_node(new_state, self.state, "right")


class DepthFirstSearch:
    pass


def main():
    new_state = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    tmp_node_0 = Puzzle_node(new_state, [])
    print(tmp_node_0)

    tmp_node_1 = tmp_node_0.move_up()
    print(tmp_node_1)

    tmp_node_2 = tmp_node_0.move_down()
    print(tmp_node_2)
    
    tmp_node_3 = tmp_node_0.move_left()
    print(tmp_node_3)
    
    tmp_node_4 = tmp_node_0.move_right()
    print(tmp_node_4)


if __name__ == '__main__':
    main()
