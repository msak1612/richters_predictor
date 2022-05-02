import pandas as pd


# Collect train data(features & labels) and merge into single dataframe
def make_train_dataset():
    data_file = "../data/raw/train_values.csv"
    labels_file = "../data/raw/train_labels.csv"

    # Read datafrom csv file
    df1 = pd.read_csv(data_file)
    df2 = pd.read_csv(labels_file)

    # Check the shape of dataframes
    print(f'Shape of Feature dataset: {df1.shape}')
    print(f'Shape of Target dataset: {df2.shape}')

    # Merges feature and target dataset
    return pd.merge(df1, df2, on='building_id', how='inner')


# Collect test data
def make_test_dataset():
    test_file = "../data/raw/test_values.csv"

    # Read datafrom csv file
    df = pd.read_csv(test_file)

    # Check the shape of dataframes
    print(f'Shape of Test dataset: {df.shape}')

    return df
