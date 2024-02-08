#!/usr/bin/python3
"""Inheritance Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """Square class that inherits from Rectangle

    Attributes:
        __size(int): square size

    Methods:
        __init__: initializes a new square object
        area: calculates square area
        integer_validator: validates square size
    """

    def __init__(self, size):
        """Initializes a new square instance

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
