"""Unittest module for the base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_nb_objects_increment(self):
        obj1 = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        obj2 = Base()
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"key": "value"}]),
                         '[{"key": "value"}]')

    def test_save_to_file(self):
        r1 = Rectangle(5, 6, 7, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "width": 5, "height": 6, '
                             '"x": 7, "y": 8}, '
                             '{"id": 2, "width": 2, "height": 4, '
                             '"x": 0, "y": 0}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"key": "value"}]'),
                         [{"key": "value"}])

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 is r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        r1 = Rectangle(5, 5)
        r2 = Rectangle(10, 10)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)


if __name__ == "__main__":
    unittest.main()
