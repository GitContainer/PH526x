import numpy as np
import matplotlib.pyplot as plt

# loop over all points
# compute the distance between p and each point
# sort distances and return those k points that are nearest to p

points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])

p = np.array([2.5, 2])
plt.plot(points[:, 0], points[:, 1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
plt.show()
