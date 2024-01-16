import pandas as pd


def get_seasons_df():
    """

    :return: load and return seasons.csv as pandas dataframe
    """
    seasons_df = pd.read_csv('./F1_dataset/seasons.csv')
    return seasons_df
