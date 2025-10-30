import logging
from config import CITIES
from api.api_client import WeatherAPIClient
from transformer.weather_transformer import WeatherTransformer
from storage.weather_record import CsvRecord
from helper.TimestampHelper import timestamp

# Новый класс для генерации имени файла и логирования
class FileLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)  # создаем логгер

    def generate_filename(self):
        # Формируем имя файла с временной меткой
        return f"weather_data_{timestamp}.csv"

    def log_success(self, filename):
        # Логируем успех сохранения
        self.logger.info(f"Данные успешно сохранены в файл {filename}")


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
    file_logger = FileLogger()  # создаем объект для работы с файлами и логированием

    # Сбор и преобразование сырых данных о погоде для всех городов
    raw = api.get_all_cities(CITIES)
    logging.info("Получены данные о погоде для выбранных городов")
    df = transformer.to_dataframe(raw)
    logging.info("Данные преобразованы в DataFrame")

    # Генерация имени файла и логирование
    filename = file_logger.generate_filename()
    record.save(df, filename)
    file_logger.log_success(filename)  # логируем успешное сохранение


if __name__ == "__main__":
    main()
