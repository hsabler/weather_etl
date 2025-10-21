import logging
from config import CITIES
from api.api_client import WeatherAPIClient
from transformer.weather_transformer import WeatherTransformer
from storage.weather_record import CsvRecord
from helper.TimestampHelper import timestamp

def main():
    """
        Главная функция для получения, преобразования и сохранения данных

        Последовательность действий:
        1. Настраивает логирование для информирования о ходе выполнения
        2. Создаёт объекты для работы с API, трансформации данных и сохранения в CSV
        3. Получает сырые данные о погоде для всех городов из списка CITIES
        4. Преобразует сырые данные в pandas DataFrame для удобной обработки
        5. Формирует имя CSV-файла с текущей датой и временем для уникальности
        6. Сохраняет данные в CSV файл

        Используемые объекты:
            - WeatherAPIClient: получение данных о погоде
            - WeatherTransformer: преобразование данных в DataFrame
            - CsvRecord: сохранение данных в файл
        """
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )
    # Инициализация объектов для работы с API, сохранение данных
    api = WeatherAPIClient()
    transformer = WeatherTransformer()
    record = CsvRecord()
    # Сбор и преобразование сырых данных о погоде для всех городов
    raw = api.get_all_cities(CITIES)
    logging.info("Получены данные о погоде для выбранных городов")
    df = transformer.to_dataframe(raw)
    logging.info("Данные преобразованы в DataFrame")
    # Сохранение данных в CSV
    filename = f"weather_data_{timestamp}.csv"
    record.save(df, filename)
    logging.info(f"Данные успешно сохранены в файл {filename}")

if __name__ == "__main__":
    main()
