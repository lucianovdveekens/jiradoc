# ------------------------------------------------------------
# subtask.py
#
# A class representing a JIRA sub-task
# ------------------------------------------------------------


class SubTask:
    def __init__(self, name, time, type="", desc=""):
        self.name = name
        self.time = time
        self.type = type
        self.desc = desc

    def __repr__(self):
        return 'SubTask(type=' + self.type + ',name=' + self.name + ',time=' + self.time + ',desc=' + self.desc + ')'
