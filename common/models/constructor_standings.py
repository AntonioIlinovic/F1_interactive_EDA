import pandas as pd


def get_constructor_standings_df():
    """

    :return: load and return constructor_standings.csv as pandas dataframe
    """
    constructor_standings_df = pd.read_csv('./F1_dataset/constructor_standings.csv')
    return constructor_standings_df
