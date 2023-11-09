#!/usr/bin/python3
"""my student module"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            student_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
        return student_dict
