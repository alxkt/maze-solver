from window import *
from cell import Cell
from maze import Maze

def main():
  win = Window(800, 600)
  p1 = Point(10,15)
  # cell = Cell(win, p1.x, p1.y, 20, 20)
  # cell.draw()
  # cell2 = Cell(win, 10, 50, 20, 20)
  # cell2.has_left_wall = False
  # cell2.draw()
  # cell.draw_move(cell2, undo=True)
  maze = Maze(win, 10, 10, 5, 15, 20, 20, 0.1)

  win.wait_for_close()

main()