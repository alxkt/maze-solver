from cell import Cell
import time
import random

class Maze():
  def __init__(self, x, y, num_rows, num_cols, cell_width, cell_height, animation_delay=0.5, window=None, seed=None):
    """
    Initialize the maze with the given parameters
    """
    self.__win = window
    self.x = x
    self.y = y
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_width = cell_width
    self.cell_height = cell_height
    self.animation_delay = animation_delay
    self.seed = random.Random(seed)

    self._cells = self._create_cells()
    self._draw_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)

  def _create_cells(self):
    """
    Create and return a 2D list of cells
    """
    rows = []
    for i in range(self.num_rows):
      cols = []
      for j in range(self.num_cols):
        cols.append(Cell(
          self.x + j * self.cell_width,
          self.y + i * self.cell_height,
          self.cell_width,
          self.cell_height,
          window=self.__win
        ))
      rows.append(cols)
    return rows
  
  def _draw_cells(self):
    """
    Draw all the cells in the maze
    """
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        self._draw_cell(i, j)
        self._animate()

  def _draw_cell(self, i, j):
    """
    Draw the cell at the given row and column
    """
    self._cells[i][j].draw()

  def _animate(self):
    """
    Redraw the window after a delay
    """
    if self.__win is not None:
      self.__win.redraw()
      time.sleep(self.animation_delay)
    
  def _break_entrance_and_exit(self):
    """
    Break the entrance and exit of the maze
    """
    self._cells[0][0].has_top_wall = False
    self._cells[0][0].draw()
    self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
    self._cells[self.num_rows - 1][self.num_cols - 1].draw()

  def _break_walls_r_old(self, i, j):
    """
    Recursively break walls to create the maze
    """
    unvisited_adjacent_cells = []
    if i > 0 and not self._cells[i - 1][j].visited:
      unvisited_adjacent_cells.append((i - 1, j))
    if j > 0 and not self._cells[i][j - 1].visited:
      unvisited_adjacent_cells.append((i, j - 1))
    if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
      unvisited_adjacent_cells.append((i + 1, j))
    if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
      unvisited_adjacent_cells.append((i, j + 1))

    if len(unvisited_adjacent_cells) == 0:
      return

    next_i, next_j = unvisited_adjacent_cells[self.seed.randint(0, len(unvisited_adjacent_cells) - 1)]
    self._cells[i][j].visited = True
    self._cells[next_i][next_j].visited = True
    # I need to remove the walls between the two cells by setting for example, in a move to the right, current cell's right wall to False and next cell's left wall to False
    if next_i < i:
      self._cells[i][j].has_top_wall = False
      self._cells[next_i][next_j].has_bottom_wall = False
    elif next_i > i:
      self._cells[i][j].has_bottom_wall = False
      self._cells[next_i][next_j].has_top_wall = False
    elif next_j < j:
      self._cells[i][j].has_left_wall = False
      self._cells[next_i][next_j].has_right_wall = False
    elif next_j > j:
      self._cells[i][j].has_right_wall = False
      self._cells[next_i][next_j].has_left_wall = False

    self._draw_cell(i, j)
    self._draw_cell(next_i, next_j)
    self._break_walls_r(next_i, next_j)
  def _break_walls_r(self, i, j):
    """
    Recursively break walls to create the maze using DFS with backtracking
    """
    self._cells[i][j].visited = True

    directions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    self.seed.shuffle(directions)  # Shuffle directions to ensure randomness

    for next_i, next_j in directions:
        if 0 <= next_i < self.num_rows and 0 <= next_j < self.num_cols and not self._cells[next_i][next_j].visited:
            # Remove walls between current cell and next cell
            if next_i < i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif next_i > i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif next_j < j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif next_j > j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            self._draw_cell(i, j)
            self._draw_cell(next_i, next_j)
            self._animate()

            self._break_walls_r(next_i, next_j)
