from collections import Counter

from week3.counting_words import count_words
from week3.read_book import read_book


def word_count_distribution(text):
    word_counts = count_words(text)
    print(word_counts)
    count = Counter(frequency for frequency in word_counts.values())
    count_distribution = dict(count)

    return count_distribution


text = read_book("../resources/English/shakespeare/Romeo and Juliet.txt")

distribution = word_count_distribution(text)
print(distribution)
