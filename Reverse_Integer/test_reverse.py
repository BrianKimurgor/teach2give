import unittest
from reverse import reverse_digits

class TestReverseDigits(unittest.TestCase):
    def test_reverse_digits(self):
        self.assertEqual(reverse_digits(12345), 54321)
        self.assertEqual(reverse_digits(6789), 9876)
        self.assertEqual(reverse_digits(0), 0)
        self.assertEqual(reverse_digits(1), 1)

if __name__ == '__main__':
    unittest.main()
