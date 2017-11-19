import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

print(whisky.head())
print(whisky.iloc[0:10])
print(whisky.iloc[5:10, 0:5])
print(whisky.columns)

flavors = whisky.iloc[:, 2:14]

print(flavors.columns)

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

plt.figure(figsize=(10, 10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("correlation_flavors.pdf")
