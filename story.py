# ------------------------------------------------------------
# story.py
#
# A class representing a JIRA story
# ------------------------------------------------------------


class Story:
    def __init__(self, issue, name, sub_tasks):
        self.issue = issue
        self.name = name
        self.sub_tasks = sub_tasks

    def __repr__(self):
        return self.issue + ' ' + self.name + ' ' + str(self.sub_tasks)
