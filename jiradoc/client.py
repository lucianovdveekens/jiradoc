import sys

import yaml
from jira import JIRA
from jira import JIRAError
from requests import ConnectionError


class JIRAClient(object):
    """A client to communicate with the JIRA REST API."""

    def __init__(self, server, username, password):
        try:
            self.jira = JIRA(server, basic_auth=(username, password), max_retries=0, logging=False)
        except ConnectionError:
            raise ClientError("Failed connecting to JIRA. Is it up and running?")

    def insert_subtasks(self, subtasks):
        try:
            for subtask in subtasks:
                self._insert_subtask(subtask)
        except JIRAError as e:
            raise ClientError(e.message)

    def _insert_subtask(self, subtask):
        self._validate(subtask)

        fields = _to_fields(subtask)
        _append_custom_fields(fields)

        issue = self.jira.create_issue(fields=fields)
        print("Created sub-task '%s' under parent '%s'" % (issue.key + issue.fields.summary, subtask.parent_id))

    def _validate(self, subtask):
        story = self.jira.issue(subtask.parent_id)
        existing_subtasks = story.fields.subtasks
        for existing_task in existing_subtasks:
            if subtask.summary == existing_task.fields.summary:
                raise ValidationError(subtask.parent_id + ' already has a sub-task named \'' + subtask.summary + '\'')


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


def _append_custom_fields(fields):
    config = _load_config()
    custom_fields = config['custom_fields']
    if custom_fields is not None:
        for custom_field, value in custom_fields.items():
            fields[custom_field] = value


def _load_config():
    try:
        with open('data/config.yml') as f:
            return yaml.load(f)
    except IOError as e:
        sys.exit("Failed to load config: " + str(e))


class ClientError(Exception):
    """Raised when a JIRA client exception occurred"""


class ValidationError(ClientError):
    """Raised when a sub-task is invalid"""
