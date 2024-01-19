from dash import callback, Output, Input
from pages.lap_times.data import get_lap_times_data_for_race, get_race_names_for_season
import plotly.express as px


@callback(
    Output('lap-times-graph', 'figure'),
    [Input('lap-times-graph-year-slider', 'value'),
     Input('lap-times-graph-dropdown', 'value')]
)
def update_lap_times_graph(year, race_name):
    lap_times_for_race = get_lap_times_data_for_race(year, race_name)
    fig = px.line(
        lap_times_for_race,
        x='lap',
        y='milliseconds',
        color='driver_full_name',
        labels={'lap': 'Lap', 'milliseconds': 'Lap Time (ms)', 'driver_full_name': 'Full Name'},
        height=700)
    return fig


@callback(
    Output('lap-times-graph-title', 'children'),
    [Input('lap-times-graph-year-slider', 'value'),
     Input('lap-times-graph-dropdown', 'value')]
)
def update_lap_times_graph_title(year, race_name):
    return f'Lap Times for {race_name} {year}'


@callback(
    Output('lap-times-graph-dropdown', 'options'),
    Input('lap-times-graph-year-slider', 'value')
)
def update_lap_times_dropdown_options(year):
    race_names_for_season = get_race_names_for_season(year)
    return race_names_for_season
