import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import sys
import pickle
import os

bins = {}
# mergedfile = sys.argv[1]

files = int(sys.argv[2])

for i in range(1, files+1):
    with open(sys.argv[i+2], 'rb') as f:#read file 1
        bins1 = pickle.load(f)
    for x in bins1:
        if x in bins:
            bins[x] += bins1[x]
        else:
            bins[x] = bins1[x]


histlist = [(k[0], k[1], v) for k, v in bins.items()]
x = [item[0] for item in histlist]
y = [item[1] for item in histlist]
counts = [item[2] for item in histlist]

print(histlist)

plt.hist2d(x, y, bins=[500, 500], weights=counts)
plt.xlabel('precmz')
plt.ylabel('mz')
plt.colorbar()
plt.savefig(sys.argv[1])