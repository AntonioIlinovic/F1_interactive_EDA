from dash import html, dcc


def constructor_standings_year_slider():
    # TODO try to reuse circuits_map_year_slider
    return dcc.Slider(
        id='constructor-standings-year-slider',
        min=1950,  # TODO change to min(years)
        max=2023,  # TODO change to max(years)
        value=2023,  # TODO change to max(years)
        marks={str(year): str(year) for year in [i for i in range(1950, 2023, 5)]},  # TODO change marks dynamically
        step=1
    )


def constructor_standings_graph():
    return dcc.Graph(id='constructor-standings-graph')


def constructor_standings_layout():
    return html.Div([
        constructor_standings_year_slider(),
        constructor_standings_graph()
    ])
