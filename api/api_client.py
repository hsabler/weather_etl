import logging
import requests
from config import BASEURL


class WeatherAPIClient:
    """
        Класс для получения данных о текущей погоде через API Open-Meteo

        Методы:
            - get_city_weather: Получает текущую погоду для одного города
            - get_all_cities: Получает текущую погоду для нескольких городов
        """
    def get_city_weather(self, city: str, lat: float, lon: float) -> dict:
        """
                Получает текущую погоду для указанного города

                Args:
                    city (str): Название города
                    lat (float): Широта города
                    lon (float): Долгота города

                Returns:
                    dict: Словарь с данными о погоде, включая название города
                          и значения из current_weather API

                Raises:
                    HTTPError: Если запрос к API завершился ошибкой
                """
        url = f"{BASEURL}?latitude={lat}&longitude={lon}&current_weather=true"
        logging.info(f"Запрос погоды для {city} из {url}")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "city": city,
            **data["current_weather"]
        }

    def get_all_cities(self, cities: dict) -> list[dict]:
        """
                Получает текущую погоду для всех городов из переданного словаря.

                Args:
                    cities (dict): Словарь вида {"город": (широта, долгота)}

                Returns:
                    list[dict]: Список словарей с данными о погоде для каждого города.

                Логирование:
                    Информационные сообщения о получении данных и ошибки при неудаче.
                """
        results = []
        for city, (lat, lon) in cities.items():
            try:
                results.append(self.get_city_weather(city, lat, lon))
                logging.info(f"Получен прогноз погоды для {city}")
            except Exception as e:
                logging.error(f"Не удалось получить прогноз погоды в {city}: {e}")
        return results