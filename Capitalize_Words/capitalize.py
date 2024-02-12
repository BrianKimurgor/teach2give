"""
Write a program that accepts a string as input, capitalizes the first letter
of each word in the string, and then returns the result string
"""
def capitalize_first(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return ' '.join(words)
