import pandas as pd


def get_status_df():
    """

    :return: load and return status.csv as pandas dataframe
    """
    status_df = pd.read_csv('./F1_dataset/status.csv')
    return status_df
