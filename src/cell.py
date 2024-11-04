from window import *

class Cell():
  def __init__(self, x, y, width, height, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, window=None):
    self.__window = window
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall
    self.visited = False

  def draw(self):
    left = Line(Point(self.x, self.y), Point(self.x, self.y + self.height))
    right = Line(Point(self.x + self.width, self.y), Point(self.x + self.width, self.y + self.height))
    top = Line(Point(self.x, self.y), Point(self.x + self.width, self.y))
    bottom = Line(Point(self.x, self.y + self.height), Point(self.x + self.width, self.y + self.height))

    color = "red"
    clear_color = "black"
    if self.__window is not None:
      if self.has_left_wall:
        self.__window.draw_line(left, color)
      else:
        self.__window.draw_line(left, clear_color)

      if self.has_right_wall:
        self.__window.draw_line(right, color)
      else:
        self.__window.draw_line(right, clear_color)

      if self.has_top_wall:
        self.__window.draw_line(top, color)
      else:
        self.__window.draw_line(top, clear_color)

      if self.has_bottom_wall:
        self.__window.draw_line(bottom, color)
      else:
        self.__window.draw_line(bottom, clear_color)

  def draw_move(self, target_cell, undo=False):
    start = Point(self.x + self.width/2, self.y + self.height/2)
    end = Point(target_cell.x + target_cell.width/2, target_cell.y + target_cell.height/2)
    line = Line(start, end)
    color = "red"
    if undo: color = "gray"
    if self.__window is not None:
      self.__window.draw_line(line, color)