import random
import numpy as np
import matplotlib.pyplot as plt

rolls = []
for k in range(100):
    rolls.append(random.choice(range(1, 7)))

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7));
