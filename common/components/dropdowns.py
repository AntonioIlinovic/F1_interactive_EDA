from dash import dcc


def create_dropdown(html_id='dropdown', options=None, value=None):
    if options is None:
        options = []
    return dcc.Dropdown(
        id=html_id,
        className='dropdown',
        options=options,
        value=value
    )
