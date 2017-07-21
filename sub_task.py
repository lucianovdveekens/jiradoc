# ------------------------------------------------------------
# sub_task.py
#
# A class representing a JIRA sub-task
# ------------------------------------------------------------

class SubTask:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __repr__(self):
        return self.type + ': ' + self.name
