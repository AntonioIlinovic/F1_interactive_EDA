from dash import html, dcc, dash_table
import plotly.graph_objects as go
from common.components.sliders import create_year_slider


def driver_standings_graph():
    return dcc.Graph(
        id='driver-standings-graph'
    )


def driver_standings_table():
    return html.Div(
        className='table-container',
        children=[
            dash_table.DataTable(
                id='driver-standings-table',
                columns=[
                    {'name': 'Position', 'id': 'position'},
                    {'name': 'Driver Code', 'id': 'code'},
                    {'name': 'Full Name', 'id': 'full_name'},
                    {'name': 'Wins', 'id': 'wins'},
                    {'name': 'Points', 'id': 'points'},
                ],
                style_cell_conditional=[  # Column widths
                    {'if': {'column_id': 'position'}, 'width': '15%'},
                    {'if': {'column_id': 'code'}, 'width': '15%'},
                    {'if': {'column_id': 'full_name'}, 'width': '40%'},
                    {'if': {'column_id': 'wins'}, 'width': '15%'},
                    {'if': {'column_id': 'points'}, 'width': '15%'},
                ],
                sort_action='custom',
                sort_mode='single',
            )
        ])


def driver_standings_season_progress_layout():
    return html.Div([
        html.H2('Driver Standings', id='driver-standings-graph-title'),
        create_year_slider(html_id='driver-standings-graph-year-slider'),
        driver_standings_graph()
    ])


def driver_standings_season_finale_layout():
    return html.Div([
        html.H2('Driver Standings', id='driver-standings-table-title'),
        create_year_slider(html_id='driver-standings-table-year-slider'),
        driver_standings_table()
    ])
