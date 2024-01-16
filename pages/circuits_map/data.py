import pandas as pd
from common.models.races import get_races_df
from common.models.circuits import get_circuits_df
from .preprocessing import preprocess_map_data_for_year


# Load necessary dataframes once
races_df = get_races_df()
circuits_df = get_circuits_df()
races_circuit_df = pd.merge(races_df, circuits_df, on='circuitId')


def get_data_for_map(year):
    """
    This function will return data for circuits map for selected year.
    :return: pandas.DataFrame with columns: ['country', 'circuit_name', 'lat', 'lng']
    """
    return preprocess_map_data_for_year(year, races_circuit_df)
