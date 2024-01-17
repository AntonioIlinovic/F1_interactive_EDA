from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify


def get_navbar_content():
    # To add a new subpage, add a new entry to children list
    return html.Div(
        dmc.Stack(
            spacing="sm",
            mt=20,
            children=[
                create_main_nav_link(
                    icon="bi:house",
                    label="Home",
                    href="/",
                ),
                create_main_nav_link(
                    # icon of a map
                    icon="bi:map",
                    label="Circuits Map",
                    href="/circuits-map",
                ),
                create_main_nav_link(
                    # icon of a histogram
                    icon="bi:bar-chart",
                    label="Distribution Histogram",
                    href="/distribution-histogram",
                ),
                create_nav_link_with_sublinks(
                    icon="bi:person",
                    label="Driver Standings",
                    href=None,  # No direct href, as this is a parent link
                    sublinks=[
                        ("Season Progress", "/driver-standings/season-progress"),
                        ("Season Finale", "/driver-standings/season-finale")
                    ]
                ),
                create_nav_link_with_sublinks(
                    icon="bi:car-front",
                    label="Constructor Standings",
                    href=None,  # No direct href, as this is a parent link
                    sublinks=[
                        ("Season Progress", "/constructor-standings/season-progress"),
                        ("Season Finale", "/constructor-standings/season-finale")
                    ]
                ),
            ],
        ),
        style={"padding-left": 16}
    )


def create_main_nav_link(icon, label, href):
    return dmc.Anchor(
        dmc.Group(
            [
                DashIconify(
                    icon=icon, width=23
                ),
                dmc.Text(label, size="sm"),
            ]
        ),
        href=href,
        variant="text",
    )


def create_nav_link_with_sublinks(icon, label, href, sublinks):
    return dmc.NavLink(
        label=label,
        icon=DashIconify(icon=icon, width=23),
        href=href,
        opened=True,
        children=[
            dmc.NavLink(label=sublink_label, href=sublink_href)
            for sublink_label, sublink_href in sublinks
        ],
    )
