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
import argparse

def main():
    parser = argparse.ArgumentParser(description='creating histogram.')
    parser.add_argument('input_filename')
    parser.add_argument('output_filename')

    args = parser.parse_args()

    df = pd.read_feather(args.input_filename)
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

    with open(args.output_filename , 'wb') as f:
        pickle.dump(bins, f)

if __name__ == "__main__":
    main()