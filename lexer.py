# ------------------------------------------------------------
# lexer.py
#
# A tokenizer for the jiradoc language.
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = ['EQUALS', 'ISSUE', 'TYPE', 'ASTERISK', 'AT_SIGN', 'DOUBLE_ASTERISK', 'WORD']

# Regular expression rules for simple tokens
t_EQUALS = r'='

t_ISSUE = r'\w+-\d+'

t_TYPE = r'CODE|FD|TEST|MANUAL'

t_ASTERISK = r'\*'

t_AT_SIGN = r'@'

t_DOUBLE_ASTERISK = r'\*\*'

t_WORD = r'[\w-]+'

# A string containing ignored characters (spaces, tabs and newlines)
t_ignore = ' \t\n'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()