import pandas as pd


def get_constructor_standings_data_for_year(year, constructors_df, constructor_standings_df, races_df):
    """

    :param year:
    :param constructors_df:
    :param constructor_standings_df:
    :param races_df:
    :return:
    """
    constructor_standings_year_df = pd.merge(constructor_standings_df, races_df, on='raceId')
    # Filter only for the given year
    constructor_standings_year_df = constructor_standings_year_df[constructor_standings_year_df['year'] == year]
    constructor_standings_year_df = pd.merge(constructor_standings_year_df, constructors_df, on='constructorId')
    constructor_standings_year_df = constructor_standings_year_df[['name_x', 'name_y', 'points', 'round']]
    # Rename columns
    constructor_standings_year_df.rename(columns={'name_x': 'circuit_name', 'name_y': 'constructor_name'}, inplace=True)
    constructor_standings_year_df.sort_values(by='round', inplace=True)
    return constructor_standings_year_df
