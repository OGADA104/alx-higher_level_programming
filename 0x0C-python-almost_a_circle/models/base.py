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
        if json_string is not None:
            json_dict = json.loads(json_string)
        else:
            json_dict = []
        return json_dict

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from dictionary."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class: {}".format(cls.__name__))

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from file"""
        file = "{}.json".format(cls.__name__)
        try:
            with open(file, 'r') as loader:
                data = cls.from_json_string(loader.read())
                instances = [cls.create(**item) for item in data]
            return instances
        except FileNotFoundError:
            return []
