"""Unittest module for the square class
"""


import unittest
import io
import sys
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5, 7, 8, 9)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 9)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -1)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("test")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(1, "test")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(1, 1, "test")

    def test_display(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_no_xy(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_no_x(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)


    def test_str(self):
        s = Square(3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (6) 4/5 - 3")

    def test_update(self):
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        s = Square(3, 4, 5, 6)
        expected_dict = {'id': 6, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_update(self):
            s = Square(1)
            s.update(2, 3, 4, 5)
            self.assertEqual(s.id, 2)
            self.assertEqual(s.size, 3)
            self.assertEqual(s.x, 4)
            self.assertEqual(s.y, 5)

    def test_create(self):
        s1_dict = {'id': 1, 'size': 5}
        s2_dict = {'id': 2, 'size': 10}
        s1 = Square.create(**s1_dict)
        s2 = Square.create(**s2_dict)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 10)

    def test_load_from_file(self):
        s1 = Square(5)
        s2 = Square(10)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)


if __name__ == '__main__':
    unittest.main()