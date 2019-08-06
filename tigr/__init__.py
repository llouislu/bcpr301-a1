def invoke_interactive(args):
    pass


def parse_parameters(args):
    from .lib.source_reader.file_source_reader import FileSourceReader
    from .lib.parser.regex_parser import RegexParser
    from .lib.interface import AbstractDrawer
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
    reader = FileSourceReader(RegexParser(Drawer()), optional_file_name=args.infile)
    reader.go()

def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog='tigr', description="Tiny Interpreted Graphics language (TIGr)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--interactive', action='store_true')
    group.add_argument('infile', nargs='?',
                       type=str, default=sys.stdin)
    group.add_argument('outfile', nargs='?',
                       type=str, default=sys.stdout)
    group.add_argument('-c', '--config', action='store')
    group.add_argument('-p', '--parser', action='store')
    group.add_argument('-o', '--output', action='store')
    group.add_argument('-t', '--type', action='store')
    args = parser.parse_args()
    if args.interactive:
        invoke_interactive(args)
    else:
        print(args)
        parse_parameters(args)