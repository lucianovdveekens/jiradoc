# ------------------------------------------------------------
# story.py
#
# A class representing a JIRA story
# ------------------------------------------------------------


class Story:
    def __init__(self, id, name, sub_tasks, sprint=""):
        self.id = id
        self.name = name
        self.sub_tasks = sub_tasks
        self.sprint = sprint

    def __repr__(self):
        return 'Story    : ' + self.id + ' ' + self.name + '\n'\
               'Sprint   : ' + self.sprint + '\n' \
               'Sub-tasks: ' + str(self.sub_tasks)
