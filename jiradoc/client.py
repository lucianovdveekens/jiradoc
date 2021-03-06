from __future__ import print_function

import json
import logging
import re

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
        except JIRAError as e:
            raise ClientError(e.text)

    def insert_subtasks(self, subtasks):
        for subtask in subtasks:
            try:
                self._insert_subtask(subtask)
            except ValidationError as e:
                print(e.message)

    def _insert_subtask(self, subtask):
        if config.load('validate'):
            self._validate(subtask)

        fields = _to_fields(subtask)
        _append_default_fields(fields, subtask.type)

        try:
            logging.debug("Creating issue:\n {}".format(json.dumps(fields, sort_keys=True, indent=4)))
            issue = self.jira.create_issue(fields=fields)
        except JIRAError as e:
            raise ClientError("Failed to insert subtask: {},\nResponse from client: {}".format(fields, e.response.text))

        print("Created sub-task '{} {}'".format(issue.key, issue.fields.summary))

    def _validate(self, subtask):
        story = self.jira.issue(subtask.parent_id)
        existing_subtasks = story.fields.subtasks
        for existing_task in existing_subtasks:
            if subtask.summary == existing_task.fields.summary:
                raise ValidationError("{} already has a sub-task named '{}'".format(subtask.parent_id, subtask.summary))


def _to_fields(subtask):
    fields = {
        'project': {
            'key': re.search("\w+", subtask.parent_id).group(0)
        },
        'parent': {
            'id': subtask.parent_id
        },
        'summary': subtask.summary,
        'description': subtask.description,
        'issuetype': {
            'name': 'Sub-task'
        },
        'timetracking': {
            'originalEstimate': subtask.estimate,
        }
    }
    return fields


def _append_default_fields(fields, type):
    default_fields = config.load('default_fields', required=False)
    if not default_fields:
        return

    for field, value in default_fields.items():
        if isinstance(value, dict) and type in value:
            # this custom field has type-specific values
            value = value[type]

        fields[field] = value


class ClientError(Exception):
    """Raised when a JIRA client exception occurred"""


class ValidationError(Exception):
    """Raised when a sub-task is invalid"""
