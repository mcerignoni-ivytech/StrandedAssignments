import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """Test that it can sum a list of integers"""
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """Test that it can sum a list of fractions"""
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)  #intentionally wrong

if __name__ == "__main__":
    unittest.main()


"""
The test results showed one pass, indicated by a dot, and one fail, marked with an F.
While the integer addition test worked perfectly, the second test failed because the function returned 9/10 instead of the expected 1.
The test runner made the error obvious by displaying the specific test name and comparing the expected value to the actual result side-by-side.
"""
