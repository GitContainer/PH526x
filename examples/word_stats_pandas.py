import os
import pandas as pd

from examples.counting_words import count_words
from examples.read_book import read_book
from examples.word_stats import word_stats

book_dir = "./resources"

stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))

title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            # print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author, title, sum(counts), num_unique
            title_num += 1

print(stats)
