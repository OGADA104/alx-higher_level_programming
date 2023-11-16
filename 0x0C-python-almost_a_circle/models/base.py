#!/usr/bin/python3
""" my base module"""

import json


class Base:
    """
    my class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """save to json string"""
        if list_dictionaries is not None:
            data_json = json.dumps(list_dictionaries)
        else:
            data_json = "[]"
        return data_json
