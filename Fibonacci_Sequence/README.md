# Explanation
## fibonacci.py

This program defines a function fibonacci_sequence that takes an integer num as input and
returns a list of Fibonacci numbers up to, but not exceeding, num. The function uses a
while loop to generate the Fibonacci sequence, starting with a and b set to 0 and 1, respectively.
In each iteration of the loop, the function appends the current value of a to the sequence list,
then updates a and b to be the next two numbers in the sequence. The loop continues until a is
greater or equal to n.

## test_fibonacci.py
This test file defines a test case called Test_fibonaci that inherits from unittest.TestCase.
The test case includes a single test method called testing_fibonacci that checks whether the
fibonacci_sequence function returns the expected sequence of Fibonacci numbers up to 100.

## testing
To test it,
- navigat to Fibonacci_Sequence directory and returns
```python
     python3 -m unittest test_fibonacci.py
