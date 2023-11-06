#!/usr/bin/python3
class MyList(list):
    """ my class that inherits from list"""

    def print_sorted(self):
        """
        prints asorted list without modifiyng the original
        Args: (int) list
        Return: a sorted list
        """
        new_list = sorted(self)
        print(new_list)
