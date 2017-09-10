import argparse
import sys

import pkg_resources

import config
import parser
from client import JIRAClient, ClientError
from parser import ParseError


def main():
    try:
        parsed_args = _cli_parse()
        subtasks = _parse_file(parsed_args.file)

        client = _init_client()
        client.insert_subtasks(subtasks)
    except (ParseError, ClientError) as e:
        sys.exit(e)


def _cli_parse():
    parser = argparse.ArgumentParser(
        description='A tool that parses a JIRAdoc file, extracts sub-tasks and inserts them into JIRA.')
    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    parser.add_argument('-f', dest='file', default=test_file, help='A file containing the sub-tasks')
    cli_args = parser.parse_args()
    return cli_args


def _init_client():
    jira = config.load('jira')
    return JIRAClient(jira['url'], jira['user'], jira['passwd'])


def _parse_file(file):
    with open(file) as f:
        content = f.read()

    subtasks = parser.parse(content)
    return subtasks


if __name__ == "__main__":
    main()
