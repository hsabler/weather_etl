import requests
import logging
from config import BASEURL

class WeatherAPIClient:
    def get_city_weather(self, city: str, lat: float, lon: float) -> dict:
        url = f"{BASEURL}?latitude={lat}&longitude={lon}&current_weather=ture"
        logging.info(f"Requesting weather for {city} from {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            **data["current_weather"]
        }

    def get_all_cities(self, cities: dict) -> list[dict]:
        results = []
        for city, (lat, lon) in cities.items():
            try:
                results.append(self.get_city_weather(city, lat, lon))
            except Exception as e:
                logging.error(f"Failed to get weather for {city}: {e}")
        return results