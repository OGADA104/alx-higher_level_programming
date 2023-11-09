#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    elif hasattr(obj, "__dict__"):
        return {key: class_to_json(value) for key, value in obj.__dict__.items()}
    else:
        return None

