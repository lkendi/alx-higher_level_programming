#!/usr/bin/python3
"""Class that defines a square by:
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    Without importing any modules
"""


class Square:
    """Class that defines a square

    Attributes:
        __size(int): size of the square; private variable

    Methods:
        __init__: initializes a new square object
    """
    def __init__(self, size):
        """Initializes a square with a specified size

        Args:
            size(int): size of the square
        """
        self.__size = size
