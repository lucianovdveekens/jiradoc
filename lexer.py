# ------------------------------------------------------------
# lexer.py
#
# A tokenizer for the jiradoc language.
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = ['EQUALS', 'ISSUE', 'TYPE', 'AT_SIGN', 'DOUBLE_ASTERISK', 'WORD']

# Regular expression rules for simple tokens
t_EQUALS = r'='

t_ISSUE = r'\w+-\d+'

t_AT_SIGN = r'@'

t_DOUBLE_ASTERISK = r'\*\*'

t_WORD = r'[\w-]+'

# A string containing ignored characters (spaces, tabs and newlines)
t_ignore = ' \t\n'

current_task_type = ""


def t_current_task_type(t):
    r'CODE|FD|TEST|MANUAL'
    global current_task_type
    current_task_type = t.value
    pass


def t_TYPE(t):
    r'\*'
    t.value = current_task_type
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
= ABC-1234 My story
CODE
* A sub-task
* Another sub-task
FD
* klfjskldafj
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
