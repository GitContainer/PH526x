from week3.casestudy3.majority_vode_scipy import majority_vote
from week3.casestudy3.nearest_neighbors import find_nearest_neighbors, points

import numpy as np


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])

print(knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2))