import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import sys
import pickle
import os
import glob
import argparse

def main():
    parser = argparse.ArgumentParser(description='creating final histogram.')
    parser.add_argument('input_folder')
    parser.add_argument('output_filename')

    args = parser.parse_args()

    bins = {}

    # Getting the filenames
    input_files = glob.glob(args.input_folder + "/*.pickle")

    for input_filename in input_files:
        with open(input_filename, 'rb') as f:#read file 1
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
    plt.savefig(args.output_filename)

if __name__ == "__main__":
    main()