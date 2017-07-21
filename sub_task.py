# ------------------------------------------------------------
# sub_task.py
#
# A class representing a JIRA sub-task
# ------------------------------------------------------------

class SubTask:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return self.type
