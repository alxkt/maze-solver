from window import *
from cell import Cell

def main():
  win = Window(800, 600)
  p1 = Point(10,15)
  cell = Cell(win, p1.x, p1.y, 20, 20)
  cell.draw()
  cell2 = Cell(win, 10, 50, 20, 20)
  cell2.has_left_wall = False
  cell2.draw()
  cell.draw_move(cell2, undo=True)
  win.wait_for_close()

main()