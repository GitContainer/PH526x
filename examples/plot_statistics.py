import matplotlib.pyplot as plt

from examples.word_stats_pandas import stats

plt.plot(stats.length, stats.unique)
plt.show()