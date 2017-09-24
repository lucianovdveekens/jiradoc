import argparse
import sys

import config
import parser
from client import JIRAClient, ClientError
from parser import ParseError


def main():
    """The program's main entry point"""
    try:
        parsed_args = _cli_parse()
        subtasks = _parse_file(parsed_args.file)

        client = _init_client()
        client.insert_subtasks(subtasks)
    except (ParseError, ClientError) as e:
        sys.exit(e)


def _cli_parse():
    parser = DefaultHelpParser(prog='jiradoc',
                               description='Extract sub-tasks from a file and insert them into JIRA using the REST ' \
                                           'API.')
    parser.add_argument(dest='file', help='A file containing JIRAdoc markup language')
    cli_args = parser.parse_args()
    return cli_args


def _init_client():
    """Connect to JIRA and return the client"""
    jira = config.load('jira')
    return JIRAClient(jira['url'], jira['user'], jira['passwd'])


def _parse_file(file):
    """Parse the JIRAdoc file and return a list of sub-tasks"""
    with open(file) as f:
        content = f.read()

    subtasks = parser.parse(content)
    return subtasks


class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()
