import pygame
# from tigr.lib.interface import AbstractDrawer
# from tigr.lib.drawer.pen_config import pen_config as default_pen_config


pygame.init()

class PyGameDrawer():

    def __init__(self, pen_config=None):
        super().__init__()
        self.width = 800
        self.height = 600
        self.pen_state = False
        self.x = 0
        self.y = 0
        self.window = pygame.display.set_mode((self.width, self.height))
        self._update()
        self.window.fill([255,255,255])
        self.pen_color = (0, 0, 0)
        self.pen_size = 10

    def select_pen(self, pen_num):
        pass

    def pen_down(self):
        self.pen_state = True

    def pen_up(self):
        self.pen_state = False

    def go_along(self, along):
        new_x = self.x + along
        new_y = self.y
        if self.pen_state:
            old_x = self.x
            old_y = self.y
            pygame.draw.line(self.window, self.pen_color, (old_x, old_y),
                             (new_x, new_y), 1)
        self.x += along

    def go_down(self, down):
        new_x = self.x
        new_y = self.y + down
        if self.pen_state:
            old_x = self.x
            old_y = self.y
            self._do_draw_line()
            pygame.draw.line(self.window, self.pen_color, (old_x, old_y),
                             (new_x, new_y), 1)
        self.y += down

    def draw_line(self, direction, distance):
        if 'N':
            self._do_draw_line((self.x, self.y), (self.x, self.y + distance))
        elif 'S':
            self._do_draw_line((self.x, self.y), (self.x, self.y - distance))
        elif 'W':
            self._do_draw_line((self.x, self.y), (self.x - distance, self.y))
        elif 'E':
            self._do_draw_line((self.x, self.y), (self.x + distance, self.y))

    def _update(self):
        pygame.display.update()

    def _do_draw_line(self, old_pos, new_pos):
        print(old_pos, new_pos)
        old_x, old_y = old_pos
        new_x, new_y = new_pos
        # y axis direction:
        # go north is positive diff
        # go south is negative diff
        # reality in pygame is reversed
        diff_y = new_y - old_y
        real_diff_y = - diff_y
        new_y += real_diff_y

        # map the origin point to top-left point of canvas
        real_old_x, real_old_y = old_x + (self.width / 2), old_y + (self.height / 2)
        real_new_x, real_new_y = new_x + (self.width / 2), new_y + (self.height / 2)
        print(real_old_x, real_old_y)
        print(real_new_x, real_new_y)
        
        pygame.draw.line(self.window, self.pen_color,
                         (real_old_x, real_old_y), (real_new_x, real_new_y), self.pen_size)
        pygame.display.update()
        self._update()

    def test(self):
        pygame.draw.line(self.window, (0,0,0), (400,300), (600, 500), 10)
        self._update()


import time
d = PyGameDrawer()
d.draw_line('N', 100)
print()
exit()
d.test()
time.sleep(3)
exit()

d.pen_down()
d.go_along(100)
# d.test()