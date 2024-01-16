import pandas as pd


def get_lap_times_df():
    """

    :return: load and return lap_times.csv as pandas dataframe
    """
    lap_times_df = pd.read_csv('./F1_dataset/lap_times.csv')
    return lap_times_df
