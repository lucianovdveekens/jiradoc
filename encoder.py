# ------------------------------------------------------------
# encoder.py
#
# A small utility class to serialize objects to JSON
# ------------------------------------------------------------
from json import JSONEncoder


class MyJSONEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
