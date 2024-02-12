import unittest
from power import powerOfTwo


class testPower(unittest.TestCase):
    def test_power(self):
        self.assertFalse(powerOfTwo(1))
        self.assertTrue(powerOfTwo(2))
        self.assertTrue(powerOfTwo(16))
        self.assertFalse(powerOfTwo(3))
        self.assertFalse(powerOfTwo(5))
        self.assertFalse(powerOfTwo(7))
        self.assertFalse(powerOfTwo(9))

if __name__ == '__main__':
    unittest.main()
