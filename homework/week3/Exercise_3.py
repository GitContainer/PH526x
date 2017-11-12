import string

alphabet = string.ascii_lowercase + " "
letters = dict(enumerate(alphabet))

message = "hi my name is caesar"


def caesar(message, encryption_key):
    encoded_message = ""
    encoding = {char: (value + encryption_key) % 27 for (value, char) in letters.items()}
    for letter in message:
        encoded_message += letters[encoding[letter]]
    return encoded_message


encoded_message = caesar(message, 3)

print(encoded_message)
