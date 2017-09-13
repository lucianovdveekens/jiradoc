from jira import JIRA
from jira import JIRAError
from requests import ConnectionError

import config


class JIRAClient(object):
    """A client to communicate with the JIRA REST API."""

    def __init__(self, server, username, password):
        try:
            self.jira = JIRA(server, basic_auth=(username, password), max_retries=0, logging=False)
        except ConnectionError:
            raise ClientError("Failed connecting to JIRA. Is it up and running?")

    def insert_subtasks(self, subtasks):
        for subtask in subtasks:
            self._insert_subtask(subtask)

    def _insert_subtask(self, subtask):
        self._validate(subtask)

        fields = _to_fields(subtask)
        _append_custom_fields(fields, subtask.type)

        try:
            issue = self.jira.create_issue(fields=fields)
        except JIRAError as e:
            raise ClientError('Failed to insert subtask: %s,\nResponse from client: %s' % (fields, e.response.text))

        print("Created sub-task '%s %s'" % (issue.key, issue.fields.summary))

    def _validate(self, subtask):
        story = self.jira.issue(subtask.parent_id)
        existing_subtasks = story.fields.subtasks
        for existing_task in existing_subtasks:
            if subtask.summary == existing_task.fields.summary:
                raise ValidationError("%s already has a sub-task named '%s'" % (subtask.parent_id, subtask.summary))


def _to_fields(subtask):
    fields = {
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
    return fields


def _append_custom_fields(fields, type):
    custom_fields = config.load('custom_fields')
    for custom_field, value in custom_fields.items():
        if isinstance(value, dict) and type in value:
            # this custom field has type-specific values
            value = value[type]

        fields[custom_field] = value


class ClientError(Exception):
    """Raised when a JIRA client exception occurred"""


class ValidationError(ClientError):
    """Raised when a sub-task is invalid"""
