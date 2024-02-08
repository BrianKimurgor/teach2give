import unittest
from fizzbuzz import FizzBuzz


"""
This is a unit test suit for the FizzBuzz function
- 'unittest' module defines a test suite and test cases
- 'testfizzbuzz' class where test suite is defined containing:
    -"test_fizz" checks if the function returnz "Fizz" for multiples of 3
    -"test_buzz" checks if the function returns "Buzz" for multiples of 5
    -"test fizz_buzz" checkss if the function returns "FizzBuzz" for
    multiples of 15
    -"test_number" checks if the function returns the input number for
    number not multiple of 3 or 5
"""


class testfizzbuzz(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 9, 18]:
            self.assertEqual(FizzBuzz(i), "Fizz")

    def test_buzz(self):
        for i in [5, 10, 20]:
            self.assertEqual(FizzBuzz(i), "Buzz")

    def test_fizzbuzz(self):
        for i in [15, 30, 45]:
            self.assertEqual(FizzBuzz(i), "FizzBuzz")

    def test_number(self):
        for i in [1, 2, 4, 7]:
            self.assertEqual(FizzBuzz(i), i)


if __name__ == "__main__":
    unittest.main()
