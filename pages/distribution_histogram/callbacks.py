import dash
from dash import Output, Input

from pages.distribution_histogram.data import get_histogram_distribution


@dash.callback(
    Output('distribution-histogram', 'figure'),
    [Input('distribution-histogram-dataset-name-dropdown', 'value'),
        Input('distribution-histogram-column-name-dropdown', 'value')])
def update_distribution_histogram(dataset_name, column_name):
    print(f"dataset_name={dataset_name}, column_name={column_name}")
    return get_histogram_distribution(dataset_name, column_name)
