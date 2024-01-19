from dash import html, dcc

from common.components import dropdowns
from common.utils.utils import DatasetName


def distribution_histogram():
    return dcc.Graph(
        id='distribution-histogram',
    )


def distribution_dataset_selector():
    return dropdowns.create_dropdown(
        value=DatasetName.DRIVERS.value,  # default value
        html_id='distribution-histogram-dataset-dropdown',
        options=[{'label': dataset_name.value, 'value': dataset_name.value} for dataset_name in DatasetName],
        placeholder='Select a Dataset'
    )


def distribution_column_selector():
    return dropdowns.create_dropdown(
        value='dob',  # default value, date of birth
        html_id='distribution-histogram-column-dropdown',
        placeholder='Select a Column'
    )


def distribution_histogram_layout():
    return html.Div([
        html.H2('Distribution Histogram', id='distribution-histogram-title'),
        distribution_dataset_selector(),
        distribution_column_selector(),
        distribution_histogram()
    ])
