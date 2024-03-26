#!/usr/bin/python3
"""obj to json module"""


import json


def to_json_string(my_obj):
    """
    my_obj to json string
    """
    x = json.dumps(my_obj)
    return x
