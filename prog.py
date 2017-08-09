# ------------------------------------------------------------
# prog.py
#
# The main program which expects a jiradoc formatted file to
# be passed in as a cmdline option. It reads the file and
# parses its content to a Story object.
# ------------------------------------------------------------
import argparse

from parser import parser

argparser = argparse.ArgumentParser(description='The JIRAdoc parser')
argparser.add_argument('-f', dest='file', default='test.jiradoc', help='The jiradoc formatted file')
args = argparser.parse_args()

f = open(args.file)
content = f.read()

parsed = parser.parse(content)
print parsed