#!/usr/bin/python3
""" text indentation"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    new_paragraph = True
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            new_paragraph = True
        if new_paragraph and char.isspace():
            result += "\n\n"
            new_paragraph = False

    print(result)
