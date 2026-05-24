from plyer import gps

class GPSService:

    def start_gps(self):
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except:
            print("GPS not supported on this device")

    def on_location(self, **kwargs):
        print(kwargs)