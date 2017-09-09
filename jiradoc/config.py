import sys

import yaml


def load(key):
    try:
        with open('data/config.yml') as f:
            return yaml.load(f)[key]
    except IOError as e:
        sys.exit("Failed to load config: " + str(e))
    except KeyError as e:
        sys.exit("Config does not contain key: " + e.message)
