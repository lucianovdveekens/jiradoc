# ------------------------------------------------------------
# __main__.py
#
# The main program which expects a jiradoc formatted file to
# be passed in as a cmdline option. It reads the file and
# parses its content to Story objects.
# ------------------------------------------------------------
import argparse
import pkg_resources

from jiradoc.parser.parser import parser


def main(args=None):
    argparser = argparse.ArgumentParser(description='The JIRAdoc parser')

    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    argparser.add_argument('-f', dest='file', default=test_file, help='The jiradoc formatted file')
    args = argparser.parse_args()

    with open(args.file) as f:
        content = f.read()

    stories = parser.parse(content)
    for story in stories:
        print story


if __name__ == "__main__":
    main()
