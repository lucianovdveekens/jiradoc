# JIRAdoc

This repository serves as a small library to parse a _.jiradoc_ file and extract JIRA sub-tasks from it which later can be inserted into JIRA using the REST API.

_An example format:_
```
# Sprint 3

= ABC-1234 The 1st story
CODE
* A sub-task @ 4h
** Task description!
* Another sub-task @ 1h
** Do "something"
FD
* A functional design sub-task @ 1h

= ABC-1234 The 2nd story
TEST
* A test task @ 4h
```
TODO 