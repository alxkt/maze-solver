import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(0, 0, 5, 5, 10, 10)

    def test_create_cells(self):
        cells = self.maze._create_cells()
        self.assertEqual(len(cells), 5)
        self.assertEqual(len(cells[0]), 5)
        self.assertIsInstance(cells[0][0], Cell)

if __name__ == '__main__':
    unittest.main()