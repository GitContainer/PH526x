import string

from functools import reduce

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

message = "hi my name is caesar"


def caesar(message, encryption_key):
    encoding = {char: (value + encryption_key) % 27 for (value, char) in letters.items()}
    return reduce(
        lambda x, y: x + y,
        map(
            lambda char: letters[encoding[char]],
            message
        )
    )

encoded_message = caesar(message, 3)

print(encoded_message)
