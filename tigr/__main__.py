def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        prog='tigr', description="Tiny Interpreted Graphics language (TIGr)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--interactive', action='store_true')
    group.add_argument('infile', nargs='?',
                       type=argparse.FileType('r'), default=sys.stdin)
    group.add_argument('outfile', nargs='?',
                       type=argparse.FileType('w'), default=sys.stdout)
    group.add_argument('-c', '--config', action='store')
    group.add_argument('-p', '--parser', action='store')
    group.add_argument('-o', '--output', action='store')
    group.add_argument('-t', '--type', action='store')
    args = parser.parse_args()
    if args.interactive:
        invoke_interactive(args)
    else:
        parse_parameters(args)


def invoke_interactive(args):
    pass


def parse_parameters(args):
    pass


if __name__ == '__main__':
    main()
