from dash import callback, Output, Input
import plotly.express as px
from pages.constructor_standings.data import get_constructor_standings_data


@callback(
    Output('constructor-standings-graph', 'figure'),
    Input('constructor-standings-year-slider', 'value')
)
def update_constructor_standings_graph(year):
    """
    Function will return a figure for constructor standings for a given year
    :param year:
    :return:
    """
    data_for_year = get_constructor_standings_data(year)

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
