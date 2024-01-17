import pandas as pd
from common.utils.utils import load_dataset, DatasetName
from .preprocessing import preprocess_map_data_for_year


print('Loading circuits map data...')
# Load necessary dataframes once
races_df = load_dataset(DatasetName.RACES)
circuits_df = load_dataset(DatasetName.CIRCUITS)
races_circuit_df = pd.merge(races_df, circuits_df, on='circuitId')


def get_data_for_map(year):
    """
    This function will return data for circuits map for selected year.
    :return: pandas.DataFrame with columns: ['country', 'circuit_name', 'lat', 'lng']
    """
    return preprocess_map_data_for_year(year, races_circuit_df)
