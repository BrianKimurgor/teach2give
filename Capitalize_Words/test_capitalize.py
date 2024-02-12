import unittest
from capitalize import capitalize_first

class test_capitalize(unittest.TestCase):
    def test_first(self):
        self.assertEqual(capitalize_first("hello world"), "Hello World")
        self.assertEqual(capitalize_first("HELLO WORLD"), "Hello World")
        self.assertEqual(capitalize_first("this is a test"), "This Is A Test")
        self.assertEqual(capitalize_first("This is a test "), "This Is A Test")
        self.assertEqual(capitalize_first("12345"), "12345")

if __name__ == "__main__":
    unittest.main()
