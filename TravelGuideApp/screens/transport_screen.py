from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.metrics import dp
from kivy.graphics import Color, Rectangle


class TransportScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ================= MAIN LAYOUT =================

        main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(15)
        )

        # ================= BACKGROUND =================

        with main_layout.canvas.before:
            Color(0.96, 0.96, 0.96, 1)

            self.rect = Rectangle(
                pos=main_layout.pos,
                size=main_layout.size
            )

        main_layout.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        # ================= TITLE =================

        title = MDLabel(
            text="Live Transport Tracker",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=dp(60)
        )

        # ================= SCROLL =================

        scroll = ScrollView(
            do_scroll_x=False
        )

        # ================= CONTENT =================

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            size_hint_y=None,
            padding=dp(10)
        )

        content.bind(
            minimum_height=content.setter('height')
        )

        # ================= VEHICLE DATA =================

        vehicles = [

            {
                "name": "Bus 101",
                "arrival": "5 mins",
                "route": "Salt Lake → Howrah",
                "image": "assets/bus1.jpg",
                "lat": 22.5726,
                "lon": 88.3639
            },

            {
                "name": "Metro Blue Line",
                "arrival": "2 mins",
                "route": "Dum Dum → Kavi Subhash",
                "image": "assets/metro.jpg",
                "lat": 22.5950,
                "lon": 88.3700
            },

            {
                "name": "Bus 202",
                "arrival": "8 mins",
                "route": "Airport → Garia",
                "image": "assets/bus2.jpg",
                "lat": 22.5600,
                "lon": 88.4000
            },

            {
                "name": "Local Train",
                "arrival": "10 mins",
                "route": "Sealdah → Barrackpore",
                "image": "assets/train.jpg",
                "lat": 22.6500,
                "lon": 88.4100
            }

        ]

        # ================= VEHICLE CARDS =================

        for vehicle in vehicles:

            card = MDCard(
                orientation="vertical",
                padding=dp(12),
                spacing=dp(12),
                size_hint=(1, None),
                height=dp(360),
                elevation=5,
                md_bg_color=(1, 1, 1, 1)
            )

            # ================= IMAGE =================

            image = Image(
                source=vehicle["image"],
                size_hint=(1, None),
                height=dp(190)
            )

            # ================= VEHICLE NAME =================

            vehicle_name = MDLabel(
                text=vehicle["name"],
                font_style="H6",
                bold=True,
                halign="center",
                size_hint_y=None,
                height=dp(35)
            )

            # ================= ROUTE =================

            route = MDLabel(
                text=f"Route: {vehicle['route']}",
                halign="center",
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(30)
            )

            # ================= ARRIVAL =================

            arrival = MDLabel(
                text=f"Arrival: {vehicle['arrival']}",
                halign="center",
                size_hint_y=None,
                height=dp(30)
            )

            # ================= TRACK BUTTON =================

            track_btn = MDRaisedButton(
                text="Track Live",
                size_hint=(0.8, None),
                height=dp(50),
                pos_hint={"center_x": 0.5},
                md_bg_color=(0.1, 0.55, 0.9, 1),
                on_release=lambda x, v=vehicle: self.open_live_tracking(v)
            )

            # ================= ADD TO CARD =================

            card.add_widget(image)
            card.add_widget(vehicle_name)
            card.add_widget(route)
            card.add_widget(arrival)
            card.add_widget(track_btn)

            # ================= ADD CARD =================

            content.add_widget(card)

        # ================= ADD CONTENT =================

        scroll.add_widget(content)

        # ================= BACK BUTTON =================

        back_btn = MDRaisedButton(
            text="Back",
            size_hint=(1, None),
            height=dp(55),
            md_bg_color=(0.9, 0.2, 0.2, 1),
            on_release=self.go_back
        )

        # ================= FINAL ADD =================

        main_layout.add_widget(title)
        main_layout.add_widget(scroll)
        main_layout.add_widget(back_btn)

        self.add_widget(main_layout)

    # ================= UPDATE BACKGROUND =================

    def update_rect(self, instance, value):

        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # ================= LIVE TRACKING =================

    def open_live_tracking(self, vehicle):

        tracking_screen = self.manager.get_screen("live_tracking")

        tracking_screen.update_location(
            vehicle["name"],
            vehicle["lat"],
            vehicle["lon"]
        )

        self.manager.current = "live_tracking"

    # ================= GO BACK =================

    def go_back(self, instance):
        self.manager.current = "home"