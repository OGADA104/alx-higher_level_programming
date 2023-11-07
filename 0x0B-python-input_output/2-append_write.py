#!/usr/bin/python3
"""append to file module"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="UTF8") as myfile:
        chars = myfile.write(text)
    return chars
