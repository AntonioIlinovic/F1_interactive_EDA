import pandas as pd


def preprocess_constructor_standings_data_for_graph_for_year(year, constructors_df, constructor_standings_df, races_df):
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


def preprocess_constructor_standings_data_for_table_for_year(year, constructors_df, constructor_standings_df, races_df):
    """

    :param year:
    :param constructors_df:
    :param constructor_standings_df:
    :param races_df:
    :return:
    """
    constructor_championship_table_df = constructor_standings_df[
        ['raceId', 'constructorId', 'points', 'position', 'wins']]
    constructor_championship_table_df = pd.merge(constructor_championship_table_df,
                                                 races_df[['raceId', 'year', 'round']], on='raceId')
    constructor_championship_table_df = pd.merge(constructor_championship_table_df,
                                                 constructors_df[['constructorId', 'name', 'nationality']],
                                                 on='constructorId')
    constructor_championship_table_df = constructor_championship_table_df.drop(['raceId'], axis=1)

    # Get standings for selected year
    constructor_championship_table_year_df = constructor_championship_table_df[
        constructor_championship_table_df['year'] == year]
    constructor_championship_table_year_df = constructor_championship_table_year_df.sort_values(by=['round'],
                                                                                                ascending=False)
    constructor_championship_table_year_df = constructor_championship_table_year_df.groupby(['constructorId']).head(1)
    constructor_championship_table_year_df = constructor_championship_table_year_df.drop(
        ['year', 'round', 'constructorId'], axis=1)
    constructor_championship_table_year_df.sort_values(by=['position'], inplace=True)
    constructor_championship_table_year_df.rename(columns={'name': 'constructor_name'}, inplace=True)
    constructor_columns_reordered = ['position', 'constructor_name', 'nationality', 'wins', 'points']
    constructor_championship_table_year_df = constructor_championship_table_year_df[constructor_columns_reordered]
    return constructor_championship_table_year_df
