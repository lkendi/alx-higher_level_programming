#!/usr/bin/python3
"""Base class module
"""


import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of a JSON string representation

        Args:
            jdon_string: string rep of a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file = cls.__name__ + ".json"
        try:
            with open(file, "r") as f:
                contents = f.read()
                dict_list = cls.from_json_string(contents)
                return [cls.create(**obj) for obj in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the list_objs to a CSV file

        Args:
            list_objs: list of instances
        """
        if list_objs is None:
            list_objs = []
        file = cls.__name__ + ".csv"
        with open(file, "w", newline='') as f:
            writer = csv.writer(f, delimiter=",")
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances list from CSV file"""
        file = cls.__name__ + ".csv"
        try:
            instances = []
            with open(file, "r", newline='') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        my_dict = {'id': int(row[0]), 'width': int(row[1]),
                                   'height': int(row[2]), 'x': int(row[3]),
                                   'y': int(row[4])}
                    elif cls.__name__ == "Square":
                        my_dict = {'id': int(row[0]), 'size': int(row[1]),
                                   'x': int(row[2]), 'y': int(row[3])}
                    instance = cls.create(**my_dict)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares
        using the Turtle graphics module

        Args:
            list_rectangles: list of rectangle instances
            list_squares: list of square instances
        """
        window = turtle.Screen()
        pen = turtle.Turtle()
        pen.penup()
        pen.speed(1)

        for rect in list_rectangles:
            pen.color("red")
            pen.begin_fill()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.right(90)
            pen.forward(rect.width)
            pen.right(90)
            pen.forward(rect.height)
            pen.end_fill()
            pen.penup()

        for sq in list_squares:
            pen.color("blue")
            pen.begin_fill()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(sq.size)
                pen.right(90)
            pen.end_fill()
            pen.penup()

        window.exitonclick()


