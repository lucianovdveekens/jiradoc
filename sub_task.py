# ------------------------------------------------------------
# sub_task.py
#
# A class representing a JIRA sub-task
# ------------------------------------------------------------

class SubTask:
    def __init__(self, name, type="", desc=""):
        self.type = type
        self.name = name
        self.desc = desc

    def __repr__(self):
        return 'SubTask(type=' + self.type + ',name=' + self.name + ',desc=' + self.desc + ')'
