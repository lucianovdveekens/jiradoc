# ------------------------------------------------------------
# parser.py
#
# A parser containing BNF grammars to parse jiradoc tokens.
# ------------------------------------------------------------
import ply.yacc as yacc

# DO NOT REMOVE! importing the tokens is required
from lexer import tokens
from lexer import testdata
from story import Story
from sub_task import SubTask


def p_story(p):
    '''story : STORY_START ISSUE name types-and-subtasks'''
    p[0] = Story(p[2], p[3], p[4])


def p_words(p):
    '''words : WORD words
             | WORD'''
    if (len(p) == 3):
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]


def p_name(p):
    '''name : words'''
    p[0] = p[1]


def p_types_and_subtasks(p):
    '''types-and-subtasks : TYPE subtasks types-and-subtasks
                          | TYPE subtasks'''
    for task in p[2]:
        task.type = p[1]

    if len(p) == 4:
        p[0] = p[2] + p[3]
    else:
        p[0] = p[2]


def p_subtasks(p):
    '''subtasks : subtask subtasks
                | subtask'''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [p[1]] + p[2]


def p_subtask(p):
    '''subtask : SUBTASK_START name time description
               | SUBTASK_START name time'''
    task = SubTask(name=p[2], time=p[3])
    if len(p) == 5:
        task.desc = p[4]

    p[0] = task


def p_time(p):
    '''time : TIME_START WORD'''
    p[0] = p[2]


def p_description(p):
    '''description : DESCRIPTION_START words'''
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input: " + str(p))


# Build the parser
parser = yacc.yacc()

# Testing
result = parser.parse(testdata)
print(result)
