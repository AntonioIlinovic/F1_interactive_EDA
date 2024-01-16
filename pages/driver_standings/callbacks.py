from dash import callback, Output, Input
import plotly.express as px
from pages.driver_standings.data import get_driver_standings_data


@callback(
    Output('driver-standings-graph', 'figure'),
    Input('driver-standings-year-slider', 'value')
)
def update_driver_standings_graph(year):
    """
    Function will return a figure for driver standings for a given year
    :param year:
    :return:
    """
    data_for_year = get_driver_standings_data(year)

    fig = px.line(data_for_year,
                  x='race_of_the_season',
                  y='points',
                  color='full_name',
                  title=f'Driver Standings {year}',
                  labels={'full_name': 'Full Name'},
                  height=700)
    fig.update_xaxes(title='Circuit Name',
                     tickvals=data_for_year['race_of_the_season'],
                     ticktext=data_for_year['circuit_name'],
                     tickangle=45)
    fig.update_yaxes(title='Points')
    return fig
