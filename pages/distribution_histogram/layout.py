from dash import html, dcc
from common.utils.utils import DatasetName


def distribution_histogram():
    return dcc.Graph(id='distribution-histogram')


def distribution_dataset_selector():
    return html.Div([
        dcc.Dropdown(value=DatasetName.CIRCUITS.value,  # default value
                     id='distribution-histogram-dataset-name-dropdown',
                     options=[{'label': dataset_name.value, 'value': dataset_name.value} for dataset_name in
                              DatasetName]
                     ),
        html.Div(id='distribution-histogram-dataset-name-output')
    ])


def distribution_column_selector():
    return html.Div([
        dcc.Dropdown(
            id='distribution-histogram-column-name-dropdown'),
        html.Div(id='distribution-histogram-column-name-output')
    ])


def distribution_histogram_layout():
    return html.Div([
        html.H1('Distribution Histogram'),
        distribution_dataset_selector(),
        distribution_column_selector(),
        distribution_histogram()
    ])
