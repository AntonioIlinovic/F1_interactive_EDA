from dash import html, dcc
import plotly.graph_objects as go

from common.components.sliders import create_year_slider


def circuits_map_projection():
    return dcc.Graph(
        id='circuits-map'
    )


def circuits_map_layout():
    return html.Div([
        create_year_slider(html_id='circuits-map-year-slider'),
        html.H2('Circuits Map', id='circuits-map-title'),
        circuits_map_projection()
    ])
