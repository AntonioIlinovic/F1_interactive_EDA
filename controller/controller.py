import dash
from pages.home.layout import home_layout
from pages.circuits_map.layout import circuits_map_layout
from pages.distribution_histogram.layout import distribution_histogram_layout
from pages.driver_standings.layout import driver_standings_season_progress_layout, driver_standings_season_finale_layout
from pages.constructor_standings.layout import constructor_standings_season_progress_layout, constructor_standings_season_finale_layout


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
            "driver-standings/season-progress",
            path='/driver-standings/season-progress',
            title='Driver Standings - Season Progress',
            name='Driver Standings - Season Progress',
            layout=driver_standings_season_progress_layout
        )
        dash.register_page(
            "driver-standings/season-finale",
            path='/driver-standings/season-finale',
            title='Driver Standings - Season Finale',
            name='Driver Standings - Season Finale',
            layout=driver_standings_season_finale_layout
        )

        dash.register_page(
            "constructor-standings/season-progress",
            path='/constructor-standings/season-progress',
            title='Constructor Standings - Season Progress',
            name='Constructor Standings - Season Progress',
            layout=constructor_standings_season_progress_layout
        )
        dash.register_page(
            "constructor-standings/season-finale",
            path='/constructor-standings/season-finale',
            title='Constructor Standings - Season Finale',
            name='Constructor Standings - Season Finale',
            layout=constructor_standings_season_finale_layout
        )
