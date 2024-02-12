import unittest
from fibonacci import Fibonacci

class test_fibonacci(unittest.TestCase):
    def testing_fibonacci(self):
        result = Fibonacci(100)
        self.assertEqual(result, [0, 1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


if __name__ == '__main__':
    unittest.main()
