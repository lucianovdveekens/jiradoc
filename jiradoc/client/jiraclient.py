# ------------------------------------------------------------
# jiraclient.py
#
# A client to communicate with the JIRA REST API.
# ------------------------------------------------------------
import re

import sys
from jira import JIRA


class JIRAClient:
    def __init__(self, server, username, password):
        self.jira = JIRA(server, basic_auth=(username, password))

    def insert_subtask(self, subtask):
        valid = self._validate_summary(subtask)
        if not valid:
            return

        data = {
            "project": {
                "key": "LP"
            },
            "parent": {
                "id": subtask.parent_id
            },
            "summary": subtask.summary,
            "description": subtask.description,
            "issuetype": {
                "name": "Sub-task"
            }
        }

        issue = self.jira.create_issue(fields=data)
        print "Created sub-task '" + issue.key + " " + issue.fields.summary + "'"

    def _validate_summary(self, subtask):
        story = self.jira.issue(subtask.parent_id)
        current_subtasks = story.fields.subtasks
        for task in current_subtasks:
            if subtask.summary == task.fields.summary:
                print subtask.parent_id + ' already has a sub-task named \'' + subtask.summary + '\''
                return False

        return True
