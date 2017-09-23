from __future__ import print_function

import os
import sys

import appdirs
import pkg_resources
import yaml

# The config is lazy-loaded
config = None


def load(key, required=True):
    """Return the value associated with the key"""
    config_dir = appdirs.user_config_dir('jiradoc')
    config_file = os.path.join(config_dir, 'config.yml')

    if not os.path.isfile(config_file):
        _create_user_config(config_file)

    global config
    if config is None:
        _load_config(config_file)

    if key in config:
        return config[key]
    elif required:
        sys.exit("Configuration is missing required key: " + key)


def _create_user_config(config_file):
    """Create the user's configuration file"""
    config_dir = os.path.dirname(config_file)
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    src = pkg_resources.resource_stream(__name__, 'data/sample_config.yml')
    with open(config_file, 'w') as dst:
        dst.writelines(src)


def _load_config(config_file):
    """Load the user's configuration file."""
    print('Loading configuration: ' + config_file)
    try:
        global config
        with open(config_file) as f:
            config = yaml.load(f)
    except IOError as e:
        sys.exit('Failed to load config: ' + str(e))
