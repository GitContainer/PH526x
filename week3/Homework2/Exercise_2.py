import numpy as np

from week3.Homework2.Exercise_1 import distribution


def more_frequent(distribution):
    # return dict((key, value) for key,value in distribution.items() if value > key)
    counts = list(distribution.keys())
    frequency_of_counts = list(distribution.values())
    cumulative_frequencies = np.cumsum(frequency_of_counts)
    more_frequent = 1 - cumulative_frequencies / cumulative_frequencies[-1]
    return dict(zip(counts, more_frequent))


cumulative = more_frequent(distribution)
print(cumulative)
