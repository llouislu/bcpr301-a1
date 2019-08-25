import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tigr.lib.drawer.turtle_drawer import TurtleDrawer
from tigr.lib.drawer.pen_config import pen_config as default_pen_config


class TestCasetTurtleDrawer(unittest.TestCase):

    def setUp(self):
        self.instance = TurtleDrawer()

    def test_pencolor(self):
        self.instance.pencolor('red')
        self.assertEqual(self.instance.pencolor(), 'red')
        self.instance.pencolor('black')
        self.assertEqual(self.instance.pencolor(), 'black')

    def test_pensize(self):
        self.instance.pensize(4)
        self.assertEqual(self.instance.pensize(), 4)
        self.instance.pensize(10)
        self.assertNotEqual(not self.instance.pensize(), 10)

    def test_draw_line(self):
        self.instance.pen_up()
        self.instance.draw_line('N', 100)
        self.assertTrue(self.instance.isdown() == True)
        self.instance.pen_up()
        self.instance.draw_line('S', 100)
        self.assertTrue(self.instance.isdown() == True)

    def test_pen_down(self):
        self.instance.pen_down()
        self.assertTrue(self.instance.isdown())

    def test_pen_up(self):
        self.instance.pen_up()
        self.assertFalse(self.instance.isdown())

    def test_go_along(self):
        self.instance.setposition(0,0)
        self.instance.go_along(100)
        self.assertTrue(self.instance.pos() == (100,0))

    def test_go_down(self):
        self.instance.setposition(0,0)
        self.instance.go_down(100)
        self.assertTrue(self.instance.pos() == (0,100))


    def test_select_pen_color(self):
        self.instance.select_pen(1)
        self.assertTrue(self.instance.pencolor() == 'blue')
        old_pencolor = self.instance.pencolor()
        self.instance.select_pen(10)
        self.assertTrue(self.instance.pencolor() == old_pencolor)

    def test_select_pen_size(self):
        self.instance.select_pen(1)
        self.assertTrue(self.instance.pensize() == 1)
        self.instance.select_pen(10)
        self.assertFalse(self.instance.pensize() == 10)

    def test_check_draw_line_degree(self):
        self.assertTrue(self.instance.draw_degrees.get('N', -1) == 90)
        self.assertTrue(self.instance.draw_degrees.get('E', -1) == 0)
        self.assertTrue(self.instance.draw_degrees.get('S', -1) == 270)
        self.assertTrue(self.instance.draw_degrees.get('W', -1) == 180)

if __name__ == '__main__':
    unittest.main()