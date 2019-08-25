import turtle
from tigr.lib.interface import AbstractDrawer
from tigr.lib.drawer.pen_config import pen_config as default_pen_config

class TurtleDrawer(AbstractDrawer, turtle.Turtle):
    def __init__(self, pen_config=None):
        super().__init__()
        # super(turtle.Screen, self).__init__()
        # super(AbstractDrawer, self).__init__()
        # self.mode = 'logo'
        self.__name__ = 'turtle'
        if pen_config:
            self.pen_config = pen_config
        else:
            self.pen_config = default_pen_config
        if 'default' in self.pen_config:
            self.pencolor(self.pen_config['default']['color'])
            self.pensize(self.pen_config['default']['size'])
        self.draw_degrees = {
            'N': 90 * 1,
            'E': 90 * 0,
            'S': 90 * 3,
            'W': 90 * 2
        }

    def select_pen(self, pen_num):
        pen_num = int(pen_num)
        if int(pen_num) not in self.pen_config:
            print('invalid pen number: {}'.format(pen_num))
        self.pencolor(self.pen_config[int(pen_num)]['color'])
        self.pensize(self.pen_config[int(pen_num)]['size'])

    def pen_down(self):
        self.pendown()

    def pen_up(self):
        self.penup()

    def go_along(self, along):
        x, y = self.pos()
        self.goto(x + along, y)

    def go_down(self, down):
        x, y = self.pos()
        self.goto(x, y + down)

    def draw_line(self, direction, distance):
        self.pen_down()
        self.setheading(self.draw_degrees[direction])
        self.forward(distance)
