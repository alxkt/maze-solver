from window import *

def main():
  win = Window(800, 600)
  p1 = Point(10,15)
  p2 = Point(350, 400)
  line = Line(p1, p2)
  win.draw_line(line, "red")
  win.wait_for_close()

main()