# JIRAdoc

This repository serves as a small library to parse a _.jiradoc_ file and extract JIRA sub-tasks from it which later can be inserted into JIRA using the REST API.

_An example file:_
```
= ABC-1234 Example story
CODE
* A sub-task # 8h
** its description  
FD
* Another sub-task # 4h

= ABC-5678 Example story 2
...
etc.
```
TODO 