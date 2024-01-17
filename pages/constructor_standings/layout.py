from dash import html, dcc, dash_table

from common.components.sliders import create_year_slider


def constructor_standings_graph():
    return dcc.Graph(
        id='constructor-standings-graph'
    )


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
        create_year_slider(html_id='constructor-standings-season-progress-year-slider'),
        constructor_standings_graph()
    ])


def constructor_standings_season_finale_layout():
    return html.Div([
        create_year_slider(html_id='constructor-standings-season-finale-year-slider'),
        html.H2('Constructor Standings', id='constructor-standings-table-title'),
        constructor_standings_table()
    ])
