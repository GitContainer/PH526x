import string

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

encryption_key = 3

encoding = {char: (value + encryption_key) % 27 for (value, char) in letters.items()}

print(encoding)