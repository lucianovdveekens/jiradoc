JIRAdoc
=======

This is a small library to parse JIRAdoc markup files. Sub-tasks are extracted from the file and inserted into JIRA via the REST API.

Sample format::

  = LP-1 The 1st story
  CODE
  * A sub-task @ 4h
  ** Task description!
  * Another sub-task @ 1h
  ** Do "something"
  FD
  * A functional design sub-task @ 1h

  = LP-2 The 2nd story
  TEST
  * A test task @ 4h

TODO
