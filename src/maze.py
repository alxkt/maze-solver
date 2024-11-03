from cell import Cell
import time

class Maze():
  def __init__(self, x, y, num_rows, num_cols, cell_width, cell_height, animation_delay=0.5, window=None):
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

    self._cells = self._create_cells()
    self._draw_cells()
    self._break_entrance_and_exit()

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