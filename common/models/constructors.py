import pandas as pd


def get_constructors_df():
    """

    :return: load and return constructors.csv as pandas dataframe
    """
    constructors_df = pd.read_csv('./F1_dataset/constructors.csv')
    return constructors_df
