import pandas as pd


def get_pit_stops_df():
    """

    :return: load and return pit_stops.csv as pandas dataframe
    """
    pit_stops_df = pd.read_csv('./F1_dataset/pit_stops.csv')
    return pit_stops_df
