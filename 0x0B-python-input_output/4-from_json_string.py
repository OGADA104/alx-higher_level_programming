#!/usr/bin/python3
"""json to string module"""


import json


def from_json_string(my_str):
    """ json to string"""
    x = json.loads(my_str)
    return x
