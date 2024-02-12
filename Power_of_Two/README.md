# Explanation
## power.py
The powerOfTwo function takes an integer num as input and returns a boolean
value indicating whether or not num is a power of two. Here's a step-by-step
explanation of the function:
- The function uses an if statement to check if num is divisible by 2 with no remainder.
If num is a power of two, it must be even because any two consecutive powers of two differ by a factor of 2.
- If num is even, the function returns True. This indicates that num is a power of two.
- If num is not even, the function returns False. This indicates that num is not a power of two.

## test_power.py
This is a test file for the powerOfTwo function, which checks if a given integer is a power of two.

Run the test file from the terminal using the following command:
```python
 python3 -m unittest test_power.py
