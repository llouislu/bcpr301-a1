import cmd
import platform
from tigr.lib.interface import AbstractSourceReader


class PromptSourceReader(cmd.Cmd, AbstractSourceReader):
    intro = 'Welcome to tigr on {}'.format(platform.system())

    def __init__(self, parser, optional_file_name=None):
        self.parser = parser
        self.file_name = optional_file_name
        self.source = []
        super().__init__()
        self.alias_commands = set(['quit', 'bye', 'q', 'halt'])

    def onecmd(self, line):
        line = line.strip()
        if line in self.alias_commands:
            print('bye bye!')
            return True
        else:
            self.parser.parse([line])

    def go(self):
        self.cmdloop()
