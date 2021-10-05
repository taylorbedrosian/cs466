import pandas
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
parser.add_argument('--minrs', type=int)
args = parser.parse_args()

GOODS_FILE = "goods.csv"
BAKERY_OUT2= "-out2.csv"

def load_good_labels(filename):
    # labeled goods df, indexed on Id has Flavor, Food, Price, Type column
    good_labels_df = pandas.read_csv(filename, index_col="Id")
    return good_labels_df

def load_full_bv_bakery(filename):
    # indexed by transaction id, .iloc[tid][item_id] to get value
    full_bv_df = pandas.read_csv(filename, index_col=0, header=None, 
                                 names=[i for i in range(51)])
    # example full_bv_df.iloc[2][2]
    return full_bv_df

def apriori_freq_first_pass(transactions, items, minsup):
    """
    transactions - df from -out2 file
    items - list from 1-50 representing bakery items and indeces of df vector
    minsup - minsupport
    """
    item_counts = {i: sum(transactions[i]) for i in transactions.columns}
    sum_all_items = sum(item_counts[i] for i in transactions.columns)
    item_rsup = {i: item_counts[i] / sum_all_items for i in transactions.columns}
    print(item_rsup)
    for tid in transactions.columns:
        continue
        """
        transaction = transactions[tid]
        for item in items:
            item_count[item] += transaction[tid][item]
        """


def apriori_freq_itemsets(transactions, items, minsup):
    # first pass    
    pass
    

if __name__ == "__main__":
    good_labels_df = load_good_labels(GOODS_FILE)
    bakery_bv_df = load_full_bv_bakery(f"1000/1000{BAKERY_OUT2}")
    apriori_freq_first_pass(bakery_bv_df, (i for i in range(1, 51)), 0.08)


