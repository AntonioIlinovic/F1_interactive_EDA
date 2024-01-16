from common.models.circuits import get_circuits_df
from common.models.constructor_results import get_constructor_results_df
from common.models.constructor_standings import get_constructor_standings_df
from common.models.constructors import get_constructors_df
from common.models.driver_standings import get_driver_standings_df
from common.models.drivers import get_drivers_df
from common.models.lap_times import get_lap_times_df
from common.models.pit_stops import get_pit_stops_df
from common.models.qualifying import get_qualifying_df
from common.models.races import get_races_df
from common.models.results import get_results_df
from common.models.seasons import get_seasons_df
from common.models.sprint_results import get_sprint_results_df
from common.models.status import get_status_df
from common.utils.utils import DatasetName
import pandas as pd
import plotly.express as px


def get_histogram_distribution(dataset: DatasetName, column_name: str):
    """
    This function will return a histogram distribution for a given dataset and column name.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :param column_name: of a column in the dataset
    :return:
    """

    # TODO refactor code

    df = pd.read_csv(f"./F1_dataset/{dataset}.csv")
    fig = px.histogram(df, x=column_name, marginal='box', hover_data=df.columns)
    return fig


def get_dataset_columns(dataset: DatasetName):
    """
    This function will return a list of columns for a given dataset.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :return:
    """

    # TODO refactor code

    df = pd.read_csv(f"./F1_dataset/{dataset}.csv")
    return df.columns
