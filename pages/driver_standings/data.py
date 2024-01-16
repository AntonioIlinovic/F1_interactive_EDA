import pandas as pd
from common.models.driver_standings import get_driver_standings_df
from common.models.races import get_races_df
from common.models.drivers import get_drivers_df
from .preprocessing import get_driver_standings_data_for_graph_for_year, get_driver_standings_data_for_table_for_year

# Load necessary data once
driver_standings_df = get_driver_standings_df()
races_df = get_races_df()
drivers_df = get_drivers_df()


def get_driver_standings_for_graph(year):
    """
    Function will return a dataframe of driver standings for a given year
    :param year:
    :return:
    """
    driver_standings_data_for_year = get_driver_standings_data_for_graph_for_year(year, drivers_df, driver_standings_df, races_df)
    return driver_standings_data_for_year


def get_driver_standings_for_table(year):
    """

    :param year:
    :return:
    """
    driver_standings_season_finale_for_year = get_driver_standings_data_for_table_for_year(year, driver_standings_df, races_df, drivers_df)
    return driver_standings_season_finale_for_year
