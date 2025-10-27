import logging
import requests
from config import BASEURL

class WeatherAPIClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_city_weather(self, city: str, lat: float, lon: float) -> dict:
        """
        Получает текущую погоду для указанного города.
        """
        url = f"{BASEURL}?latitude={lat}&longitude={lon}&current_weather=true"
        logging.info(f"Запрос погоды для города {city} по URL {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Выбросит исключение при ошибке запроса
            data = response.json()
            logging.info(f"Получены данные о погоде для города {city}")
            return {
                "city": city,
                **data["current_weather"]
            }
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка при запросе погоды для города {city}: {e}")
            raise

    def get_all_cities(self, cities: dict) -> list[dict]:
        """
        Получает текущую погоду для всех городов из переданного словаря.
        """
        results = []
        for city, (lat, lon) in cities.items():
            try:
                # Логирование скрыто внутри метода get_city_weather
                results.append(self.get_city_weather(city, lat, lon))
            except Exception as e:
                logging.error(f"Не удалось получить данные для города {city}: {e}")
        return results
