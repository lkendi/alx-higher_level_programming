#!/usr/bin/python3
"""Inheritance Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeomtry

    Attributes:
        __width(int): rectangle width
        __height(int): rectangle height

    Methods:
        __init__: initializes a new rectangle object
        area: calculates the rectangle area
        integer_validator: validates a value passed to it
        __str__: returns rectangle description
    """
    def __init__(self, width, height):
        """Initializes a new rectangle instance

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates rectangle area"""
        return (self.__height * self.__width)

    def __str__(self):
        """Returns a description of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
