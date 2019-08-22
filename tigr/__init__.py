__version__ = '0.1'

def invoke_interactive(args):
    pass


def parse_parameters(args):
    from .lib.source_reader.file_source_reader import FileSourceReader
    from .lib.source_reader.prompt_source_reader import PromptSourceReader
    from .lib.parser.regex_parser import RegexParser
    from .lib.parser.peg_parser import PegParser
    from .lib.interface import AbstractDrawer
    from .lib.drawer.turtle_drawer import TurtleDrawer

    class Drawer(AbstractDrawer):
        def select_pen(self, pen_num):
            pass

        def pen_down(self):
            pass

        def pen_up(self):
            pass

        def go_along(self, along):
            pass

        def go_down(self, down):
            pass

        def draw_line(self, direction, distance):
            pass
    reader = FileSourceReader(PegParser(
        TurtleDrawer()), optional_file_name=args.infile)
    reader.go()


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog='tigr', description="Tiny Interpreted Graphics language (TIGr)")
    group = parser.add_argument_group()
    group.add_argument('-i', '--interactive',
                       action='store_true', default=False)
    group.add_argument('-c', '--config', action='store',
                       help='use configuration from a file', default='')
    group.add_argument('-p', '--parser', action='store',
                       help='specify a parser', default='peg')
    group.add_argument('-d', '--drawer', action='store',
                       help='specify a drawer', default='turtle')
    group.add_argument('-pn', '--pen', action='store',
                       help='specify a pen number', default='1')
    group.add_argument('infile', nargs='?', type=argparse.FileType(
        'r'), default=sys.stdin, help='input script')
    group.add_argument('outfile', nargs='?', type=argparse.FileType(
        'w'), default=sys.stdout, help='output file. draw on window if omitted')

    args = parser.parse_args()

    # read config file here as dict
    # convert to argparse.Namespace #argparse.Namespace(**dict)
    # override args from config file
    #
    if args.interactive:
        invoke_interactive(args)
    else:
        print(args.infile)
        print(args.outfile)
        if not args.infile:
            raise ValueError()
        if not args.outfile:
            raise ValueError()
        print(args)
        parse_parameters(args)
