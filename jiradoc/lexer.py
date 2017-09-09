import ply.lex as lex

# List of token names
tokens = ['STORY_START', 'TASK_START', 'DESC_START', 'TIME_START', 'ISSUE', 'WORD', 'TYPE']

# Regular expression rules for simple tokens
t_TYPE = r'(CODE|FD|TEST|MANUAL):'
t_ISSUE = r'[A-Z]+-\d+'
t_WORD = r'[^-=@\s]+'
t_DESC_START = r'--'
t_TASK_START = r'-'
t_STORY_START = r'='
t_TIME_START = r'@'

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
