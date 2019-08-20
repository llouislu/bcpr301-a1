from parsimonious import Grammar
from parsimonious.nodes import NodeVisitor
from tigr.lib.interface import AbstractParser


class TigrVisitor(NodeVisitor):
    def visit_line(self, node, visited_children):
        """ Makes a dict of the section (as key) and the key/value pairs. """
        s, *_ = visited_children
        return s

    def visit_statement(self, node, visited_children):
        directive, _, parameter = visited_children
        if parameter:
            return directive.text, parameter[0].text
        else:
            return directive.text, ''

    def generic_visit(self, node, visited_children):
        """ The generic visit method. """
        return visited_children or node


class PegParser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0

        self.peg_grammar = Grammar(r'''
            line = statement ws? comment? ws
            statement   = directive ws? parameter?
            directive   = ~"P|X|Y|D|W|N|E|S|U"
            parameter   = ~"-?\d{0,}\.{0,1}\d{0,}"
            comment     = ~"#.*"
            ws          = ~"\s*"
        ''')
        self.peg_visitor = TigrVisitor()

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
            'N': 90 * 1,
            'E': 0,
            'S': 90 * 3,
            'W': 90 * 2
        }

    def parse(self, raw_source):
        for line in raw_source:
            line = line.strip()
            if not line:
                continue
            ast = self.peg_grammar.parse(line)
            print(self.peg_visitor)
            self.command, self.data = self.peg_visitor.visit(ast)
            # self.command, self.data = self.peg_visitor(ast).visit()
            self.draw()

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