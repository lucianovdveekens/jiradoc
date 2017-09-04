# ------------------------------------------------------------
# parser.py
#
# A parser containing BNF grammars to create sub-tasks out of
# the jiradoc tokens.
# ------------------------------------------------------------
import ply.yacc as yacc

# noinspection PyUnresolvedReferences
from lexer import tokens
from subtask import SubTask


def p_stories(p):
    '''stories : story stories
               | story'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_story(p):
    '''story : STORY_START ISSUE sentence subtasks'''
    for task in p[4]:
        task.parent_id = p[2]

    p[0] = p[4]


def p_sentence(p):
    '''sentence : WORD sentence
                | WORD'''
    if len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]


def p_subtasks(p):
    '''subtasks : subtasks-by-type subtasks
                | subtasks-by-type'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_subtasks_by_type(p):
    '''subtasks-by-type : TYPE subtasks-without-type'''
    for task in p[2]:
        task.type = p[1]

    p[0] = p[2]


def p_subtasks_without_type(p):
    '''subtasks-without-type : subtask subtasks-without-type
                             | subtask'''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [p[1]] + p[2]


def p_subtask(p):
    '''subtask : TASK_START sentence time description
               | TASK_START sentence time'''
    task = SubTask(summary=p[2], estimate=p[3])
    if len(p) == 5:
        task.description = p[4]

    p[0] = task


def p_time(p):
    '''time : TIME_START WORD'''
    p[0] = p[2]


def p_description(p):
    '''description : DESC_START sentence'''
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input: " + str(p))


# Build the parser
parser = yacc.yacc()
