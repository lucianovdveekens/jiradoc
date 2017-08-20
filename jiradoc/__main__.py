# ------------------------------------------------------------
# __main__.py
#
# The main program
# ------------------------------------------------------------
import argparse
import os
import pkg_resources
import sys

from client.jiraclient import JIRAClient
from jiradoc.parser.parser import parser as jiradoc_parser


def main(args=None):
    parser = argparse.ArgumentParser(description='A tool that parses a JIRAdoc formatted file and returns a list of '
                                                 'story objects')

    test_file = pkg_resources.resource_filename(__name__, 'data/test.jiradoc')
    parser.add_argument('-f', dest='file', default=test_file,
                        help='A .jiradoc file containing sub-tasks to JIRA stories')
    args = parser.parse_args()

    filename, ext = os.path.splitext(args.file)
    if ext != '.jiradoc':
        print 'Invalid file extension: ' + ext
        print 'The only valid extension is .jiradoc'
        sys.exit(1)

    with open(args.file) as f:
        content = f.read()

    client = JIRAClient('http://localhost:8080', 'admin', 'admin')
    subtasks = jiradoc_parser.parse(content)

    for subtask in subtasks:
        sprint = client.get_sprint(subtask.parent_id)
        subtask.sprint = sprint
        print subtask


if __name__ == "__main__":
    main()
