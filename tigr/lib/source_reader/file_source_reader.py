from tigr.lib.interface import AbstractSourceReader

class FileSourceReader(AbstractSourceReader):
    def go(self):
        for line_number, line in enumerate(self.file_name, 1):
            line = line.strip()
            line = line.upper()
            self.source.append(line)
        try:
            self.parser.parse(self.source)
        except:
            print('you have a syntax error on Line {}: "{}"'.format(line_number, line))
