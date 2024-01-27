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
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2
