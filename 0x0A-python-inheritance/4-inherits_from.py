#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ check if obj is instance of class
    inheritance directly or ondirectly
    """
    return isinstance(obj, a_class) and type(obj) is a_class
