#!/usr/bin/python3
""" add itegers"""


def add_integer(a, b=98):
    """ 
    add integer

    Args:
        a :first int
        b: second int, default 98
    
    Return: int(sum)
        return sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
            raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
            raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return result
