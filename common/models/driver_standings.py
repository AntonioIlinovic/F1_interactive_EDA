import pandas as pd


def get_driver_standings_df():
    """

    :return: load and return driver_standings.csv as pandas dataframe
    """
    driver_standings_df = pd.read_csv('./F1_dataset/driver_standings.csv')
    return driver_standings_df
