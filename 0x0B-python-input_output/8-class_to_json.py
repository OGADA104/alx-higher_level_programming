#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
MyClass = __import__('8-my_class_2').MyClass
"""class to json module"""



def class_to_json(obj):
    if not isinstance(obj, MyClass):
        raise ValueError("Input is not an instance of MyClass")
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value
    return result
