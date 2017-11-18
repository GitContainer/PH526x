import numpy as np
import matplotlib.pyplot as plt

# loop over all points
# compute the distance between p and each point
# sort distances and return those k points that are nearest to p
from week3.casestudy3.vector_distance import distance

points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
p = np.array([2.5, 2])


def find_nearest_neighbors(p, points, k=5):
    """Find the k nearest neighbors of point p and return their indices"""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


ind = find_nearest_neighbors(p, points, 2)
print(points[ind])

plt.plot(points[:, 0], points[:, 1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
plt.show()
