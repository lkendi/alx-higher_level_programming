#!/usr/bin/python3
"""BaseGeometry class module
"""


class BaseGeometry:
    """BaseGeometry class

    Methods:
        area: raises an exception
        integer_validator: validates a value passed to it
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates a value

        Args:
            name(str): name
            value(int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if valeue is less or equal to 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(str(name)))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))
