# ------------------------------------------------------------
# parser.py
#
# A parser containing BNF grammars to parse jiradoc tokens.
# ------------------------------------------------------------
import ply.yacc as yacc

from lexer import tokens
from story import Story
from sub_task import SubTask


def p_story(p):
    'story : EQUALS ISSUE sentence sub-tasks'
    p[0] = Story(p[2], p[3], p[4])


def p_sentence(p):
    '''sentence : sentence WORD
                | WORD'''
    if (len(p) == 3):
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]


def p_sub_tasks(p):
    '''sub-tasks : sub-tasks sub-task
                 | sub-task'''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = p[1] + [p[2]]


def p_sub_task(p):
    'sub-task : TYPE'
    p[0] = SubTask(p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input: " + str(p))


# Build the parser
parser = yacc.yacc()

# Testing
data = '''
= ABC-1234 My story
CODE
FD
MANUAL
TEST
'''

result = parser.parse(data)
print(result)
