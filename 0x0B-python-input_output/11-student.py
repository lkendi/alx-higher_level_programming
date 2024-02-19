#!/usr/bin/python3
"""Student module
"""


class Student():
    """Student class

    Attributes:
        first_name(str; public): student's first name
        last_name(str; public): student's last name
        age(int; public): student's age

    Methods:
        init: constructor
        to_json : retrieves a dictionary representation of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        containing only attributes listed in attrs"""
        if attrs is None:
            """otherwise retrieve all attributes"""
            return self.__dict__
        else:
            student_dict = {}
            for a in attrs:
                if hasattr(self, a):
                    student_dict[a] = getattr(self, a)
        return student_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
