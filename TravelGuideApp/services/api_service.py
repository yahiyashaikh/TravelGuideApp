import requests

API_KEY = "YOUR_API_KEY"

class TourismAPI:

    def get_places(self, lat, lon):

        url = f"https://api.opentripmap.com/0.1/en/places/radius?radius=5000&lon={lon}&lat={lat}&apikey={API_KEY}"

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        return []