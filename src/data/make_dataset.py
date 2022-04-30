# -*- coding: utf-8 -*-
import pandas as pd


def make_train_dataset():
    data_file = "../data/raw/train_values.csv"
    labels_file = "../data/raw/train_labels.csv"

    #Collecting Data
    df1 = pd.read_csv(data_file)
    df2 = pd.read_csv(labels_file)

    print(f'Shape of Feature dataset: {df1.shape}')
    print(f'Shape of Target dataset: {df2.shape}')

    #merges feature and target dataset
    return pd.merge(df1, df2, on='building_id', how='inner')


def make_test_dataset():
    test_file = "../data/raw/test_values.csv"

    #Collecting Data
    df = pd.read_csv(test_file)

    print(f'Shape of Test dataset: {df.shape}')

    return df
