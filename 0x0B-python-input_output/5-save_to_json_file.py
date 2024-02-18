#!/usr/bin/python3
"""Module that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using a JSON representation

    Args:
        my_obj: object to write
        filename: name of the text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
