from tigr.lib.parser.base_parser import BaseParser
import re


class RegexParser(BaseParser):
    line_pattern = re.compile(
        r'^(P|X|Y|D|W|N|E|S|U)\s+(\d{0,}\.{0,1}\d{0,})\s{0,}(?=#{0,1})')

    def __init__(self, drawer):
        super().__init__(drawer)

    def parse(self, raw_source):
        for line in raw_source:
            line = line.strip()
            matched = self.line_pattern.match(line)
            if not matched:
                raise ValueError()
            self.command, self.data = matched.groups()
            self.draw()