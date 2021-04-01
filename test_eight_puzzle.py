import unittest
from eight_puzzle_DFS import DepthFirstSearch


class Test8Puzzle(unittest.TestCase):
    def test_goal_puzzle(self):
        """Test with input puzzle is already at goal state"""
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        DFS = DepthFirstSearch(puzzle)
        result = DFS.search()
        self.assertTrue(result)

    def test_simple_puzzle_00(self):
        """ From goal state, move blank cell left
            This is the simple puzzle"""
        puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        DFS = DepthFirstSearch(puzzle)
        result = DFS.search()
        self.assertTrue(result)

    def test_simple_puzzle_01(self):
        """ From goal state, move blank cell up
            This is the simple puzzle"""
        puzzle = [1, 2, 3, 4, 5, 0, 7, 8, 6]
        DFS = DepthFirstSearch(puzzle)
        result = DFS.search()
        self.assertTrue(result)

    def test_simple_puzzle_02(self):
        """ Continue with puzzle from test_simple_puzzle_00,
            move blank cell left again"""
        puzzle = [1, 2, 3, 4, 5, 6, 0, 7, 8]
        DFS = DepthFirstSearch(puzzle)
        result = DFS.search()
        self.assertTrue(result)

    def test_simple_puzzle_03(self):
        """ From goal state, move blank cell left, then up, to replace value 5"""
        puzzle = [1, 2, 3, 4, 0, 6, 7, 5, 8]
        DFS = DepthFirstSearch(puzzle)
        result = DFS.search()
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
