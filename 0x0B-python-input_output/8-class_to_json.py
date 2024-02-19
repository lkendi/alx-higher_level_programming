#!/usr/bin/python3
"""Class to JSON module
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:"""

    serialized = dict()
    obj_attr = vars(obj)
    for n, v in obj_attr.items():
        if isinstance(v, (list, dict, str, int, bool)):
            serialized[n] = v
    return serialized
