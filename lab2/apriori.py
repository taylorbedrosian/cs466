import pandas
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--minrs', type=int)
args = parser.parse_args()

def load_good_labels(filename):
    good_labels_dataframe = pandas.read_csv(filename, index_col="Id")
    print(good_labels_dataframe)

load_good_labels(args.file)
