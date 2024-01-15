from dash import html, dcc
import plotly.graph_objects as go


def circuits_map_layout():
    return html.Div([
        dcc.Slider(
            id='year-slider',
            className='circuits-map-year-slider',
            min=1950,  # TODO change to min(years)
            max=2023,  # TODO change to max(years)
            value=2023,  # TODO change to max(years)
            marks={str(year): str(year) for year in [i for i in range(1950, 2023, 5)]},  # TODO change marks dynamically
            # step=1
        ),
        dcc.Graph(id='circuits-map', figure=
        go.Figure(
            data=go.Scattergeo(
                lon=[],
                lat=[],
                text=[],
                mode='markers',
                marker=dict(
                    size=8,
                    opacity=0.8,
                    reversescale=True,
                    autocolorscale=False,
                    symbol='square',
                    line=dict(
                        width=1,
                        color='rgba(102, 102, 102)'
                    ),
                    colorscale='Blues',
                    cmin=0,
                    color=[],
                    cmax=0,
                    colorbar=dict(
                        title="TODO"
                    )
                )
            ),
            layout=go.Layout(
                title=go.layout.Title(
                    text='TODO'
                ),
                geo=go.layout.Geo(
                    scope='world',
                    projection=go.layout.geo.Projection(
                        type='equirectangular'
                    ),
                    showland=True,
                    landcolor='rgb(217, 217, 217)',
                    subunitwidth=1,
                    countrywidth=1,
                    subunitcolor="rgb(255, 255, 255)",
                    countrycolor="rgb(255, 255, 255)"
                )
            )
        )
                  )
    ])
