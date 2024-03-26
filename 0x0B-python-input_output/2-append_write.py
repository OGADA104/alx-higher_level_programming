#!/usr/bin/python3
"""append to file module"""


def append_write(filename="", text=""):
    """ append text to filename
    args: filename, text to be added
    """
    with open(filename, 'a', encoding="UTF8") as myfile:
        chars = myfile.write(text)
    return chars
