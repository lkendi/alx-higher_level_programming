#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Class that defines a rectangle

    Attributes:
        width(int): rectangle width (private)
        height(int): rectangle height (private)

    Methods:
        width: width property getter
        width: width property setter
    """
    def __init__(self, width=0, height=0):
        """Intializes a new rectangle instance

        Args:
            width: rectangle width; default value of 0
            height: rectangle height; default value of 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of a rectangle"""
        return self.__width

    @property
    def height(self):
        """Retrieves the height of a rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the value of the width of a rectangle

        Args:
            value: value to set the width to

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value of the height of a rectangle

        Args:
            value: value to set the height to

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
