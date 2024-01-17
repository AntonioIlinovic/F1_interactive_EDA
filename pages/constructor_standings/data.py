from common.utils.utils import load_dataset, DatasetName
from .preprocessing import preprocess_constructor_standings_data_for_graph_for_year, preprocess_constructor_standings_data_for_table_for_year


print('Loading constructor standings data...')
# Load necessary data once
constructors_df = load_dataset(DatasetName.CONSTRUCTORS)
constructor_standings_df = load_dataset(DatasetName.CONSTRUCTOR_STANDINGS)
races_df = load_dataset(DatasetName.RACES)


def get_constructor_standings_data_for_graph(year):
    return preprocess_constructor_standings_data_for_graph_for_year(year, constructors_df, constructor_standings_df, races_df)


def get_constructor_standings_data_for_table(year):
    return preprocess_constructor_standings_data_for_table_for_year(year, constructors_df, constructor_standings_df, races_df)
