import pandas as pd


def get_qualifying_df():
    """

    :return: load and return qualifying.csv as pandas dataframe
    """
    qualifying_df = pd.read_csv('./F1_dataset/qualifying.csv')
    return qualifying_df
