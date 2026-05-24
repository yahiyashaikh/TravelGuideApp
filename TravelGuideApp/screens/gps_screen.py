from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from kivy.uix.boxlayout import BoxLayout


class GPSScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.location_label = MDLabel(
            text="GPS simulation for Windows",
            halign="center"
        )

        gps_btn = MDRaisedButton(
            text="Get Current Location",
            pos_hint={"center_x": 0.5},
            on_release=self.get_location
        )

        back_btn = MDRaisedButton(
            text="Back",
            pos_hint={"center_x": 0.5},
            on_release=self.go_back
        )

        layout.add_widget(self.location_label)
        layout.add_widget(gps_btn)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def get_location(self, instance):

        # Simulated Kolkata GPS coordinates
        lat = 22.5726
        lon = 88.3639

        self.location_label.text = (
            f"Latitude: {lat}\n"
            f"Longitude: {lon}"
        )

    def go_back(self, instance):
        self.manager.current = "home"