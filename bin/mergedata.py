import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import sys
import pickle
import os

bins = {}
mergedfile = sys.argv[1]

files = int(sys.argv[2])

for i in range(1, files+1):
    with open(sys.argv[i+2], 'rb') as f:#read file 1
        bins1 = pickle.load(f)
    for x in bins1:
        if x in bins:
            bins1[x] += bins1[x]
        else:
            bins[x] = bins1[x]



# with open(sys.argv[2], 'rb') as f:#read file 2
#     bins2 = pickle.load(f)

# for x in bins2:
#     if x in bins1:
#         bins1[x] += bins2[x]
#     else:
#         bins1[x] = bins2[x]


# histlist = [(k[0], k[1], v) for k, v in bins1.items()]
# x = [item[0] for item in histlist]
# y = [item[1] for item in histlist]
# counts = [item[2] for item in histlist]


# plt.hist2d(x, y, bins=[1000, 1000], weights=counts)
# plt.xlabel('precmz')
# plt.ylabel('mz')
# plt.colorbar()
# plt.savefig(sys.argv[4])

with open(mergedfile, 'wb') as f:#save merged file
    pickle.dump(bins, f)





