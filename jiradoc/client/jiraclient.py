# ------------------------------------------------------------
# jiraclient.py
#
# A client to communicate with the JIRA REST API.
# ------------------------------------------------------------
import re

from jira import JIRA


class JIRAClient:
    def __init__(self, server, username, password):
        self.jira = JIRA(server, basic_auth=(username, password))

    def insert_subtask(self, subtask):
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

        self.jira.create_issue(fields=data)
