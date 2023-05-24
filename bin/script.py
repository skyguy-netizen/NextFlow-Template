"""
Created on Wed May 10 14:39:07 2023

@author: Aarav Sane
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import pickle
import sys
df = pd.read_feather(sys.argv[1])
# x_col = "precmz"
# y_col = "mz"
# bin_size = 1000000
# print(df)

bin_size = 0.2
bins = {}

# Loop through each row of the dataframe
for index, row in df.iterrows():

    # Round the x and y values to the nearest bin
    x_bin = round(row['precmz'] / bin_size) * bin_size
    y_bin = round(row['mz'] / bin_size) * bin_size

    # Increment the count for this bin
    bin_key = (x_bin, y_bin)
    if bin_key in bins:
        bins[bin_key] += 1
    else:
        bins[bin_key] = 1

# filel = sys.argv[1].split(".")
# filename = filel[0] + ".pickle"
with open(sys.argv[2] , 'wb') as f:
    pickle.dump(bins, f)