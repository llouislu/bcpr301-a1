from tigr.lib.interface import AbstractSourceReader

class FileSourceReader(AbstractSourceReader):
    def go(self):
        for line in self.file_name:
            line = line.strip()
            line = line.upper()
            self.source.append(line)
        self.parser.parse(self.source)
