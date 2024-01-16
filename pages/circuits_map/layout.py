from dash import html, dcc
import plotly.graph_objects as go


def circuits_map_year_slider():
    return dcc.Slider(
        id='year-slider',
        className='circuits-map-year-slider',
        min=1950,  # TODO change to min(years)
        max=2023,  # TODO change to max(years)
        value=2023,  # TODO change to max(years)
        marks={str(year): str(year) for year in [i for i in range(1950, 2023, 5)]},  # TODO change marks dynamically
        step=1
    )


def circuits_map_projection():
    return dcc.Graph(id='circuits-map')


def circuits_map_layout():
    return html.Div([
        circuits_map_year_slider(),
        html.H2('Circuits Map', id='circuits-map-title'),
        circuits_map_projection()
    ])
