#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Class that defines a rectangle

    Attributes:
        width(int): rectangle width (private)
        height(int): rectangle height (private)

    Methods:
        width(self): width property getter
        width(self, value): width property setter
        area:(self): calculates rectangle area
        perimeter(self): calculates rectangle perimeter
    """
    def __init__(self, width=0, height=0):
        """Intializes a new rectangle instance

        Args:
            width: rectangle width; default value of 0
            height: rectangle height; default value of 0

        Raises:
            TypeError: if width and/or height are not integers
            ValueError: if width and/or height are less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
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

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimeter of a rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle with the # character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        res = "#" * self.__width
        return (res + "\n") * (self.__height - 1) + res

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
