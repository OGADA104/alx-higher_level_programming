#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    if not isinstance(obj, MyClass):
        raise ValueError("Input is not an instance of MyClass")
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result

class MyClass:
    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
