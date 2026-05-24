from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.metrics import dp
from kivy.graphics import Color, Rectangle


class HomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ================= MAIN LAYOUT =================

        main_layout = BoxLayout(
            orientation="vertical",
            spacing=dp(15),
            padding=dp(15)
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

        # ================= SCROLL VIEW =================

        scroll = ScrollView(
            do_scroll_x=False
        )

        # ================= CONTENT LAYOUT =================

        content = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            size_hint_y=None,
            padding=dp(10)
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        # ================= BANNER IMAGE =================

        banner = Image(
            source="assets/banner.png",
            size_hint=(1, None),
            height=dp(200)
        )

        # ================= TITLE =================

        title = MDLabel(
            text="Travel & Transport",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=dp(60)
        )

        # ================= SUBTITLE =================

        subtitle = MDLabel(
            text="Explore Smart Tourism & Live Transit",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(40)
        )

        # ================= ADD HEADER =================

        content.add_widget(banner)
        content.add_widget(title)
        content.add_widget(subtitle)

        # ================= FEATURES =================

        features = [

            ("Nearby Attractions", self.open_attractions),
            ("Hotels & Booking", self.open_hotels),
            ("Live Transport Tracker", self.open_transport),
            ("Offline Saved Places", self.open_offline),
            ("Open Interactive Maps", self.open_maps),
            ("GPS Location", self.open_gps)

        ]

        # ================= BUTTON CARDS =================

        for text, action in features:

            card = MDCard(
                orientation="vertical",
                padding=dp(12),
                size_hint=(1, None),
                height=dp(90),
                elevation=5,
                md_bg_color=(1, 1, 1, 1),
            )

            button = MDRaisedButton(
                text=text,
                pos_hint={
                    "center_x": 0.5,
                    "center_y": 0.5
                },
                size_hint=(0.95, None),
                height=dp(55),
                md_bg_color=(0.1, 0.55, 0.9, 1),
                font_size="17sp",
                on_release=action
            )

            card.add_widget(button)

            content.add_widget(card)

        # ================= FINAL ADD =================

        scroll.add_widget(content)

        main_layout.add_widget(scroll)

        self.add_widget(main_layout)

    # ================= UPDATE BACKGROUND =================

    def update_rect(self, instance, value):

        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # ================= NAVIGATION =================

    def open_attractions(self, instance):
        self.manager.current = "attractions"

    def open_hotels(self, instance):
        self.manager.current = "hotels"

    def open_transport(self, instance):
        self.manager.current = "transport"

    def open_offline(self, instance):
        self.manager.current = "offline"

    def open_maps(self, instance):
        self.manager.current = "maps"

    def open_gps(self, instance):
        self.manager.current = "gps"