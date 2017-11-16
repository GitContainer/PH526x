import matplotlib.pyplot as plt

from examples.word_stats_pandas import stats

plt.plot(stats.length, stats.unique, "bo")
plt.figure(figsize=(10, 10))

subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")

subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")

subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")

subset = stats[stats.language == "Portugese"]
plt.loglog(subset.length, subset.unique, "o", label="Portugese", color="blueviolet")

plt.legend()
plt.xlabel("Book length")
plt.ylabel("Number of unique words")

plt.savefig("lang_plot.pdf")

plt.show()
