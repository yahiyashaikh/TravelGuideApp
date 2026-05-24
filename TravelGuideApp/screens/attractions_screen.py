import webbrowser

from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.metrics import dp
from kivy.graphics import Color, Rectangle

from services.offline_service import OfflineService


class AttractionsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.db = OfflineService()

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
            text="Nearby Attractions",
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

        # ================= ATTRACTIONS =================

        attractions = [

            {
                "name": "Victoria Memorial",
                "distance": "2 KM Away",
                "image": "assets/images.jpg",
                "lat": 22.5448,
                "lon": 88.3426
            },

            {
                "name": "Eco Park",
                "distance": "5 KM Away",
                "image": "assets/ecopark.jpg",
                "lat": 22.5806,
                "lon": 88.4674
            },

            {
                "name": "Science City",
                "distance": "3 KM Away",
                "image": "assets/sciencecity.jpg",
                "lat": 22.5401,
                "lon": 88.3965
            },

            {
                "name": "Indian Museum",
                "distance": "4 KM Away",
                "image": "assets/meusium.jpg",
                "lat": 22.5580,
                "lon": 88.3509
            },

            {
                "name": "Howrah Bridge",
                "distance": "6 KM Away",
                "image": "assets/Howrah.jpg",
                "lat": 22.5850,
                "lon": 88.3468
            }

        ]

        # ================= CARDS =================

        for place in attractions:

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
                source=place["image"],
                size_hint=(1, None),
                height=dp(180)
            )

            # ================= PLACE NAME =================

            place_name = MDLabel(
                text=place["name"],
                font_style="H6",
                bold=True,
                halign="center",
                size_hint_y=None,
                height=dp(35)
            )

            # ================= DISTANCE =================

            place_distance = MDLabel(
                text=place["distance"],
                halign="center",
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(25)
            )

            # ================= BUTTON LAYOUT =================

            button_layout = BoxLayout(
                orientation="horizontal",
                spacing=dp(10),
                size_hint=(1, None),
                height=dp(55)
            )

            # ================= SAVE BUTTON =================

            save_btn = MDRaisedButton(
                text="Save Offline",
                size_hint=(0.5, None),
                height=dp(50),
                md_bg_color=(0.1, 0.55, 0.9, 1),
                on_release=lambda x, p=place: self.save_place(p)
            )

            # ================= NAVIGATE BUTTON =================

            navigate_btn = MDRaisedButton(
                text="Navigate",
                size_hint=(0.5, None),
                height=dp(50),
                md_bg_color=(0.0, 0.65, 0.3, 1),
                on_release=lambda x, p=place: self.navigate_to_place(p)
            )

            # ================= ADD BUTTONS =================

            button_layout.add_widget(save_btn)
            button_layout.add_widget(navigate_btn)

            # ================= ADD TO CARD =================

            card.add_widget(image)
            card.add_widget(place_name)
            card.add_widget(place_distance)
            card.add_widget(button_layout)

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

    # ================= SAVE PLACE =================

    def save_place(self, place):

        self.db.save_place(
            place["name"],
            place["distance"],
            "Tourist Attraction",
            place["image"]
        )

        dialog = MDDialog(
            title="Success",
            text=f"{place['name']} saved successfully!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )

        dialog.open()

    # ================= NAVIGATION =================

    def navigate_to_place(self, place):

        navigation_screen = self.manager.get_screen("navigation")

        navigation_screen.show_route(
            place["name"],
            place["lat"],
            place["lon"]
        )

        self.manager.current = "navigation"

    # ================= BACK =================

    def go_back(self, instance):
        self.manager.current = "home"