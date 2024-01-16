from dash import html, dcc, dash_table


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


def constructor_standings_table():
    return dash_table.DataTable(
        id='constructor-standings-table',

        columns=[
            {'name': 'Position', 'id': 'position'},
            {'name': 'Constructor Name', 'id': 'constructor_name'},
            {'name': 'Constructor Nationality', 'id': 'nationality'},
            {'name': 'Wins', 'id': 'wins'},
            {'name': 'Points', 'id': 'points'},
        ],
        style_cell_conditional=[  # Column widths
            {'if': {'column_id': 'position'},
             'width': '10%'},
            {'if': {'column_id': 'constructor'},
             'width': '40%'},
            {'if': {'column_id': 'nationality'},
             'width': '30%'},
            {'if': {'column_id': 'wins'},
             'width': '10%'},
            {'if': {'column_id': 'points'},
             'width': '10%'},
        ],

        data=[],  # Initial empty data

        sort_action='custom',
        sort_mode='single',
        sort_by=[],
    )


def constructor_standings_season_progress_layout():
    return html.Div([
        constructor_standings_year_slider(),
        constructor_standings_graph()
    ])


def constructor_standings_season_finale_layout():
    return html.Div([
        constructor_standings_year_slider(),
        html.H2('Constructor Standings', id='constructor-standings-table-title'),
        constructor_standings_table()
    ])
