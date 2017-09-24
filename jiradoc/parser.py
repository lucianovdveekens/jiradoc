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
    type = p[1].replace(':', '')
    for task in p[2]:
        task.type = type

    p[0] = p[2]


def p_subtasks_by_type_error_missing_subtasks(p):
    '''subtasks-by-type : TYPE error'''
    raise ParseError("A type should be followed by one or more sub-tasks")


def p_subtasks_by_type_error_missing_type(p):
    '''subtasks-by-type : error subtasks-without-type'''
    raise ParseError("Expected either CODE, TEST, FD or MANUAL followed by a ':'")


def p_subtasks_without_type(p):
    '''subtasks-without-type : subtask subtasks-without-type
                             | subtask'''
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [p[1]] + p[2]


def p_subtask(p):
    '''subtask : TASK_START words time
               | TASK_START words time description'''
    subtask = SubTask(summary=p[2], estimate=p[3])
    if len(p) == 5:
        subtask.description = p[4]

    p[0] = subtask


def p_subtask_error_missing_time(p):
    '''subtask : TASK_START words error'''
    raise ParseError("'%s' is missing a time estimate." % p[2])


def p_time(p):
    '''time : TIME_START WORD'''
    p[0] = p[2]


def p_description(p):
    '''description : DESC_START words'''
    p[0] = p[2]


error_count = 0


# Error rule for syntax errors
def p_error(p):
    global error_count
    error_count += 1
    print("Syntax error in input: " + str(p), file=sys.stderr)


def parse(content):
    global error_count
    error_count = 0

    parser = yacc.yacc()
    parsed_content = parser.parse(content)
    if error_count > 0:
        raise ParseError(str(error_count) + " parse error(s) found")

    return parsed_content


class ParseError(Exception):
    """Raised when the content could not be parsed"""
