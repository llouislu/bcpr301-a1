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
        # self.alias_commands = {
        #     'quit': self.do_exit,
        #     'bye': self.do_exit,
        #     'q': self.do_exit,
        #     'halt': self.do_exit
        # }

    def onecmd(self, line):
        line = line.strip()
        if line in self.alias_commands:
            self.alias_commands[line]()
        else:
            try:
                line_uppercased = line.upper()
                self.parser.parse([line_uppercased])
            except:
                print('you have a syntax error in "{}"'.format(line))

    def go(self):
        self.cmdloop()
