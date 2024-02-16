"""Unittest module for the square class
"""


import unittest
import io
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5, 7, 8, 9)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 9)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            s.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

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


if __name__ == '__main__':
    unittest.main()