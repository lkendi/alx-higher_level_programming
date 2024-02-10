#!/usr/bin/python3
"""MyInt class module
"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, obj):
        """Equality function inverted"""
        return not super().__eq__(obj)

    def __ne__(self, obj):
        """Inequality function inverted"""
        return not super().__ne__(obj)
