from dash import html, dcc
from common.utils.utils import DatasetName


def distribution_histogram():
    return dcc.Graph(
        id='distribution-histogram'
    )


def distribution_dataset_selector():
    return html.Div([
        dcc.Dropdown(
            value=DatasetName.DRIVERS.value,  # default value
            id='distribution-histogram-dataset-dropdown',
            options=[{'label': dataset_name.value, 'value': dataset_name.value} for dataset_name in DatasetName],
            placeholder='Select a Dataset',
        ),
    ])


def distribution_column_selector():
    return html.Div([
        dcc.Dropdown(
            value='dob',  # default value, date of birth
            id='distribution-histogram-column-dropdown',
            placeholder='Select a Column',
        ),
    ])


def distribution_histogram_layout():
    return html.Div([
        distribution_dataset_selector(),
        distribution_column_selector(),
        distribution_histogram()
    ])
