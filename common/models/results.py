import pandas as pd


def get_results_df():
    """

    :return: load and return results.csv as pandas dataframe
    """
    results_df = pd.read_csv('./F1_dataset/results.csv')
    return results_df
