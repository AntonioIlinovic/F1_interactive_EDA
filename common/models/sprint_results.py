import pandas as pd


def get_sprint_results_df():
    """

    :return: load and return sprint_results.csv as pandas dataframe
    """
    sprint_results_df = pd.read_csv('./F1_dataset/sprint_results.csv')
    return sprint_results_df
