from dash import callback, Output, Input
import plotly.express as px
from pages.driver_standings.data import get_driver_standings_data


@callback(
    Output('driver-standings-graph', 'figure'),
    Input('driver-standings-year-slider', 'value')
)
def update_driver_standings_graph(selected_year):
    """
    Function will return a figure for driver standings for a given year
    :param selected_year:
    :return:
    """
    data_for_year = get_driver_standings_data(selected_year)
    fig = px.line(data_for_year,
                  x='race_of_the_season',
                  y='points',
                  color='full_name',
                  title=f'Driver standings {selected_year}',
                  labels={'full_name': 'Full name'},
                  height=700)
    fig.update_xaxes(title='Circuit name',
                     tickvals=data_for_year['race_of_the_season'],
                     ticktext=data_for_year['circuit_name'],
                     tickangle=45)
    fig.update_yaxes(title='Points')
    return fig
