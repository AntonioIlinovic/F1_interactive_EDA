import pandas as pd


def get_races_df():
    """

    :return: load and return races.csv as pandas dataframe
    """
    races_df = pd.read_csv('./F1_dataset/races.csv')
    return races_df
