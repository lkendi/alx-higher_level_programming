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
    def test_non_ints(self):
        """List that does not contain integers"""
        with self.assertRaises(TypeError):
            max_integer([2, "3", 4.5])
    def test_non_list(self):
        with self.assertRaises(TypeError):
            max_integer(1091)
            
if __name__ == '__main__':
    unittest.main()