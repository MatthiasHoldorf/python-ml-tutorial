import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("KAG_conversion_data.csv")

g = sns.FacetGrid(df, col="gender", hue="age")
g.map(plt.scatter, "Impressions", "Clicks", alpha=.4)
g.add_legend();

g = sns.FacetGrid(df, col="age", hue="gender")
g.map(plt.scatter, "Impressions", "Clicks", alpha=.4)
g.add_legend();
print(g)
