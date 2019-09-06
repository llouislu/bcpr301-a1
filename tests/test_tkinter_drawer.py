import unittest
from tigr.lib.drawer.tkinter_drawer import TkinterDrawer
from tigr.lib.drawer.pen_config import pen_config as default_pen_config


class TestCasetTkinterDrawer(unittest.TestCase):

    def setUp(self):
        self.instance = TkinterDrawer()
    
    def test_penconfig(self):
        self.instance_with_vendor_config = TkinterDrawer(
            pen_config=default_pen_config)
        self.assertTrue(
            self.instance_with_vendor_config.pen_config)

        user_pen_config = default_pen_config
        user_pen_config['default'] = default_pen_config[6]
        self.instance_user_config = TkinterDrawer(pen_config=user_pen_config)
        self.assertTrue(
            self.instance_user_config._pencolor == 'green')
        self.assertTrue(
            self.instance_user_config._pensize == 10)

    def test_select_pen(self):
        self.instance.select_pen(1)
        self.assertTrue(self.instance._pencolor == 'blue')
        self.assertTrue(self.instance._pensize == 1)

        self.instance.select_pen(100)
        self.assertTrue(self.instance._pencolor == 'blue')
        self.assertTrue(self.instance._pensize == 1)

    def test_pen_down(self):
        self.instance.pen_down()
        self.assertTrue(self.instance._pendown)

    def test_pen_up(self):
        self.instance.pen_up()
        self.assertFalse(self.instance._pendown)
    
    def test_go_along(self):
        old_x = self.instance.pos['x']
        old_y = self.instance.pos['y']
        self.instance.go_along(100)
        self.assertFalse(self.instance.pos['y'] == old_y)
        self.instance.go_along(-100)
        self.assertFalse(old_x == self.instance.pos['x'])
    
    def test_go_down(self):
        old_x = self.instance.pos['x']
        old_y = self.instance.pos['y']
        self.instance.go_down(100)
        self.assertFalse(self.instance.pos['x'] == old_x)
        self.instance.go_down(-100)
        self.assertFalse(old_y == self.instance.pos['y'])

    def test_draw_line(self):
        self.instance.pen_up()
        self.instance.draw_line('N', 100)
        self.assertFalse(self.instance._pendown)

        self.instance.pen_down()
        self.instance.draw_line('E', 100)
        self.assertTrue(self.instance._pendown)

if __name__ == '__main__':
    unittest.main()
