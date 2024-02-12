# Explanation
## count.py
The count_vowels function converts the input string to lowercase using the lower() method,
and then iterates over each character in the string using a for loop. If the character is
a vowel (i.e., if it is in the vowels string), the function increments a count variable.
Finally, the function returns the count variable.

## test_count.py
The test file uses the unittest module to define a test case called TestCountVowels.
The test case includes several test methods that check the count_vowels function with various inputs.

To run the test, you can use the following command in your terminal:
```python
 python3 -m unittest test_count.py
