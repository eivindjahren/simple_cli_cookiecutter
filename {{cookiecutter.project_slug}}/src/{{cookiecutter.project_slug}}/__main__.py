import argparse
import sys

from {{cookiecutter.project_slug}} import __version__


def make_parser(prog):
    parser = argparse.ArgumentParser(
        prog=prog, description="{{cookiecutter.project_short_description}}"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    return parser


def parse_args(argv):
    parser = make_parser(argv[0])
    return parser.parse_args(argv[1:])


def run_{{cookiecutter.project_slug}}(args):
    # TODO
    pass


def parse_args_and_run(argv):
    run_{{cookiecutter.project_slug}}(parse_args(argv))

def main():
    parse_args_and_run(sys.argv)


if __name__ == "__main__":
    main()
