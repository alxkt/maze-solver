
from tkinter import Tk, BOTH, Canvas

class Window():
  def __init__(self, width, height):
    self.root = Tk()
    self.root.title = "My window"
    self.canvas = Canvas(height=height, width=width)
    self.canvas.pack()
    self.running = False

    self.root.protocol("WM_DELETE_WINDOW", self.close)

  def redraw(self):
    self.root.update_idletasks()
    self.root.update()

  def wait_for_close(self):
    self.running = True
    while(self.running):
      self.redraw()

  def close(self):
    self.running = False

def main():
  win = Window(800, 600)
  win.wait_for_close()

main()