class SubTask(object):
    """This class represents a JIRA sub-task"""

    def __init__(self, summary, estimate, parent_id="", type="", description=""):
        self.parent_id = parent_id
        self.summary = summary
        self.estimate = estimate
        self.type = type
        self.description = description

    def __str__(self):
        return "SubTask(" \
               "parent_id=" + self.parent_id + \
               ",type=" + self.type + \
               ",summary=" + self.summary + \
               ",estimate=" + self.estimate + \
               ",description=" + self.description + \
               ")"
