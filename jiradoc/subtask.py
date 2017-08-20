# ------------------------------------------------------------
# subtask.py
#
# A class representing a JIRA sub-task
# ------------------------------------------------------------


class SubTask:
    def __init__(self, name, time, sprint="", parent_id="", type="", desc=""):
        self.parent_id = parent_id
        self.sprint = sprint
        self.name = name
        self.time = time
        self.type = type
        self.desc = desc

    def __str__(self):
        return "SubTask(parent_id=" + self.parent_id + ",sprint=" + self.sprint + ",type=" + self.type + ",name=" + self.name + ",time=" + self.time + ",desc=" + self.desc + ")"
