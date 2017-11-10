import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'


# Create your function here!
def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if not letter in count_letters:
                count_letters[letter] = 1
            else:
                count_letters[letter] += 1
    return count_letters


count_letters = counter(sentence)
print(count_letters.items())

most_frequent_letter = max(count_letters, key=count_letters.get)
print(most_frequent_letter)
