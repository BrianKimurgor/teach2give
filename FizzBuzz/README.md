#FIZZBUZZ explanation

## explanation
 This code is a Python program that follows the FizzBuzz challenge but has an added function to test the output for a given range of numbers.

The first part is a docstring summarizing the program's objective.

The FizzBuzz function takes an integer num as input and returns a string based on the following rules:

- If num is divisible by both 3 and 5 (i.e., a multiple of 15), return "FizzBuzz".
- If num is only divisible by 3, return "Fizz".
- If num is only divisible by 5, return "Buzz".
- If none of the above conditions are met, return the input number as a string.
- The test_fizzbuzz function tests the FizzBuzz function by printing its output for numbers in the range from 1 to the given max_num.

###Testing
- go to the FizzBuzz directory
- to test the code with the test file, run:
```Python
    python3 -m unittest test_fizzbuzz.py
    ```
