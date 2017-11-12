"""
Create a dictionary letters with keys consisting of the numbers from 0 to 26,
and values consisting of the lowercase letters of the English alphabet,
including the space ' ' at the end.
"""

import string

string.ascii_lowercase

alphabet = string.ascii_lowercase + " "

letters = {}
i = 0
for letter in alphabet:
    letters[i] = letter
    i += 1

print(letters)
