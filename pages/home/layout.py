from dash import html


def home_layout():
    return html.Div(children=[
        html.H1(children="F1 Interactive EDA"),
        html.Div(children='''
            Explore interactive F1 data visualizations using the options in the sidebar.
        '''),
    ])
