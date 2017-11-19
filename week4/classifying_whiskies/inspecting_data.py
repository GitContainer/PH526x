import numpy as np
import pandas as pd

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

print(whisky.head())
print(whisky.iloc[0:10])
print(whisky.iloc[5:10, 0:5])
print(whisky.columns)

flavors = whisky.iloc[:, 2:14]

print(flavors.columns)