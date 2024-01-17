import pandas as pd
from dash import ctx
from enum import Enum


def get_trigger() -> str:
    return ctx.triggered[0]["prop_id"]


class DatasetName(Enum):
    CIRCUITS = "circuits"
    CONSTRUCTOR_RESULTS = "constructor_results"
    CONSTRUCTOR_STANDINGS = "constructor_standings"
    CONSTRUCTORS = "constructors"
    DRIVER_STANDINGS = "driver_standings"
    DRIVERS = "drivers"
    LAP_TIMES = "lap_times"
    PIT_STOPS = "pit_stops"
    QUALIFYING = "qualifying"
    RACES = "races"
    RESULTS = "results"
    SEASONS = "seasons"
    SPRINT_RESULTS = "sprint_results"
    STATUS = "status"


def load_dataset(dataset_name: [DatasetName, str]):
    """
    This function will load a dataset from F1_dataset folder. Both DatasetName and str are accepted as input because
    when using Dash callback, the value of a dropdown is a str.
    :param dataset_name:
    :return:
    """
    if isinstance(dataset_name, DatasetName):
        dataset_name = dataset_name.value
    df = pd.read_csv(f"./F1_dataset/{dataset_name}.csv")
    return df


def get_dataset_columns(dataset_name: DatasetName):
    """
    This function will return a list of columns for a given dataset.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :return:
    """
    df = load_dataset(dataset_name)
    return df.columns
