import pandas as pd


def get_drivers_df():
    """

    :return: load and return drivers.csv as pandas dataframe
    """
    drivers_df = pd.read_csv('./F1_dataset/drivers.csv')
    return drivers_df
