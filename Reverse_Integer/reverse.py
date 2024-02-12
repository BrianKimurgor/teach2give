"""
Write a program that takes an integer as input and returns
an integer with reversed digit
ordering.
"""


def reverse_digits(num):
    """Reverses the digit ordering of an integer."""
    if num < 0:
        return -int(str(-num)[::-1])
    else:
        return int(str(num)[::-1])
