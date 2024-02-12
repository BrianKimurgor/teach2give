"""
Write a program that counts the number of vowels in a sentence.
"""

def count_vowels(sentence):
    """Counts the number of vowels in a sentence."""
    vowels = "aeiou"
    sentence = sentence.lower()
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
