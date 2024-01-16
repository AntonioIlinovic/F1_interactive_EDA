import dash
from pages.home.layout import home_layout
from pages.circuits_map.layout import circuits_map_layout
from pages.distribution_histogram.layout import distribution_histogram_layout
from pages.driver_standings.layout import driver_standings_layout


class Controller:
    def configure(self):
        dash.register_page(
            "home",
            path='/',
            title='Home',
            name='Home',
            layout=home_layout
        )

        dash.register_page(
            "circuits-map",
            path='/circuits-map',
            title='Circuits Map',
            name='Circuits Map',
            layout=circuits_map_layout
        )

        dash.register_page(
            "distribution-histogram",
            path='/distribution-histogram',
            title='Distribution Histogram',
            name='Distribution Histogram',
            layout=distribution_histogram_layout

        )

        dash.register_page(
            "driver-standings",
            path='/driver-standings',
            title='Driver Standings',
            name='Driver Standings',
            layout=driver_standings_layout
        )
