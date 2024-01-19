import pandas as pd
from common.utils.utils import load_dataset, DatasetName


print('Loading data for Lap Times page...')
# Load necessary data once
lap_times_df = load_dataset(DatasetName.LAP_TIMES)
races_df = load_dataset(DatasetName.RACES)
drivers_df = load_dataset(DatasetName.DRIVERS)


def get_lap_times_data_for_race(year, race_name):
    # Filter data for selected season
    races_for_season = races_df[races_df['year'] == year]
    # Filter data for selected race
    selected_race = races_for_season[races_for_season['name'] == race_name]
    assert len(selected_race) == 1, f'There are multiple races named {race_name} in year {year}'
    selected_race_id = selected_race['raceId'].values[0]

    # Get lap times data for selected race
    lap_times_for_race = lap_times_df[lap_times_df['raceId'] == selected_race_id]
    # Merge driver info
    lap_times_for_race = pd.merge(lap_times_for_race, drivers_df, on='driverId')
    # Select only necessary data
    lap_times_for_race = lap_times_for_race[['lap', 'time', 'milliseconds', 'number', 'code', 'forename', 'surname']]
    # Combine driver name and surname
    lap_times_for_race['driver_full_name'] = lap_times_for_race['forename'] + ' ' + lap_times_for_race['surname']
    lap_times_for_race.drop(['forename', 'surname'], axis=1, inplace=True)
    # Rename columns for clarity
    lap_times_for_race.rename(columns={'number': 'driver_number', 'code': 'driver_code'}, inplace=True)

    return lap_times_for_race


def get_race_names_for_season(year):
    # Filter data for selected season
    races_for_season = races_df[races_df['year'] == year]
    # Return races in selected season
    race_names_for_season = races_for_season.name
    return race_names_for_season
