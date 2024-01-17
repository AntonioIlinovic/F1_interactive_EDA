from dash import callback, Output, Input
import plotly.express as px
from pages.driver_standings.data import get_driver_standings_for_graph, get_driver_standings_for_table


@callback(
    Output('driver-standings-graph', 'figure'),
    Input('driver-standings-graph-year-slider', 'value')
)
def update_driver_standings_graph(year):
    data_for_year = get_driver_standings_for_graph(year)
    fig = px.line(data_for_year,
                  x='race_of_the_season',
                  y='points',
                  color='full_name',
                  labels={'full_name': 'Full Name'},
                  height=700)
    fig.update_xaxes(title='Circuit Name',
                     tickvals=data_for_year['race_of_the_season'],
                     ticktext=data_for_year['circuit_name'],
                     tickangle=45)
    fig.update_yaxes(title='Points')
    return fig


@callback(
    Output('driver-standings-graph-title', 'children'),
    Input('driver-standings-graph-year-slider', 'value')
)
def update_driver_standings_graph_title(year):
    return f'Driver Standings {year}'


@callback(
    Output('driver-standings-table', 'data'),
    [Input('driver-standings-table-year-slider', 'value'),
     Input('driver-standings-table', 'sort_by')]
)
def update_driver_standings_table(year, sort_by):
    """
    Function will return a table for driver standings for a given year
    :param sort_by: DashTable sends a list of sort_by objects. We only use single sorting, so we take the first one.
        One example of sort_by object: [{'column_id': 'wins', 'direction': 'asc'}]
    :param year:
    :return:
    """
    data_for_year = get_driver_standings_for_table(year)

    if sort_by:
        data_for_year.sort_values(
            by=sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=True)

    return data_for_year.to_dict('records')


@callback(
    Output('driver-standings-table-title', 'children'),
    Input('driver-standings-table-year-slider', 'value')
)
def update_driver_standings_table_title(year):
    return f'Driver Standings {year}'
