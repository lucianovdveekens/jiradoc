# ------------------------------------------------------------
# jiraclient.py
#
# A client to communicate with the JIRA REST API.
# ------------------------------------------------------------
import yaml
from jira import JIRA


class JIRAClient:
    def __init__(self, server, username, password):
        self.jira = JIRA(server, basic_auth=(username, password))

    def insert(self, subtask):
        self._validate(subtask)

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
            },
        }

        with open('data/config.yml') as f:
            config = yaml.load(f)

        custom_fields = config['custom_fields']
        if custom_fields is not None:
            for custom_field, value in custom_fields.items():
                data[custom_field] = value

        issue = self.jira.create_issue(fields=data)
        print "Created sub-task '" + issue.key + " " + issue.fields.summary + "'"

    def _validate(self, subtask):
        story = self.jira.issue(subtask.parent_id)
        current_subtasks = story.fields.subtasks
        for task in current_subtasks:
            if subtask.summary == task.fields.summary:
                raise ValidationError(subtask.parent_id + ' already has a sub-task named \'' + subtask.summary + '\'')


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)
