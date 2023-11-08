#!/usr/bin/python3
""" json to file module"""


import json


def save_to_json_file(my_obj, filename):
    """json to file
    args: my_object to be saved
        file name to be used
    """
    with open(filename, 'w') as myfile:
        json.dump(my_obj, myfile)
