import unittest
from n_puzzle_DFS import *


class Test8Puzzle(unittest.TestCase):
    def test_valid_8_puzzle_00(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(is_puzzle(puzzle))

    def test_valid_8_puzzle_01(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 0, 8]
        self.assertTrue(is_puzzle(puzzle))

    def test_valid_8_puzzle_02(self):
        puzzle = [1, 2, 3, 4, 5, 0, 7, 8, 6]
        self.assertTrue(is_puzzle(puzzle))

    def test_invalid_8_puzzle_00(self):
        puzzle = [1, 2, 3, 4, 0, 6, 7, 8, 0]
        self.assertFalse(is_puzzle(puzzle))

    def test_invalid_8_puzzle_01(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 8]
        self.assertFalse(is_puzzle(puzzle))

    def test_invalid_8_puzzle_02(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertFalse(is_puzzle(puzzle))

    def test_valid_16_puzzle_00(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.assertTrue(is_puzzle(puzzle))

    def test_valid_16_puzzle_01(self):
        puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertTrue(is_puzzle(puzzle))
        
    def test_invalid_16_puzzle_00(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15]
        self.assertFalse(is_puzzle(puzzle))
        
    def test_invalid_16_puzzle_01(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertFalse(is_puzzle(puzzle))

    def test_invalid_puzzle_not_square_matrix_00(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9]
        self.assertFalse(is_puzzle(puzzle))

    def test_invalid_puzzle_not_square_matrix_01(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.assertFalse(is_puzzle(puzzle))


if __name__ == '__main__':
    unittest.main()
