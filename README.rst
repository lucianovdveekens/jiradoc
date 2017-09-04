JIRAdoc
=======

This is a small library to parse JIRAdoc markup files. Sub-tasks are extracted from the file and inserted into JIRA via the REST API.

Sample format::

    = LP-1 The 1st story
    CODE:
    - A subtask @ 4h
    -- Task description!
    - Another subtask @ 1h
    -- Do "something", awesome!
    FD:
    - A functional design subtask @ 1h

    = LP-2 The 2nd story
    TEST:
    - A test task @ 4h

TODO
