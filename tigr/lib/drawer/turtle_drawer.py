import turtle
from tigr.lib.interface import AbstractDrawer

class TurtleDrawer(AbstractDrawer, turtle.Turtle):
    def __init__(self):
        super().__init__()
        # super(turtle.Screen, self).__init__()
        # super(AbstractDrawer, self).__init__()
        # self.mode = 'logo'
        self.__name__ = 'turtle'

    def select_pen(self, pen_num):
        pass

    def pen_down(self):
        self.pendown()

    def pen_up(self):
        self.penup()

    def go_along(self, along):
        x, y = self.pos()
        self.goto(x+along, y)

    def go_down(self, down):
        x, y = self.pos()
        self.goto(x, y+down)

    def draw_line(self, direction, distance):
        self.pen_down()
        self.setheading(direction)
        self.forward(distance)