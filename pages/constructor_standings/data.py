from common.models.constructors import get_constructors_df
from common.models.constructor_standings import get_constructor_standings_df
from common.models.races import get_races_df
from .preprocessing import get_constructor_standings_data_for_year


# Load necessary data once
constructors_df = get_constructors_df()
constructor_standings_df = get_constructor_standings_df()
races_df = get_races_df()


def get_constructor_standings_data(year):
    """

    :return:
    """
    constructor_standings_data_for_year = get_constructor_standings_data_for_year(year, constructors_df, constructor_standings_df, races_df)
    return constructor_standings_data_for_year
