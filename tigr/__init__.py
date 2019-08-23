__version__ = '0.1'

def run(args):
    file_name = None
    if args.interactive:
        from .lib.source_reader.prompt_source_reader import PromptSourceReader as Reader
    else:
        from .lib.source_reader.file_source_reader import FileSourceReader as Reader
        file_name = args.infile

    if args.parser == 'peg':
        from .lib.parser.peg_parser import PegParser as Parser
    elif args.parser == 'regex':
        from .lib.parser.regex_parser import RegexParser as Parser

    if args.drawer == 'turtle':
        from .lib.drawer.turtle_drawer import TurtleDrawer as Drawer
    elif args.drawer == 'tkinter':
        from .lib.drawer.tkinter_drawer import TkinterDrawer as Drawer

    reader = Reader(Parser(Drawer()), optional_file_name=file_name)
    reader.go()

def main():
    import argparse
    import sys
    from .lib.config.config_reader import Config

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

    print(args)
    args_config = args.config
    if args_config != '':
        result = Config(args_config).readConfig()
        args.parser = result["--parser"]
        args.drawer = result["--drawer"]
        args.pen = result["--pen"]
    print(args)
    # read config file here as dict
    # convert to argparse.Namespace #argparse.Namespace(**dict)
    # override args from config file
    #
    run(args)
