"""
Write a program that prints the numbers from 1 to 100. For multiples of 3,
print "Fizz"; for
multiples of 5, print "Buzz"; and for numbers that are multiples of both
3 and 5, print
"FizzBuzz".
"""


def FizzBuzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def test_fizzbuzz(max_num):
    for num in range(1, max_num + 1):
        print(FizzBuzz(num))
