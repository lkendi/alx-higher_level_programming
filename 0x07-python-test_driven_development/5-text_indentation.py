#!/usr/bin/python3
"""
Module that indents text
"""


def text_indentation(text):
    """Prints a text with 2 new lines after
        each of these characters: ., ? and :
        Ensuring that there is no space at the beginning
        or at the end of each printed line

    Args:
        text(str): text to indent

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""
    for char in text:
        current_line += char
        if char in ['.', '?', ':']:
            print(current_line.strip())
            print("\n")
            current_line = ""
    if current_line:
        print(current_line.strip())
