#!/usr/bin/python3
"""
LockedClass module
"""


class LockedClass:
    """Class that restricts creation of new instance attribute

    Attributes:
        __slots__: Tuple containing the allowed instance attribute names
                    (in this case - 'first_name')
    Mathods:
        __setattr__: controls attribute creation
    """

    __slots__ = ('first_name',)  # Allow only 'first_name' attribute

    def __setattr__(self, name, value):
        """Function that overrides the default behavior of __setattr__
        in order to restric the creation of instance attributes

        Args:
            name(str): name of attribute to set
            value: valueto assign to the attribute

        Raises:
            AttributeError: if attribute name is not first_name
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
        super().__setattr__(name, value)
