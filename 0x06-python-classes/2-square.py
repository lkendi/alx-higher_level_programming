#!/usr/bin/python3
"""Class that defines a square by:
    Private instance attribute: size
    Instantiation with optional size:
        size must be an int, else TypeError
        size must be >= 0 else ValueError
    Without importing any module
"""
class Square:
    """Blueprint for a square object
    
    Attributes:
        size(int): square size
        
    Methods:
        __init__ : initializes a square object
    """
    def __init__(self, size=0):
        """Initializes an instance of a sqaure
        
        Args:
            size - size of the square
        
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
