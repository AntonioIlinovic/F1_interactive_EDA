import pandas as pd


def get_constructor_results_df():
    """

    :return: load and return constructor_results.csv as pandas dataframe
    """
    constructor_results_df = pd.read_csv('./F1_dataset/constructor_results.csv')
    return constructor_results_df
