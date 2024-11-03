import sys
import os
import unittest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):

    def test_create_cells(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        cells = m1._create_cells()
        self.assertEqual(len(cells), 5)
        self.assertEqual(len(cells[0]), 5)
        self.assertIsInstance(cells[0][0], Cell)
    
    def test_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 5, 5, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[4][4].has_bottom_wall)

if __name__ == '__main__':
    unittest.main()