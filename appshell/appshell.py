import dash_mantine_components as dmc
from dash_iconify import DashIconify

from dash import Output, Input, clientside_callback, html, dcc, page_container, State

from appshell.navbar import get_navbar_content


def create_home_link(label: str) -> dmc.Anchor:
    return dmc.Anchor(
        label,
        size="xl",
        href="/",
        underline=False,
    )


def create_header_link(icon: str, href: str, size: int = 22, color: str = "lime") -> dmc.Anchor:
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )


def create_header() -> dmc.Header:
    return dmc.Header(
        height=50,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="center",
                style={"heigth": 50},
                children=[
                    dmc.Grid(
                        children=[
                            dmc.Col(
                                [
                                    dmc.MediaQuery(
                                        create_home_link("F1 Interactive EDA"),
                                        smallerThan="lg",
                                        styles={"display": "none"},
                                    )
                                ],
                                span="content",
                                pt=12,
                            ),
                            dmc.Col(
                                span="auto",
                                children=dmc.Group(
                                    position="right",
                                    spacing="xl",
                                    children=[
                                        create_header_link(
                                            "radix-icons:github-logo",
                                            "https://github.com/AntonioIlinovic/F1_interactive_EDA",
                                        ),
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:blending-mode", width=22
                                            ),
                                            variant="outline",
                                            radius=30,
                                            size=36,
                                            color="lime",
                                            id="color-scheme-toggle",
                                        ),
                                        dmc.MediaQuery(
                                            dmc.ActionIcon(
                                                DashIconify(
                                                    icon="radix-icons:hamburger-menu",
                                                    width=18,
                                                ),
                                                id="drawer-hamburger-button",
                                                variant="outline",
                                                size=36,
                                            ),
                                            largerThan="lg",
                                            styles={"display": "none"},
                                        ),
                                    ]
                                )
                            )
                        ],
                        style={"margin": "auto 0 auto 0"}
                    )
                ]
            )
        ]
    )


def get_icon(icon):
    return DashIconify(icon=icon, height=16)


def create_side_navbar() -> dmc.Navbar:
    return dmc.Navbar(
        fixed=True,
        id="navbar",
        position={"top": 70},
        width={"base": 300},
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                children=[
                    get_navbar_content()
                ],
            )
        ],
    )


def create_navbar_drawer():
    return dmc.Drawer(
        id="navbar-drawer",
        overlayOpacity=0.55,
        overlayBlur=3,
        zIndex=9,
        size=300,
        children=[
            dmc.ScrollArea(
                offsetScrollbars=True,
                type="scroll",
                style={"height": "100%"},
                pt=20,
                children=get_navbar_content(),
            )
        ],
    )


def create_appshell():
    return dmc.MantineProvider(
        dmc.MantineProvider(
            theme={
                "fontFamily": "'Inter', sans-serif",
                "primaryColor": "lime",
                "components": {
                    "Button": {"styles": {"root": {"fontWeight": 400}}},
                },
            },
            inherit=True,
            children=[
                dcc.Store(id="theme-store", storage_type="local"),
                dcc.Location(id="url"),
                dmc.NotificationsProvider(
                    [
                        create_header(),
                        create_side_navbar(),
                        create_navbar_drawer(),
                        html.Div(
                            dmc.Container(size="xl", pt=90, children=page_container),
                            id="wrapper",
                        ),
                    ]
                ),
            ],
        ),
        theme={"colorScheme": "light"},
        id="plotly-dash-multipage-app-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )


clientside_callback(
    """ function(data) { return data } """,
    Output("plotly-dash-multipage-app-provider", "theme"),
    Input("theme-store", "data"),
)

clientside_callback(
    """function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "light" }
        }
    }""",
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
)

clientside_callback(
    """function(n_clicks) { return true }""",
    Output("navbar-drawer", "opened"),
    Input("drawer-hamburger-button", "n_clicks"),
    prevent_initial_call=True,
)
