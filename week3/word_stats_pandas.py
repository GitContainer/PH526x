import os

import pandas as pd
from week3.counting_words import count_words
from week3.word_stats import word_stats

from week3.read_book import read_book

book_dir = "./resources"

stats = pd.DataFrame(columns=("language", "author", "title", "length", "unique"))

title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt", ""), sum(counts), num_unique
            title_num += 1

print(stats.head())
