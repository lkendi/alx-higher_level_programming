#!/usr/bin/python3

class LockedClass:
    __slots__ = ('first_name',)  # Allow only 'first_name' attribute

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(name))
        super().__setattr__(name, value)
