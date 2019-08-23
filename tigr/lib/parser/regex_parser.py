from tigr.lib.interface import AbstractParser
import re

class ParseException(Exception):
    pass

class SkipParseException(Exception):
    pass

class RegexParser(AbstractParser):
    line_pattern = re.compile(
        r'^(P|X|Y|D|W|N|E|S|U)\s{0,}(-?\d{0,}\.{0,1}\d{0,})\s{0,}(?=#{0,1})')

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

    def parse(self, raw_source):
        for line_number, line in enumerate(raw_source, 1):
            try:
                self.parse_line(line_number, line)
            except ParseException:
                print('you have a syntax error at Line {}: "{}"'.format(line_number, line))
                continue
            except SkipParseException:
                continue

    def parse_line(self, line_number, line):
        line = line.strip()
        line_uppercased = line.upper()
        if not line_uppercased:
            return
        if line_uppercased.startswith('#'):
            raise SkipParseException()
        matched = self.line_pattern.match(line_uppercased)
        if not matched:
            raise ParseException()
        else:
            self.command, self.data = matched.groups()
            if self.command not in self.no_parameter_commands:
                if not self.is_float(self.data):
                    raise ParseException()
                self.data = float(self.data)
            self.draw()

    def is_float(self, string):
        try:
            float(string)
        except:
            return False
        return True

    def draw(self):

        if self.command in self.no_parameter_commands:
            self.no_parameter_commands[self.command]()
        elif self.command in self.one_parameter_commands:
            self.one_parameter_commands[self.command](self.data)
        elif self.command in self.draw_commands:
            self.draw_commands[self.command](
                self.command, self.data)