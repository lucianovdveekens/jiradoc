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
        print "Failed to load config:", e
        sys.exit(1)

    jira_client = JIRAClient(config['jira']['url'], config['jira']['user'], config['jira']['passwd'])

    with open(args.file) as f:
        content = f.read()

    # TODO: handle parser errors
    subtasks = jiraparser.parse(content)

    for subtask in subtasks:
        try:
            jira_client.insert(subtask)
        except (JIRAError, ValidationError) as e:
            sys.exit("Failed to insert task: " + str(e))


if __name__ == "__main__":
    main()
