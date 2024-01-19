from common.utils.utils import DatasetName, load_dataset
from .preprocessing import preprocess_driver_standings_data_for_graph_for_year, preprocess_driver_standings_data_for_table_for_year


print('Loading data for Driver Standings page...')
# Load necessary data once
driver_standings_df = load_dataset(DatasetName.DRIVER_STANDINGS)
races_df = load_dataset(DatasetName.RACES)
drivers_df = load_dataset(DatasetName.DRIVERS)


def get_driver_standings_for_graph(year):
    return preprocess_driver_standings_data_for_graph_for_year(year, drivers_df, driver_standings_df, races_df)


def get_driver_standings_for_table(year):
    return preprocess_driver_standings_data_for_table_for_year(year, driver_standings_df, races_df, drivers_df)
