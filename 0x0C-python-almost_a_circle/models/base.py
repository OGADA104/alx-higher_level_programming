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

    @staticmethod
    def to_json_string(list_dictionaries):
        """save to json string"""
        if list_dictionaries is not None:
            data_json = json.dumps(list_dictionaries)
        else:
            data_json = json.dumps([])
        return data_json

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    def from_json_string(json_string):
        """from string to dict"""
        json_dict = json.loads(json_string)
        return json_dict
