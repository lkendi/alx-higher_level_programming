#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__: Initializes a new instance of the Square class.
        size: Getter and setter for the size attribute.
        area: Returns the area of the square.
        my_print: Prints the square with the character '#' to stdout.

    """
    def __init__(self, size=0):
        """Initializes a square with a specific size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is less than 0.

        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters.

        If size is equal to 0, print an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
