# ------------------------------------------------------------
# __main__.py
#
# The main program, TODO
# ------------------------------------------------------------
import argparse

import pkg_resources
import yaml

from client.jiraclient import JIRAClient
from jiradoc.parser.parser import parser as jiradoc_parser


def main(args=None):
    parser = argparse.ArgumentParser(
        description='A tool that parses a JIRAdoc file, extracts sub-tasks and inserts them into JIRA.')

    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    parser.add_argument('-f', dest='file', default=test_file,
                        help='A file containing the sub-tasks')
    args = parser.parse_args()

    with open('data/settings.yml') as f:
        settings = yaml.load(f)

    jira_client = JIRAClient(settings['jira']['url'], settings['jira']['user'], settings['jira']['passwd'])

    with open(args.file) as f:
        content = f.read()

    subtasks = jiradoc_parser.parse(content)

    for subtask in subtasks:
        valid = jira_client.validate(subtask)
        if valid:
            jira_client.insert(subtask)


if __name__ == "__main__":
    main()
