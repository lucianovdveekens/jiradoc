class ClientError(Exception):
    """Raised when a JIRA client exception occurred"""


class ValidationError(ClientError):
    """Raised when a sub-task is invalid"""
