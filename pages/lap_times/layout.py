from dash import html, dcc
from common.components.sliders import create_year_slider
from common.components.dropdowns import create_dropdown


def lap_times_graph():
    return dcc.Graph(
        id='lap-times-graph'
    )


def lap_times_layout():
    return html.Div([
        html.H2('Lap Times', id='lap-times-graph-title'),
        create_year_slider(html_id='lap-times-graph-year-slider'),
        create_dropdown(html_id='lap-times-graph-dropdown', value='Bahrain Grand Prix'),
        lap_times_graph()
    ])
