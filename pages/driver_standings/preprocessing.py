import pandas as pd


def preprocess_driver_standings_data_for_graph_for_year(year, drivers_df, driver_standings_df, races_df):
    driver_standings_year_df = pd.merge(driver_standings_df, races_df, on='raceId')
    driver_standings_year_df = driver_standings_year_df[driver_standings_year_df['year'] == year]
    driver_standings_year_df = pd.merge(driver_standings_year_df, drivers_df, on='driverId')
    driver_standings_year_df = driver_standings_year_df[
        ['forename', 'surname', 'code', 'number', 'name', 'points', 'round']]
    driver_standings_year_df['full_name'] = driver_standings_year_df['forename'] + ' ' + driver_standings_year_df[
        'surname']
    driver_standings_year_df.drop(['forename', 'surname'], axis=1, inplace=True)
    driver_standings_year_df.rename(columns={'name': 'circuit_name', 'code': 'driver_code', 'number': 'driver_number',
                                             'round': 'race_of_the_season'}, inplace=True)
    driver_standings_year_df.sort_values(by='race_of_the_season', inplace=True)
    return driver_standings_year_df


def preprocess_driver_standings_data_for_table_for_year(year, driver_standings_df, races_df, drivers_df):
    championship_table_df = driver_standings_df[['raceId', 'driverId', 'points', 'position', 'wins']]
    championship_table_df = pd.merge(championship_table_df, races_df[['raceId', 'year', 'name', 'round']], on='raceId')
    championship_table_df = pd.merge(championship_table_df, drivers_df[['driverId', 'code', 'forename', 'surname']],
                                     on='driverId')
    championship_table_df['full_name'] = championship_table_df['forename'] + ' ' + championship_table_df['surname']
    championship_table_df = championship_table_df.drop(['forename', 'surname'], axis=1)
    championship_table_df = championship_table_df.drop(['raceId'], axis=1)

    # Get results for selected year
    championship_table_year_df = championship_table_df[championship_table_df['year'] == year]
    championship_table_year_df = championship_table_year_df.sort_values(by=['round'], ascending=False)
    championship_table_year_df = championship_table_year_df.groupby(['driverId']).head(1)
    championship_table_year_df = championship_table_year_df.drop(['name', 'year', 'round', 'driverId'], axis=1)
    championship_table_year_df.sort_values(by=['position'], inplace=True)
    columns_reordered = ['position', 'code', 'full_name', 'wins', 'points']
    championship_table_year_df = championship_table_year_df[columns_reordered]
    return championship_table_year_df
