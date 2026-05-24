from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.label import MDLabel


class SettingsScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        label = MDLabel(
            text="Dark Mode",
            halign="center"
        )

        switch = MDSwitch(
            pos_hint={"center_x": 0.5}
        )

        layout.add_widget(label)
        layout.add_widget(switch)

        self.add_widget(layout)