from dash import html


def home_layout():
    return html.Div(children=[
        html.H1(children="F1 interactive EDA"),
        html.Div(children='''
            This is the interactive EDA for F1 data.
            Choose visualizations from the sidebar.
        '''),
    ])