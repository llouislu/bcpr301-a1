from tigr.lib.interface import AbstractSourceReader

class FileSourceReader(AbstractSourceReader):
    def go(self):
        for line in self.file_name:
            self.source.append(line.strip())
        self.parser.parse(self.source)
