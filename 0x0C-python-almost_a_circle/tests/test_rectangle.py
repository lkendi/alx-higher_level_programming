"""Unittest module for the rectangle class
"""


import unittest
import io
import sys
import os
import unittest.mock
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 9)

    def test_init_with_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_init_with_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
    
    def test_init_with_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_init_with_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_init_with_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_init_with_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
    
    def test_init_with_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_init_with_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_init_with_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_init_with_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_display(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)
    
    def test_display_without_x_and_y(self):
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with io.StringIO() as output:
            sys.stdout = output
            r.display()
            self.assertEqual(output.getvalue(), expected_output)
        sys.stdout = sys.__stdout__

    def test_display_without_y(self):
        r = Rectangle(2, 3, 1)
        expected_output = " ##\n ##\n ##\n"
        with io.StringIO() as output:
            sys.stdout = output
            r.display()
            self.assertEqual(output.getvalue(), expected_output)
        sys.stdout = sys.__stdout__
    
    def test_str(self):
        r = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 5/6 - 3/4")

    def test_update(self):
        r = Rectangle(1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_save_to_file_single_instance(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_to_dictionary(self):
        r = Rectangle(3, 4, 5, 6, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 5, 'y': 6}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
