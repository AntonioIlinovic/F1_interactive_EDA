from dash import html, dcc, dash_table

from common.components.sliders import create_year_slider


def driver_standings_graph():
    return dcc.Graph(
        id='driver-standings-graph'
    )


def driver_standings_table():
    return dash_table.DataTable(
        id='driver-standings-table',

        columns=[
            {'name': 'Position', 'id': 'position'},
            {'name': 'Driver Code', 'id': 'code'},
            {'name': 'Full Name', 'id': 'full_name'},
            {'name': 'Wins', 'id': 'wins'},
            {'name': 'Points', 'id': 'points'},
        ],
        style_cell_conditional=[  # Column widths
            {'if': {'column_id': 'position'},
             'width': '10%'},
            {'if': {'column_id': 'code'},
             'width': '10%'},
            {'if': {'column_id': 'full_name'},
             'width': '50%'},
            {'if': {'column_id': 'code'},
             'width': '15%'},
            {'if': {'column_id': 'code'},
             'width': '15%'},
        ],

        data=[],  # Initial empty data

        sort_action='custom',
        sort_mode='single',
        sort_by=[],
    )


def driver_standings_season_progress_layout():
    return html.Div([
        create_year_slider(),
        driver_standings_graph()
    ])


def driver_standings_season_finale_layout():
    return html.Div([
        create_year_slider(),
        html.H2('Driver Standings', id='driver-standings-table-title'),
        driver_standings_table()
    ])
