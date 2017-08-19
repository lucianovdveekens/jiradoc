# JIRAdoc

This repository serves as a small library to parse a _.jiradoc_ file and extract JIRA sub-tasks from it which later can be inserted into JIRA using the REST API.

_An example format:_
```
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
```
TODO 