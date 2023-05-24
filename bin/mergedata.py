import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import sys
import pickle
import os
import argparse
import glob

def main():
    parser = argparse.ArgumentParser(description='creating histogram.')
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
                bins1[x] += bins1[x]
            else:
                bins[x] = bins1[x]

    with open(args.output_filename, 'wb') as f:#save merged file
        pickle.dump(bins, f)

if __name__ == "__main__":
    main()



