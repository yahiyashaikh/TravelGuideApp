from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView
from kivymd.uix.button import MDRaisedButton

class MapScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical"
        )

        # Kolkata coordinates
        self.map = MapView(
            zoom=10,
            lat=22.5726,
            lon=88.3639
        )

        back_btn = MDRaisedButton(
            text="Back",
            size_hint=(1, 0.1),
            on_release=self.go_back
        )

        layout.add_widget(self.map)
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "home"