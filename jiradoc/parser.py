from __future__ import print_function

import sys

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
    '''story : STORY_START ISSUE words subtasks'''
    for task in p[4]:
        task.parent_id = p[2]

    p[0] = p[4]


def p_words(p):
    '''words : WORD words
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
        task.type = p[1].replace(':', '')

    p[0] = p[2]


def p_subtasks_without_type(p):
    '''subtasks-without-type : subtask subtasks-without-type
                             | subtask'''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [p[1]] + p[2]


def p_subtask(p):
    '''subtask : TASK_START words time'''
    p[0] = SubTask(summary=p[2], estimate=p[3])


def p_subtask_description(p):
    '''subtask : TASK_START words time description'''
    p[0] = SubTask(summary=p[2], estimate=p[3], description=p[4])


def p_subtask_missing_time(p):
    '''subtask : TASK_START words error description
               | TASK_START words error'''
    raise ParseError("'%s' is missing a time estimate." % p[2])


def p_time(p):
    '''time : TIME_START WORD'''
    p[0] = p[2]


def p_description(p):
    '''description : DESC_START words'''
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    global error_count
    error_count += 1
    print("Syntax error in input: " + str(p), file=sys.stderr)


error_count = 0


def parse(content):
    parser = yacc.yacc()
    parsed_content = parser.parse(content)
    if error_count > 0:
        raise ParseError(str(error_count) + " parse error(s) found")

    return parsed_content


class ParseError(Exception):
    """Raised when the content could not be parsed"""

# # Testing
# content = open('../data/test.jiradoc').read()
# subtasks = parser.parse(content)
#
# for subtask in subtasks:
#     print subtask
