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

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        student_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return student_dict
