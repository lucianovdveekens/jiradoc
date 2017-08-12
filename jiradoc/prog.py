# ------------------------------------------------------------
# prog.py
#
# The main program which expects a jiradoc formatted file to
# be passed in as a cmdline option. It reads the file, parses
# its content to a Story object and then serializes it to JSON
# ------------------------------------------------------------
import argparse

from jiradoc.parser.parser import parser

argparser = argparse.ArgumentParser(description='The JIRAdoc parser')
argparser.add_argument('-f', dest='file', default='jiradoc/test.jiradoc', help='The jiradoc formatted file')
args = argparser.parse_args()

with open(args.file) as f:
    content = f.read()

stories = parser.parse(content)
for story in stories:
    print story

# json = json.dumps(story.__dict__, cls=MyJSONEncoder, indent=4, sort_keys=True)
# print json