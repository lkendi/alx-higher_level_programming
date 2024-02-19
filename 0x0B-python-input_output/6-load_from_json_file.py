#!/usr/bin/python3
"""Module that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename: name of the JSON file
    """
    with open(filename, "r") as f:
        return json.load(f)
