from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from kivy.uix.boxlayout import BoxLayout

from kivy_garden.mapview import MapView, MapMarker
from kivy.graphics import Color, Line


class NavigationScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation="vertical"
        )

        self.title = MDLabel(
            text="Navigation",
            halign="center",
            size_hint=(1, 0.08)
        )

        self.map = MapView(
            zoom=12,
            lat=22.5726,
            lon=88.3639
        )

        self.marker = MapMarker(
            lat=22.5726,
            lon=88.3639
        )

        self.map.add_marker(self.marker)

        back_btn = MDRaisedButton(
            text="Back",
            size_hint=(1, 0.1),
            on_release=self.go_back
        )

        self.layout.add_widget(self.title)
        self.layout.add_widget(self.map)
        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def show_route(self, place_name, lat, lon):

        self.title.text = f"Route to {place_name}"

        self.map.center_on(lat, lon)

        self.marker.lat = lat
        self.marker.lon = lon

        self.draw_route(lat, lon)

    def draw_route(self, dest_lat, dest_lon):

        # Simulated user location
        user_lat = 22.5726
        user_lon = 88.3639

        with self.map.canvas:

            Color(0, 0, 1, 1)

            Line(
                points=[
                    user_lon * 10,
                    user_lat * 10,
                    dest_lon * 10,
                    dest_lat * 10
                ],
                width=3
            )

    def go_back(self, instance):
        self.manager.current = "attractions"