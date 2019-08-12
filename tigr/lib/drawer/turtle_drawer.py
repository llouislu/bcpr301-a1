import turtle
from tigr.lib.interface import AbstractDrawer

class TurtleDrawer(AbstractDrawer):
    def __init__(self):
        turtle.mode(mode='logo')
        self.turtle = turtle.Turtle()

    def __del__(self):
        turtle.mainloop()

    def select_pen(self, pen_num):
        pass

    def pen_down(self):
        self.turtle.pendown()

    def pen_up(self):
        self.turtle.penup()

    def go_along(self, along):
        x, y = self.pos
        self.turtle.goto(x+along, y)

    def go_down(self, down):
        x, y = self.pos
        self.turtle.goto(x, y+down)

    def draw_line(self, direction, distance):
        self.pen_down()
        self.turtle.setheading(direction)
        self.turtle.forward(distance)

    @property
    def pos(self):
        return self.turtle.pos()
