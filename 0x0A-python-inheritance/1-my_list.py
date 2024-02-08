#!/usr/bin/python3
"""Module that creates a subclass of list"""


class MyList(list):
    """Subclass of list

    Methods:
        print_sorted: prints the list sorted in ascending order"""

    def print_sorted(self):
        print(sorted(self))
