from parser import parse
from subtask import SubTask


def test_parse_subtask():
    subtasks = parse("""
    = LP-1 A story
    CODE:
    - A subtask @ 1h
    """)

    assert len(subtasks) is 1
    assert subtasks[0] == SubTask(parent_id="LP-1", type="CODE", summary="A subtask", estimate="1h")


def test_parse_subtask_with_description():
    subtasks = parse("""
    = LP-1 A story
    CODE:
    - A subtask @ 1h
    -- A description!
    """)

    assert len(subtasks) is 1
    assert subtasks[0] == SubTask(parent_id="LP-1", type="CODE", summary="A subtask", estimate="1h",
                                  description="A description!")


def test_parse_subtasks():
    subtasks = parse("""
    = LP-1 A story
    CODE:
    - Coding subtask @ 1h
    - Another coding subtask @ 2h
    """)

    assert len(subtasks) is 2
    assert subtasks[0] == SubTask(parent_id="LP-1", type="CODE", summary="Coding subtask", estimate="1h")
    assert subtasks[1] == SubTask(parent_id="LP-1", type="CODE", summary="Another coding subtask", estimate="2h")


def test_parse_subtasks_with_different_types():
    subtasks = parse("""
       = LP-1 A story
       CODE:
       - Coding subtask @ 4h
       TEST:
       - Testing subtask @ 8h
       """)

    assert len(subtasks) is 2
    assert subtasks[0] == SubTask(parent_id="LP-1", type="CODE", summary="Coding subtask", estimate="4h")
    assert subtasks[1] == SubTask(parent_id="LP-1", type="TEST", summary="Testing subtask", estimate="8h")


def test_parse_multiple_stories():
    subtasks = parse("""
          = LP-1 A story
          CODE:
          - Coding subtask @ 3h
          = LP-2 Another story
          TEST:
          - Testing subtask @ 5h
          """)

    assert len(subtasks) is 2
    assert subtasks[0] == SubTask(parent_id="LP-1", type="CODE", summary="Coding subtask", estimate="3h")
    assert subtasks[1] == SubTask(parent_id="LP-2", type="TEST", summary="Testing subtask", estimate="5h")
