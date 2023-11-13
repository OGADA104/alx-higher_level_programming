#!/usr/bin/python3
"""my square module"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """a square is a special rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(width = size)
        super().__init__(x)
        super().__init__(y)

