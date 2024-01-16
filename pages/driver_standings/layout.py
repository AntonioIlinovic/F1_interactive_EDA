from dash import html, dcc


def driver_standings_year_slider():
    # TODO try to reuse circuits_map_year_slider
    return dcc.Slider(
        id='driver-standings-year-slider',
        min=1950,  # TODO change to min(years)
        max=2023,  # TODO change to max(years)
        value=2023,  # TODO change to max(years)
        marks={str(year): str(year) for year in [i for i in range(1950, 2023, 5)]},  # TODO change marks dynamically
        step=1
    )


def driver_standings_graph():
    return dcc.Graph(id='driver-standings-graph')


def driver_standings_layout():
    return html.Div([
        driver_standings_year_slider(),
        driver_standings_graph()
    ])
