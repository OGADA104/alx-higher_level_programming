#!/usr/bin/python3
""" my write file module"""


def write_file(filename="", text=""):
    """
    write text to myfile
    """
    with open(filename, 'w', encoding="UTF8") as myfile:
        chars = myfile.write(text)
        return chars
