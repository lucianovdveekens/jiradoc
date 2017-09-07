# ------------------------------------------------------------
# __main__.py
#
# The main program, TODO
# ------------------------------------------------------------
import argparse
import sys

import pkg_resources
import yaml
from jira.exceptions import JIRAError

from client.jiraclient import JIRAClient, ValidationError
from parser.jiraparse import jiraparser


def main():
    parsed_args = _cli_parse()
    subtasks = _parse_file(parsed_args.file)
    jira_client = _create_jira_client()

    try:
        jira_client.insert_subtasks(subtasks)
    except (JIRAError, ValidationError) as e:
        sys.exit("Failed to insert tasks: " + str(e))


def _cli_parse():
    parser = argparse.ArgumentParser(
        description='A tool that parses a JIRAdoc file, extracts sub-tasks and inserts them into JIRA.')
    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    parser.add_argument('-f', dest='file', default=test_file, help='A file containing the sub-tasks')
    cli_args = parser.parse_args()
    return cli_args


def _create_jira_client():
    config = _load_config()
    return JIRAClient(config['jira']['url'], config['jira']['user'], config['jira']['passwd'])


def _parse_file(file):
    with open(file) as f:
        content = f.read()

    # TODO: handle parser errors
    subtasks = jiraparser.parse(content)
    return subtasks


def _load_config():
    try:
        with open('data/config.yml') as f:
            return yaml.load(f)
    except IOError as e:
        sys.exit("Failed to load config: " + str(e))


if __name__ == "__main__":
    main()
