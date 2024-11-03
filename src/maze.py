from cell import Cell
import time

class Maze():
  def __init__(self, win, x, y, num_rows, num_cols, cell_width, cell_height, animation_delay=0.5):
    self.__win = win
    self.x = x
    self.y = y
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_width = cell_width
    self.cell_height = cell_height
    self.animation_delay = animation_delay

    self._cells = self._create_cells()
    self._draw_cells()

  def _create_cells(self):
    rows = []
    for i in range(self.num_rows):
      cols = []
      for j in range(self.num_cols):
        cols.append(Cell(
          self.__win,
          self.x + j * self.cell_width,
          self.y + i * self.cell_height,
          self.cell_width,
          self.cell_height
        ))
      rows.append(cols)
    return rows
  
  def _draw_cells(self):
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        self._draw_cell(i, j)
        self._animate()

  def _draw_cell(self, i, j):
    self._cells[i][j].draw()

  def _animate(self):
    # call the redraw method of the window and sleep for 0.5 seconds
    self.__win.redraw()
    time.sleep(self.animation_delay)