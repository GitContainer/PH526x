import numpy as np
import time

start_time = time.clock()
X = np.random.randint(1, 7, (1000000, 10))
Y = np.sum(X, axis=1)
end_time = time.clock()
print(end_time - start_time)
