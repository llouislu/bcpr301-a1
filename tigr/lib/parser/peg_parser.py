from parsimonious import Grammar
from parsimonious.nodes import NodeVisitor
from tigr.lib.parser.base_parser import BaseParser


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


class PegParser(BaseParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0

        self.peg_grammar = Grammar(r'''
            line        = statement ws? comment? ws
            statement   = directive ws? parameter?
            directive   = ~"P|X|Y|D|W|N|E|S|U"
            parameter   = ~"\d{0,}\.{0,1}\d{0,}"
            comment     = ~"#.*"
            ws          = ~"\s*"
        ''')
        self.peg_visitor = TigrVisitor()

    def parse(self, raw_source):
        for line in raw_source:
            line = line.strip()
            ast = self.peg_grammar.parse(line)
            self.command, self.data = self.peg_visitor(ast)
            self.draw()
