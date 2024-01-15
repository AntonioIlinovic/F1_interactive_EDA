import dash
from dash import Dash, Output, Input
import plotly.graph_objects as go
import pandas as pd


@dash.callback(
    Output('test-div', 'children'),
    Input('year-slider', 'value')
)
def update_test_div(selected_year):
    return f"Selected year: {selected_year}"


@dash.callback(
    Output('circuits-map', 'figure'),
    Input('year-slider', 'value')
)
def update_map(selected_year):
    races_df = pd.read_csv('./F1_dataset/races.csv')
    circuits_df = pd.read_csv('./F1_dataset/circuits.csv')

    races_circuit_df = pd.merge(races_df, circuits_df, on='circuitId')
    years = sorted(set(races_circuit_df['year']))


    yearly_data = races_circuit_df[races_circuit_df['year'] == selected_year]

    trace = go.Scattergeo(
        text=yearly_data.apply(lambda x: f"{x['country']}{x['name_x']}", axis=1),
        lat=yearly_data['lat'],
        lon=yearly_data['lng'],
        mode='markers',
        marker=dict(size=5, opacity=0.8),
        name=str(selected_year)
    )

    layout = go.Layout(
        title=f'F1 Circuits {selected_year}',
        geo=dict(projection_type='natural earth'),
        margin=dict(l=0, r=0, t=40, b=0)
    )

    fig = go.Figure(data=[trace], layout=layout)
    return fig