from tigr.lib.interface import AbstractSourceReader

class FileSourceReader(AbstractSourceReader):
    def go(self):
        for line_number, line in enumerate(self.file_name, 1):
            line = line.strip()
            line = line.upper()
            self.source.append(line)
            self.parser.parse(self.source)
