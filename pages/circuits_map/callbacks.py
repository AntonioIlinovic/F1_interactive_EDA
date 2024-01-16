from dash import callback, Output, Input
import plotly.graph_objects as go
from .data import get_data_for_map


@callback(
    Output('circuits-map', 'figure'),
    Input('year-slider', 'value')
)
def update_circuits_map(selected_year):
    data_for_map_year = get_data_for_map(selected_year)

    trace = go.Scattergeo(
        text=data_for_map_year.apply(lambda x: f"{x['country']}<br>{x['circuit_name']}", axis=1),
        lat=data_for_map_year['lat'],
        lon=data_for_map_year['lng'],
        mode='markers',
        marker=dict(size=5, opacity=0.8),
        name=str(selected_year)
    )

    layout = go.Layout(
        geo=dict(projection_type='natural earth'),
        margin=dict(l=0, r=0, t=40, b=0)
    )

    fig = go.Figure(data=[trace], layout=layout)
    return fig


@callback(
    Output('circuits-map-title', 'children'),
    Input('year-slider', 'value')
)
def update_circuits_map_title(selected_year):
    return f'Circuits Map {selected_year}'
