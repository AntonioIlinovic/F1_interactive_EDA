import pandas as pd

def get_driver_standings_data_for_year(year, drivers_df, driver_standings_df, races_df):
    """

    :return:
    """
    driver_standings_year_df = pd.merge(driver_standings_df, races_df, on='raceId')
    driver_standings_year_df = driver_standings_year_df[driver_standings_year_df['year'] == year]
    driver_standings_year_df = pd.merge(driver_standings_year_df, drivers_df, on='driverId')
    driver_standings_year_df = driver_standings_year_df[['forename', 'surname', 'code', 'number', 'name', 'points', 'round']]
    driver_standings_year_df['full_name'] = driver_standings_year_df['forename'] + ' ' + driver_standings_year_df['surname']
    driver_standings_year_df.drop(['forename', 'surname'], axis=1, inplace=True)
    driver_standings_year_df.rename(columns={'name': 'circuit_name', 'code': 'driver_code', 'number': 'driver_number', 'round': 'race_of_the_season'}, inplace=True)
    driver_standings_year_df.sort_values(by='race_of_the_season', inplace=True)
    return driver_standings_year_df
