from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screens.map_screen import MapScreen
from screens.home_screen import HomeScreen
from screens.attractions_screen import AttractionsScreen
from screens.hotels_screen import HotelsScreen
from screens.transport_screen import TransportScreen
from screens.offline_screen import OfflineScreen
from screens.settings_screen import SettingsScreen
from screens.gps_screen import GPSScreen
from screens.navigation_screen import NavigationScreen
from screens.live_tracking_screen import LiveTrackingScreen
class TravelGuideApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager()

        home = HomeScreen(name="home")
        attractions = AttractionsScreen(name="attractions")
        hotels = HotelsScreen(name="hotels")
        transport = TransportScreen(name="transport")
        offline = OfflineScreen(name="offline")
        settings = SettingsScreen(name="settings")

        sm.add_widget(home)
        sm.add_widget(attractions)
        sm.add_widget(hotels)
        sm.add_widget(transport)
        sm.add_widget(offline)
        sm.add_widget(settings)

        maps = MapScreen(name="maps")
        sm.add_widget(maps)

        gps_screen = GPSScreen(name="gps")
        sm.add_widget(gps_screen)

        live_tracking = LiveTrackingScreen(name="live_tracking")
        sm.add_widget(live_tracking)
        navigation = NavigationScreen(name="navigation")
        sm.add_widget(navigation)

        return sm

if __name__ == "__main__":
    TravelGuideApp().run()