import os
import pandas as pd

from week3.Homework2.Exercise_1 import word_count_distribution
from week3.read_book import read_book

hamlets = pd.DataFrame(columns=("language", "distribution"))

book_dir = "../resources"

title_num = 1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            if title == "Hamlet":
                inputfile = book_dir + "/" + language + "/" + author + "/" + title
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1
