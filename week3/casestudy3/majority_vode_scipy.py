import random
import scipy.stats as ss


def majority_vote(votes):
    """
    Return the most common element in votes
    """
    mode, count = ss.mstats.mode(votes)
    return mode


votes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 2]
winner = majority_vote(votes)

print(winner)
