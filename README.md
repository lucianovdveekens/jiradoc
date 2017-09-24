# JIRAdoc

Simplify the insertion of sub-tasks into JIRA by defining them in a specially formatted text file and sending them to the JIRA REST API. Hopefully, this saves you the trouble of going through the same UI dialogs over and over again to create a new sub-task.

## Prerequisites

You should have an installed version of Python on your system.

## Installation

Use Python's package manager to install the application, it comes bundled with Python on both Windows and Linux.

```
$ pip install git+https://github.com/lucianovdveekens/jiradoc
```

## Usage

The example below showcases the format of the expected input:

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

Only one story is shown here, but it's okay to define multiple stories in a single file. Once you're ready to insert them, run the following command:

```
$ python -m jiradoc tasks.txt
Logging to: /home/luciano/.cache/jiradoc/log/jiradoc.log
Creating configuration file at: /home/luciano/.config/jiradoc/config.yml
Loading configuration: /home/luciano/.config/jiradoc/config.yml
Created sub-task 'ABC-2 This is a coding task to implement a feature'
Created sub-task 'ABC-3 Write test specification'
Created sub-task 'ABC-4 Test the new feature'
Created sub-task 'ABC-5 Update the functional design'
Created sub-task 'ABC-6 Add a section describing the new functionality'

```

## Configuration

TODO

## Running the tests

TODO

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
