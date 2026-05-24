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


class OfflineScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.db = OfflineService()

        # ================= MAIN LAYOUT =================

        self.main_layout = BoxLayout(
            orientation="vertical",
            padding=dp(15),
            spacing=dp(15)
        )

        # ================= BACKGROUND =================

        with self.main_layout.canvas.before:
            Color(0.96, 0.96, 0.96, 1)

            self.rect = Rectangle(
                pos=self.main_layout.pos,
                size=self.main_layout.size
            )

        self.main_layout.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

        # ================= TITLE =================

        title = MDLabel(
            text="Offline Saved Places",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=dp(60)
        )

        # ================= SCROLL =================

        self.scroll = ScrollView(
            do_scroll_x=False
        )

        # ================= CONTENT =================

        self.content = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            size_hint_y=None,
            padding=dp(10)
        )

        self.content.bind(
            minimum_height=self.content.setter('height')
        )

        self.scroll.add_widget(self.content)

        # ================= REFRESH BUTTON =================

        refresh_btn = MDRaisedButton(
            text="Refresh Saved Places",
            size_hint=(1, None),
            height=dp(55),
            md_bg_color=(0.1, 0.55, 0.9, 1),
            on_release=self.load_places
        )

        # ================= BACK BUTTON =================

        back_btn = MDRaisedButton(
            text="Back",
            size_hint=(1, None),
            height=dp(55),
            md_bg_color=(0.9, 0.2, 0.2, 1),
            on_release=self.go_back
        )

        # ================= ADD WIDGETS =================

        self.main_layout.add_widget(title)
        self.main_layout.add_widget(self.scroll)
        self.main_layout.add_widget(refresh_btn)
        self.main_layout.add_widget(back_btn)

        self.add_widget(self.main_layout)

        self.load_places()

    # ================= UPDATE BACKGROUND =================

    def update_rect(self, instance, value):

        self.rect.pos = instance.pos
        self.rect.size = instance.size

    # ================= REFRESH ON ENTER =================

    def on_pre_enter(self):

        self.load_places()

    # ================= LOAD PLACES =================

    def load_places(self, *args):

        self.content.clear_widgets()

        places = self.db.get_places()

        # ================= EMPTY STATE =================

        if not places:

            empty_label = MDLabel(
                text="No Offline Saved Places",
                halign="center",
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(50)
            )

            self.content.add_widget(empty_label)

            return

        # ================= PLACE CARDS =================

        for place in places:

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
                source=place[4],
                size_hint=(1, None),
                height=dp(180)
            )

            # ================= PLACE NAME =================

            name = MDLabel(
                text=place[1],
                font_style="H6",
                bold=True,
                halign="center",
                size_hint_y=None,
                height=dp(35)
            )

            # ================= DISTANCE =================

            location = MDLabel(
                text=f"Distance: {place[2]}",
                halign="center",
                theme_text_color="Secondary",
                size_hint_y=None,
                height=dp(25)
            )

            # ================= DESCRIPTION =================

            description = MDLabel(
                text=place[3],
                halign="center",
                size_hint_y=None,
                height=dp(30)
            )

            # ================= DELETE BUTTON =================

            delete_btn = MDRaisedButton(
                text="Delete Saved Place",
                size_hint=(0.85, None),
                height=dp(50),
                pos_hint={"center_x": 0.5},
                md_bg_color=(0.9, 0.2, 0.2, 1),
                on_release=lambda x,
                pid=place[0],
                pname=place[1]:
                self.delete_place(pid, pname)
            )

            # ================= ADD TO CARD =================

            card.add_widget(image)
            card.add_widget(name)
            card.add_widget(location)
            card.add_widget(description)
            card.add_widget(delete_btn)

            # ================= ADD CARD =================

            self.content.add_widget(card)

    # ================= DELETE PLACE =================

    def delete_place(self, place_id, place_name):

        self.db.delete_place(place_id)

        dialog = MDDialog(
            title="Deleted",
            text=f"{place_name} removed successfully!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )

        dialog.open()

        self.load_places()

    # ================= GO BACK =================

    def go_back(self, instance):
        self.manager.current = "home"