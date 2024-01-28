#!/usr/bin/python3
"""Class that defines a square by:
    Private instance attribute: size
    Instantiation with optional size:
        size must be an int, else TypeError
        size must be >= 0 else ValueError
    Has a public instance method that returns the current sqaure area
    Without importing any module
"""


class Square:
    """Blueprint for square objects

    Attributes:
        __size(int): square size

    Methods:
        __init__: initializes a new square instance
        area: returns the area of the square
    """
    def __init__(self, size=0):
        """Initialize a square with a specific size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size**2
