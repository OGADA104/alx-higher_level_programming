#!/usr/bin/python3
"""Load from json module"""


import json


def load_from_json_file(filename):
    """load json obj from file
    args: file name
    """
    with open(filename, 'r') as myfile:
        loaded = json.load(myfile)
        return loaded
