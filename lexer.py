# ------------------------------------------------------------
# lexer.py
#
# A tokenizer for the jiradoc language.
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = ['STORY_START', 'SUBTASK_START', 'DESCRIPTION_START', 'TIME_START', 'ISSUE', 'WORD', 'TYPE']

# Regular expression rules for simple tokens
t_STORY_START = r'='

t_SUBTASK_START = r'\*'

t_DESCRIPTION_START = r'\*\*'

t_TIME_START = r'(?<= )-(?= )'

t_ISSUE = r'\w+-\d+'

t_WORD = r'[\w-]+'

t_TYPE = r'(?<=\n)(CODE|FD|TEST|MANUAL)(?=\n)'

# A string containing ignored characters (spaces, tabs and newlines)
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
testdata = '''
= ABC-1234 My story
CODE
* A sub-task - 4h 
** Task description
* Another sub-task -1h
** Test 1 2 3
FD
* A functional design sub-task - 1h
'''
# Give the lexer some input
lexer.input(testdata)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
