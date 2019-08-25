import tkinter as tk
import math
import time
from tigr.lib.interface import AbstractDrawer
from tigr.lib.drawer.pen_config import pen_config as default_pen_config


class TkinterDrawer(AbstractDrawer, tk.Tk):
    name = 'tkinterDrawer'

    def __init__(self, pen_config=None):
        width = 800
        height = 800
        speed = 6
        if pen_config:
            self.pen_config = pen_config
        else:
            self.pen_config = default_pen_config
        if 'default' in self.pen_config:
            self._pencolor = self.pen_config['default']['color']
            self._pensize = self.pen_config['default']['size']
        super().__init__()
        self.title("Tkinter drawer")
        self.geometry("800x800")
        # self._pencolor = str(pencolor)
        # self._pensize = int(pensize)
        self.speed(int(speed))
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack(side=tk.TOP, fill=tk.X)
        self.home_pos = (width/2, height/2)
        self.pos = {
            'x': width/2,
            'y': height/2
        }
        self.angle = {
            'N': 90,
            'S': 270,
            'E': 0,
            'W': 180,
        }
        self._pendown = True
        self._heading = 90

    def setheading(self, direction):
        self._heading = direction

    def select_pen(self, pen_num):
        if int(pen_num) not in self.pen_config:
            print('invalid pen number: {}'.format(pen_num))
        else:
            self._pencolor = self.pen_config[int(pen_num)]['color']
            self._pensize = self.pen_config[int(pen_num)]['size']

    def pen_down(self):
        self._pendown = True

    def pen_up(self):
        self._pendown = False

    def forward(self, length):
        x, y = self.get_location(self._heading, length)
        if self._pendown:
            self._draw_line(x, y)
        else:
            self.go_to(x, y)

        self.update()

    def go_along(self, along):
        if along > 0:
            heading = 180
        else:
            heading = 270
        self.setheading(heading)
        self.forward(abs(along))

    def bye(self):
        self.quit()
        self.update()
        time.sleep(0.5)

    def speed(self, speed):
        wait = 1 / speed
        if speed <= 0: wait = 1
        self.wait = wait

    def go_down(self, down):
        if down > 0:
            heading = 90
        else:
            heading = 0
        self.setheading(heading)
        self.forward(abs(down))

    def go_to(self, x, y):
        self.pos['x'] = x
        self.pos['y'] = y
        self.update()

    def update(self):
        super().update()
        time.sleep(self.wait)

    def draw_line(self, direction, distance):
        # to get same behaviour as turtle

        direction = self.angle[direction] + 90
        self._heading = direction
        x, y = self.get_location(direction, distance)

        if not self._pendown:
            self.pen_down()
            self._draw_line(x, y)
            self.pen_up()
        else:
            self._draw_line(x, y)

    def _draw_line(self, x, y):
        self.canvas.create_line(self.pos['x'], self.pos['y'], x, y, fill=self._pencolor, width=self._pensize)
        self.go_to(x, y)
        self.update()

    def get_location(self, direction, length):
        return (self.pos['x'] + math.sin(math.radians(direction)) * length,
                self.pos['y'] + math.cos(math.radians(direction)) * length)

    @property
    def heading(self):
        return self._heading - 90




