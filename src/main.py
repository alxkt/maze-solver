from window import *
from maze import Maze

def main():
  win = Window(800, 600)

  maze = Maze(10, 10, 15, 15, 20, 20, animation_delay=0.01, window=win)
  maze.solve()

  win.wait_for_close()

main()