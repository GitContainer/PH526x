from week3.counting_words import count_words
from week3.read_book import read_book


def word_stats(word_counts):
    """Return number of unique words and their frequencies"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)


text = read_book("./resources/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique, sum(counts))

text = read_book("./resources/German/shakespeare/Romeo und Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
# print(num_unique, sum(counts))
