# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:59:21 2017

@author: ahasani
"""
from collections import Counter

text = "dummy text for counting 'Dummy' words. dummy code - dummy text."


def count_words(text):
    """
    Count the number of times each word occurs in text
    """
    text = text.lower();
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts


#print(count_words(text))
