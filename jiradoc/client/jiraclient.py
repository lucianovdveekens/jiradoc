# ------------------------------------------------------------
# jiraclient.py
#
# A client that communicates with the JIRA REST API.
# ------------------------------------------------------------
import re

from jira import JIRA


class JIRAClient:
    def __init__(self, server, username, password):
        self.jira = JIRA(server, basic_auth=(username, password))

    def get_sprint(self, issue_id):
        issue = self.jira.issue(issue_id)
        sprint = issue.fields.customfield_10004[0]
        p = re.compile('(?<=name=).*?(?=,)')
        m = p.search(sprint)
        return m.group()
