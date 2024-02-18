#!/usr/bin/python3
"""Module that writes to a file
"""


def write_file(filename="", text=""):
    """Function that writes to UTF8 text file and
    returns the number of characters written

    Args:
        filename(str): name of text file
        text(str): text to write to the file

    Returns:
        Number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
