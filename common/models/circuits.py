import pandas as pd


def get_circuits_df():
    """

    :return: load and return circuits.csv as pandas dataframe
    """
    circuits_df = pd.read_csv('./F1_dataset/circuits.csv')
    return circuits_df
