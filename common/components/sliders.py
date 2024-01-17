from dash import dcc


def create_year_slider(html_id='year-slider', min=1950, max=2023, value=2023, marks=None, step=1):
    if marks is None:
        marks = {str(year): str(year) for year in [i for i in range(1950, 2023, 5)]}
    return dcc.Slider(
        id=html_id,
        className='year-slider',
        min=min,
        max=max,
        value=value,
        marks=marks,
        step=step
    )
