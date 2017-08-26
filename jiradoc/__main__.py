# ------------------------------------------------------------
# __main__.py
#
# The main program, TODO
# ------------------------------------------------------------
import argparse

import pkg_resources
import sys
import yaml
from jira.exceptions import JIRAError

from client.jiraclient import JIRAClient
from jiradoc.parser.parser import parser as jiradoc_parser


def main(args=None):
    parser = argparse.ArgumentParser(
        description='A tool that parses a JIRAdoc file, extracts sub-tasks and inserts them into JIRA.')

    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    parser.add_argument('-f', dest='file', default=test_file,
                        help='A file containing the sub-tasks')
    args = parser.parse_args()

    try:
        with open('data/config.yml') as f:
            config = yaml.load(f)
    except IOError as e:
        print "Failed to open settings:", e
        sys.exit(1)

    jira_config = config['jira']
    jira_client = JIRAClient(jira_config['url'], jira_config['user'], jira_config['passwd'])

    with open(args.file) as f:
        content = f.read()

    subtasks = jiradoc_parser.parse(content)

    for subtask in subtasks:
        valid = jira_client.validate(subtask)
        if valid:
            try:
                jira_client.insert(subtask)
            except JIRAError as e:
                print "Failed to insert task:", e.text

if __name__ == "__main__":
    main()
