#!/usr/bin/python3
"""Module that returns an object represented by a JSON string
"""

import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string

    Args:
        my_str(str): JSON string

    Returns:
        Object(Python data structure) represented by my_str
    """
    return json.loads(my_str)
