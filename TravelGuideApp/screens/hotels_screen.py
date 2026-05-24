import webbrowser

from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from kivy.metrics import dp
from kivy.graphics import Color, Rectangle


class HotelsScreen(MDScreen):

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
            text="Hotel Booking",
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

        # ================= HOTEL DATA =================

        hotels = [

            {
                "name": "ITC Royal Bengal",
                "price": "₹12,000/night",
                "rating": "⭐ 4.8",
                "image": "assets/hotel1.jpg"
            },

            {
                "name": "Taj Bengal",
                "price": "₹15,000/night",
                "rating": "⭐ 4.9",
                "image": "assets/hotel2.jpg"
            },

            {
                "name": "Novotel Kolkata",
                "price": "₹8,000/night",
                "rating": "⭐ 4.5",
                "image": "assets/hotel3.jpg"
            },

            {
                "name": "Hyatt Regency",
                "price": "₹10,000/night",
                "rating": "⭐ 4.7",
                "image": "assets/hotel4.jpg"
            }

        ]

        # ================= HOTEL CARDS =================

        for hotel in hotels:

            card = MDCard(
                orientation="vertical",
                padding=dp(12),
                spacing=dp(12),
                size_hint=(1, None),
                height=dp(360),
                elevation=5,
                md_bg_color=(1, 1, 1, 1)
            )

            # ================= HOTEL IMAGE =================

            image = Image(
                source=hotel["image"],
                size_hint=(1, None),
                height=dp(190)
            )

            # ================= HOTEL NAME =================

            hotel_name = MDLabel(
                text=hotel["name"],
                font_style="H6",
                bold=True,
                halign="center",
                size_hint_y=None,
                height=dp(35)
            )

            # ================= PRICE =================

            hotel_price = MDLabel(
                text=hotel["price"],
                halign="center",
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(25)
            )

            # ================= RATING =================

            hotel_rating = MDLabel(
                text=hotel["rating"],
                halign="center",
                size_hint_y=None,
                height=dp(25)
            )

            # ================= BOOK BUTTON =================

            book_btn = MDRaisedButton(
                text="Book Now",
                size_hint=(0.8, None),
                height=dp(50),
                pos_hint={"center_x": 0.5},
                md_bg_color=(0.1, 0.55, 0.9, 1),
                on_release=self.open_booking
            )

            # ================= ADD TO CARD =================

            card.add_widget(image)
            card.add_widget(hotel_name)
            card.add_widget(hotel_price)
            card.add_widget(hotel_rating)
            card.add_widget(book_btn)

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

    # ================= OPEN BOOKING =================

    def open_booking(self, instance):
        webbrowser.open("https://www.booking.com")

    # ================= GO BACK =================

    def go_back(self, instance):
        self.manager.current = "home"