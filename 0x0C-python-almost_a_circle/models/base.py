#!/usr/bin/python3
"""Base class module
"""


import json


class Base:
    """Base class

    Attributes:
        __nb_objects: private counter
        id: public identifier

    Methods:
        __init__: constructor
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string rep of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string rep of list_objs to a file

        Args:
            list_objs: list og instances who inherits of Base
                    e.g Rectangle and Square instances
        """
        if list_objs is None:
            list_objs = []
        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs]))
