#!/usr/bin/python3
"""Module that appends to a file
"""


def append_write(filename="", text=""):
    """Function that appends a string to the end of a UTF8 text file
    and returns the number of characters added

    Args:
        filename(str): name of text file
        text(str): text to write to the file

    Returns:
        Number of characters written to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
