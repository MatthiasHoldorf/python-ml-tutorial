import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

dataset = pd.read_csv("KAG_conversion_data.csv")

print(dataset.head())
print(dataset.info())
print(dataset.shape)
print(dataset.describe())

print("We have customers from age groups as follows:")
print(dataset['age'].unique())
