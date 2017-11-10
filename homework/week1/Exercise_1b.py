import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!

for letter in sentence:
    if letter in alphabet:
        if not letter in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1

print(count_letters.items())
