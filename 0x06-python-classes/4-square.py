#!/usr/bin/python3
"""Class that defines a square by:
    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
    size must be an integer, otherwise TypeError
    if size is less than 0, raise a ValueError
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method that returns the current square area
    Without importing any module
"""


class Square:
    """Blueprint for square objects

    Attributes:
        __size(int): square size

    Methods:
        __init__: initializes a new square instance
        area: returns the area of the square

    Properties:
        size: getter and setter for size attribute
    """
    def __init__(self, size):
        """Initialize a square with a specific size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value(int): specified square size

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
