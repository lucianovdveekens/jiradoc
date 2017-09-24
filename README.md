# JIRAdoc

Simplify the insertion of sub-tasks into JIRA by defining them in a specially formatted text file. This saves you the trouble of going through the same UI steps to create a sub-task over and over again.

## Prerequisites

You should have an installed version of Python on your system.

## Installation

Use Python's package manager to install the application, it comes bundled with Python on both Windows and Linux.

```
$ pip install git+https://github.com/lucianovdveekens/jiradoc
```

## Usage

Below is an example text file containing sub-tasks that we're willing to insert into JIRA.

```
= ABC-1 My story
CODE:
- This is a coding task to implement a feature @ 8h
-- With an optional description
TEST:
- Write test specification @ 4h
- Test the new feature @ 4h
FD:
- Update the functional design @ 1h
MANUAL:
- Add a section describing the new functionality @ 2h
```

Save it to a text file and provide it as an argument to the program.


```
$ python -m jiradoc tasks.txt
```

## Configuration

## Running the tests

Explain how to run the automated tests for this system

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
