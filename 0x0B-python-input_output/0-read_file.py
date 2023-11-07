#!/usr/bin/python3
""" my readfile module"""


def read_file(filename=""):
    """
    open my file
    args: file name
    """
    with open(filename, 'r', encoding="UTF8") as myfile:
        myfile.readline()
