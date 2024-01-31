import unittest
"""
Unittest for max_integer function
"""

max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Test cases for max_integer function"""
    
    def test_empty_list(self):
        """Empty list test"""
        self.assertEqual(max_integer([]), None)
    def test_single_int(self):
        """Test for list with one integer"""
        self.assertEqual(max_integer([12]), 12)
    def test_many_ints(self):
        """Test for list with multiple integers"""
        self.assertEqual(max_integer([1, 2, 5, 0, 4]), 5)
    def test_same_ints(self):
        """If the max integer is repeated"""
        self.assertEqual(max_integer([5, 4, 3, 2, 5, 1]), 5)
    def test_max_at_beginning(self):
        """If max is at the beginning of the list"""
        self.assertEqual(max_integer([10, 9, 7, 8, 6]), 10)
    def test_max_at_end(self):
        """If max is at the end of the list"""
        self.assertEqual(max_integer([6, 7, 8, 9, 10]), 10)
    def test_max_at_center(self):
        """If max is at the center of the list"""
        self.assertEqual(max_integer([1, 2, 3, 2, 1]), 3)
    def test_list_of_negatives(self):
        """If list contains only negative values"""
        self.assertEqual(max_integer([-1, -2, -10, -6]), -1)
    def test_list_with_negatives(self):
        """If list contains a mix of negative and positive values"""
        self.assertEqual(max_integer([-1, -2, -10, -6, 1, 20, 8]), 20)
    def test_non_ints(self):
        """List that does not contain integers"""
        with self.assertRaises(TypeError):
            max_integer([2, "3", 4.5])
    def test_non_list(self):
        with self.assertRaises(TypeError):
            max_integer(1091)
            
if __name__ == '__main__':
    unittest.main()