import unittest
from count import count_vowels

class TestCountVowels(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("This is a test sentence."), 7)
        self.assertEqual(count_vowels("Hello world!"), 3)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

if __name__ == '__main__':
    unittest.main()
