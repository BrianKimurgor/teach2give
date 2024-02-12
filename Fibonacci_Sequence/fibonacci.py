"""
Write a program to generate the Fibonacci sequence up to 100.
"""

def Fibonacci(num):
    sequence = [0, 1]
    a, b = 0, 1
    while b <= num:
        a, b = b, a + b
        sequence.append(a)
    return sequence
