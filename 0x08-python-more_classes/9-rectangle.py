#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Class that defines a rectangle

    Attributes:
        width(int): rectangle width (private)
        height(int): rectangle height (private)
        number_of_instances: number of class instances(public)
        print_symbol: symbol for string representation

    Methods:
        __init__: initializes a new rectangle object
        width(self): width property getter
        width(self, value): width property setter
        area: calculates rectangle area
        perimeter: calculates rectangle perimeter
        __str__: prints a rectangle using the print symbol
        __repr__: returns a string representation of the rectangle
                    to be able to recretae a new instance using eval()
        __del__: deletes a rectangle instance
        bigger_or_equal: returns the biggest rectangle
                                            based on area
        square: returns a new Rectangle instance with width == height == size
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if self.__width != 0 and self.__height != 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        """Prints the rectangle with the # character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        res = str(self.print_symbol) * self.__width
        return (res + "\n") * (self.__height - 1) + res

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes a rectangle instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be a instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangles instance with
            width == height == size

        Args:
            size: width and height value
        """
        return Rectangle(size, size)
