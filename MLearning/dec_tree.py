import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import random
from pprint import pprint

def train_test_split(df, test_size):
    if isinstance(test_size, float):
        test_size = round(test_size * len(df))

    indices = df.index.tolist()
    test_indices = random.sample(population=indices, k=test_size)

    test_df = df.loc[test_indices]
    train_df = df.drop(test_indices)

    return train_df, test_df

#Read data
df = pd.read_csv("Iris.csv")
df = df.rename(columns={"species": "label"})

#Split data
random.seed(0)
train_df, test_df = train_test_split(df, test_size=20)

#Tree algorithm
#tree = decision_tree_algorithm(train_df)

#Calc. accuracy
#accuracy = calculate_accuracy(test_df, tree)
