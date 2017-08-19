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
t_DESCRIPTION_START = r'\*{2}'
t_TIME_START = r'@'
t_ISSUE = r'[A-Z]{1,3}\-\d+'
t_WORD = r'[!\w,\-"\.]+'
t_TYPE = r'(?<=\n)(CODE|FD|TEST|MANUAL)(?=\r?\n)'

# A string containing ignored characters (spaces, tabs and newlines)
t_ignore = ' \t\r\n'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# # Testing
# # Give the lexer some input
# lexer.input(open('jiradoc/data/test.jiradoc').read())
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)
