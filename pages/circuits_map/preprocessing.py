

def preprocess_map_data_for_year(year, races_circuit_df):
    """
    This function will preprocess data for circuits map for selected year.
    It filters data for selected year, selects only necessary columns and renames them.
    :param year: filter data for selected year
    :param races_circuit_df: dataframe to preprocess
    :return: pandas.DataFrame with columns: ['country', 'circuit_name', 'lat', 'lng']
    """

    # Filter data for selected year
    races_circuit_year_df = races_circuit_df[races_circuit_df['year'] == year]
    # Select only necessary columns
    races_circuit_year_df = races_circuit_year_df[['country', 'name_x', 'lat', 'lng']]
    # Rename columns
    races_circuit_year_df.rename(columns={'name_x': 'circuit_name'}, inplace=True)
    return races_circuit_year_df
