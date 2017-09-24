def test_lex_parent_issue():
    tokens = _lex("= LP-1 A story")
    assert len(tokens) is 4
    assert tokens[0].type == 'STORY_START'
    assert tokens[1].type == 'ISSUE'
    assert tokens[2].type == 'WORD'
    assert tokens[3].type == 'WORD'


def test_lex_task():
    tokens = _lex("- A test task @ 4h")
    assert len(tokens) is 6
    assert tokens[0].type == 'TASK_START'
    assert tokens[1].type == 'WORD'
    assert tokens[2].type == 'WORD'
    assert tokens[3].type == 'WORD'
    assert tokens[4].type == 'TIME_START'
    assert tokens[5].type == 'WORD'


def test_lex_description():
    tokens = _lex("-- Some description")
    assert len(tokens) is 3
    assert tokens[0].type == 'DESC_START'
    assert tokens[1].type == 'WORD'
    assert tokens[2].type == 'WORD'


def test_lex_task_with_description():
    tokens = _lex("""
    - A test task @ 4h
    -- Some description
    """)
    assert len(tokens) is 9
    assert tokens[0].type == 'TASK_START'
    assert tokens[1].type == 'WORD'
    assert tokens[2].type == 'WORD'
    assert tokens[3].type == 'WORD'
    assert tokens[4].type == 'TIME_START'
    assert tokens[5].type == 'WORD'
    assert tokens[6].type == 'DESC_START'
    assert tokens[7].type == 'WORD'
    assert tokens[8].type == 'WORD'


def test_lex_story():
    tokens = _lex("""
    = LP-1 A story
    CODE:
    - A subtask @ 1h
    -- Task description!
    """)
    assert len(tokens) is 13
    assert tokens[0].type == 'STORY_START'
    assert tokens[1].type == 'ISSUE'
    assert tokens[2].type == 'WORD'
    assert tokens[3].type == 'WORD'
    assert tokens[4].type == 'TYPE'
    assert tokens[5].type == 'TASK_START'
    assert tokens[6].type == 'WORD'
    assert tokens[7].type == 'WORD'
    assert tokens[8].type == 'TIME_START'
    assert tokens[9].type == 'WORD'
    assert tokens[10].type == 'DESC_START'
    assert tokens[11].type == 'WORD'
    assert tokens[12].type == 'WORD'


def _lex(input):
    from jiradoc.lexer import lexer
    lexer.input(input)

    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    return tokens
