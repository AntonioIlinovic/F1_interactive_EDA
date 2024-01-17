from dash import callback, Output, Input
import plotly.graph_objects as go
from .data import get_data_for_map
from .layout import circuits_map_figure_layout_template, circuits_map_figure_data_trace_template


@callback(
    Output('circuits-map', 'figure'),
    Input('circuits-map-year-slider', 'value')
)
def update_circuits_map(year):
    data_for_map_year = get_data_for_map(year)

    # Get the trace template and update it with the data for the selected year
    trace = circuits_map_figure_data_trace_template()
    trace.text = data_for_map_year.apply(lambda x: f"{x['country']}<br>{x['circuit_name']}", axis=1)
    trace.lat = data_for_map_year['lat']
    trace.lon = data_for_map_year['lng']
    trace.name = str(year)

    # Create the figure. Use the layout function to get the layout template
    fig = go.Figure(data=[trace], layout=circuits_map_figure_layout_template())
    return fig


@callback(
    Output('circuits-map-title', 'children'),
    Input('circuits-map-year-slider', 'value')
)
def update_circuits_map_title(year):
    return f'Circuits Map {year}'
