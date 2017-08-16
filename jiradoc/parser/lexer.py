# ------------------------------------------------------------
# lexer.py
#
# A tokenizer for the jiradoc language.
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'STORY_START',
    'SUBTASK_START',
    'DESCRIPTION_START',
    'TIME_START',
    'ISSUE',
    'WORD',
    'TYPE'
]

# Regular expression rules for simple tokens
t_STORY_START = r'='
t_SUBTASK_START = r'\*'
t_DESCRIPTION_START = r'\*\*'
t_TIME_START = r'(?<= )-(?= )'
t_ISSUE = r'[A-Z]+\-\d+'
t_WORD = r'[\w\-\,"]+'
t_TYPE = r'(?<=\n)(CODE|FD|TEST|MANUAL)(?=\r?\n)'

# A string containing ignored characters (spaces, tabs and newlines)
t_ignore = ' \t\r\n'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()