from dash import callback, Output, Input
import plotly.express as px
from pages.constructor_standings.data import get_constructor_standings_data_for_graph, get_constructor_standings_for_table


@callback(
    Output('constructor-standings-graph', 'figure'),
    Input('constructor-standings-graph-year-slider', 'value')
)
def update_constructor_standings_graph(year):
    """
    Function will return a figure for constructor standings for a given year
    :param year:
    :return:
    """
    data_for_year = get_constructor_standings_data_for_graph(year)

    fig = px.line(data_for_year,
                  x='round',
                  y='points',
                  color='constructor_name',
                  title=f'Constructor Standings {year}',
                  labels={'constructor_name': 'Constructor Name'},
                  height=700)
    # Update x-axis to use circuit names as ticks
    fig.update_xaxes(title='Circuit Name',
                     tickvals=data_for_year['round'],
                     ticktext=data_for_year['circuit_name'],
                     tickangle=45)
    fig.update_yaxes(title='Points')
    return fig


@callback(
    Output('constructor-standings-table', 'data'),
    [Input('constructor-standings-table-year-slider', 'value'),
     Input('constructor-standings-table', 'sort_by')]
)
def update_constructor_standings_table(year, sort_by):
    """
    Function will return a table for constructor standings for a given year
    :param sort_by: DashTable sends a list of sort_by objects. We only use single sorting, so we take the first one.
        One example of sort_by object: [{'column_id': 'wins', 'direction': 'asc'}]
    :param year:
    :return:
    """
    data_for_year = get_constructor_standings_for_table(year)

    if sort_by:
        data_for_year.sort_values(
            by=sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=True)

    return data_for_year.to_dict('records')


@callback(
    Output('constructor-standings-table-title', 'children'),
    Input('year-slider', 'value')
)
def update_constructor_standings_table_title(year):
    """
    Function will return a table title for constructor standings for a given year
    :param year:
    :return:
    """
    return f'Constructor Standings {year}'
