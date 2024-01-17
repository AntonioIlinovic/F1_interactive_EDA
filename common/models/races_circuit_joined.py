import pandas as pd


def join_races_circuits_df(races_df, circuits_df):
    """
    Function joins races and circuits dataframes on circuitId column.
    :return: joined dataframe
    """
    return pd.merge(races_df, circuits_df, on='circuitId')
