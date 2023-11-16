#!/usr/bin/python3
""" my base module"""


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
