#!/usr/bin/python3
"""Module that reads a text file
"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout

    Args:
        filename(str): name of text file to read (UTF8)
    """
    with open(filename, "r", encoding="utf-8") as f:
        f.read()
