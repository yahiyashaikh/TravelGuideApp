from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel

from kivy_garden.mapview import MapView, MapMarker

from kivy.clock import Clock


class LiveTrackingScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.current_lat = 22.5726
        self.current_lon = 88.3639

        self.layout = BoxLayout(
            orientation="vertical"
        )

        self.title = MDLabel(
            text="Live Tracking",
            halign="center",
            size_hint=(1, 0.08)
        )

        self.map = MapView(
            zoom=12,
            lat=self.current_lat,
            lon=self.current_lon
        )

        self.marker = MapMarker(
            lat=self.current_lat,
            lon=self.current_lon
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

        # Start movement simulation
        Clock.schedule_interval(self.move_vehicle, 2)

    def update_location(self, vehicle_name, lat, lon):

        self.title.text = f"{vehicle_name} Live Location"

        self.current_lat = lat
        self.current_lon = lon

        self.map.center_on(lat, lon)

        self.marker.lat = lat
        self.marker.lon = lon

    def move_vehicle(self, dt):

        # Simulated movement
        self.current_lat += 0.001
        self.current_lon += 0.001

        self.marker.lat = self.current_lat
        self.marker.lon = self.current_lon

        self.map.center_on(
            self.current_lat,
            self.current_lon
        )

    def go_back(self, instance):
        self.manager.current = "transport"