#!/usr/bin/python3
"""Square module"""


class Square:
    """
    Represents a square with a size and position.

    Attributes:
        __size (int): The size of the square (private attribute).
        __position (tuple): The (x, y) coordinates of the square's
            top-left corner (private attribute).

    Methods:
        __init__: Initializes a new instance of the Square class.
        size: Getter and setter for the size attribute.
        position: Getter and setter for the position attribute.
        area: Calculates and returns the area of the square.
        my_print: Prints a visual representation of the square
                    using '#' characters.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a specific size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The (x, y) coordinates of the square's
                top-left corner.

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The (x, y) coordinates of the square's top-left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square,
                as a tuple of two integers.

        Raises:
            TypeError: If value is not a tuple of two integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(v, int) for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a visual representation of the square using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1],
                           self.__position[1] + self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)
