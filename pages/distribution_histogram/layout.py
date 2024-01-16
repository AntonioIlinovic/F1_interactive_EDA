from dash import html, dcc


def distribution_histogram():
    return dcc.Graph(id='distribution-histogram')


def distribution_dataset_selector():
    return html.Div([
        dcc.Dropdown(['circuits', 'constructor_results', 'constructor_standings', 'constructors'],
                     'circuits',
                     id='distribution-histogram-dataset-name-dropdown'),
        html.Div(id='distribution-histogram-dataset-name-output')
    ])


def distribution_column_selector():
    return html.Div([
        dcc.Dropdown(['circuit_id', 'circuit_ref', 'circuit_name', 'country', 'location', 'lat', 'lng', 'alt', 'url'],
                     'lat',
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
