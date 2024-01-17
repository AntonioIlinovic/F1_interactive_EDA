from common.models.races_circuit_joined import join_races_circuits_df
from common.utils.utils import load_dataset, DatasetName
from .preprocessing import preprocess_map_data_for_year


print('Loading circuits map data...')
# Load necessary dataframes once
races_df = load_dataset(DatasetName.RACES)
circuits_df = load_dataset(DatasetName.CIRCUITS)
races_circuit_df = join_races_circuits_df(races_df, circuits_df)


def get_data_for_map(year):
    return preprocess_map_data_for_year(year, races_circuit_df)
