# ------------------------------------------------------------
# story.py
#
# A class representing a JIRA story
# ------------------------------------------------------------


class Story:
    def __init__(self, issue, name, sub_tasks, sprint=""):
        self.issue = issue
        self.name = name
        self.sub_tasks = sub_tasks
        self.sprint = sprint

    def __repr__(self):
        return 'Story    : ' + self.issue + ' ' + self.name + '\n'\
               'Sprint   : ' + self.sprint + '\n' \
               'Sub-tasks: ' + str(self.sub_tasks)
