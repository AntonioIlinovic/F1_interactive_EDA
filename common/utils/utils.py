from dash import ctx
from enum import Enum


def get_trigger() -> str:
    return ctx.triggered[0]["prop_id"]


def DatasetName(Enum):
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
