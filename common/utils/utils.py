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


def load_dataset(dataset_name: DatasetName):
    """
    This function will load a dataset by dataset name. Sometimes user can dynamically select a dataset name, and
    it will be necessary to load a dataset dynamically.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :return:
    """
    df = pd.read_csv(f"./F1_dataset/{dataset_name.value}.csv")
    return df


def get_dataset_columns(dataset_name: DatasetName):
    """
    This function will return a list of columns for a given dataset.
    :param dataset_name: dataset name. It will load necessary dataframe using this parameter
    :return:
    """
    df = load_dataset(dataset_name)
    return df.columns
