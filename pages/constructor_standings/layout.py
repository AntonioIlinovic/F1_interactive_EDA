from dash import html, dcc, dash_table

from common.components.sliders import create_year_slider


def constructor_standings_graph():
    return dcc.Graph(
        id='constructor-standings-graph'
    )


def constructor_standings_table():
    return html.Div(
        className='table-container',
        children=[
            dash_table.DataTable(
                id='constructor-standings-table',
                columns=[
                    {'name': 'Position', 'id': 'position'},
                    {'name': 'Constructor Name', 'id': 'constructor_name'},
                    {'name': 'Constructor Nationality', 'id': 'nationality'},
                    {'name': 'Wins', 'id': 'wins'},
                    {'name': 'Points', 'id': 'points'},
                ],
                style_cell_conditional=[  # Column widths
                    {'if': {'column_id': 'position'}, 'width': '10%'},
                    {'if': {'column_id': 'constructor_name'}, 'width': '30%'},
                    {'if': {'column_id': 'nationality'}, 'width': '30%'},
                    {'if': {'column_id': 'wins'}, 'width': '15%'},
                    {'if': {'column_id': 'points'}, 'width': '15%'},
                ],
                sort_action='custom',
                sort_mode='single',
            )
        ])


def constructor_standings_season_progress_layout():
    return html.Div([
        html.H2('Constructor Standings', id='constructor-standings-graph-title'),
        create_year_slider(html_id='constructor-standings-graph-year-slider'),
        constructor_standings_graph()
    ])


def constructor_standings_season_finale_layout():
    return html.Div([
        html.H2('Constructor Standings', id='constructor-standings-table-title'),
        create_year_slider(html_id='constructor-standings-table-year-slider'),
        constructor_standings_table()
    ])
