from tigr.lib.interface import AbstractParser

class BaseParser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.no_parameter_commands = {
            'D': self.drawer.pen_down,
            'U': self.drawer.pen_up
        }

        self.one_parameter_commands = {
            'P': self.drawer.select_pen,
            # 'G': self.drawer.goto,
            'X': self.drawer.go_along,
            'Y': self.drawer.go_down,
        }
        self.draw_commands = {
            'N': self.drawer.draw_line,
            'E': self.drawer.draw_line,
            'S': self.drawer.draw_line,
            'W': self.drawer.draw_line,
        }
        self.draw_degrees = {
            'N': 0,
            'E': 90,
            'S': 180,
            'W': 270
        }

    def is_float(self, string):
        try:
            float(string)
        except:
            return False
        return True


    def draw(self):
        if self.command not in self.no_parameter_commands:
            if not self.is_float(self.data):
                raise ValueError()
            self.data = float(self.data)

        if self.command in self.no_parameter_commands:
            self.no_parameter_commands[self.command]()
        elif self.command in self.one_parameter_commands:
            self.one_parameter_commands[self.command](self.data)
        elif self.command in self.draw_commands:
            self.draw_commands[self.command](
                self.draw_degrees[self.command], self.data)
