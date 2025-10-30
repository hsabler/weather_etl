import logging
from config import CITIES
from api.api_client import WeatherAPIClient
from transformer.weather_transformer import WeatherTransformer
from storage.weather_record import CsvRecord
from helper.TimestampHelper import timestamp

class FileLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)  # Инициализация логгера

    def generate_filename(self):
        """
        Генерирует имя файла с текущей временной меткой
        """
        return f"weather_data_{timestamp}.csv"

    def log_success(self, filename):
        """
        Логирует успешное сохранение данных в файл
        """
        self.logger.info(f"Данные успешно сохранены в файл {filename}")


def main():
    """
    Главная функция для получения, преобразования и сохранения данных
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

    # Получение данных о погоде для всех городов
    raw = api.get_all_cities(CITIES)  # Логирование скрыто внутри метода
    df = transformer.to_dataframe(raw)  # Логирование будет скрыто в методах трансформера

    # Сохранение данных в CSV
    file_logger = FileLogger()  # создаем объект для работы с файлами и логированием
    filename = file_logger.generate_filename()  # Генерация имени файла
    record.save(df, filename)
    file_logger.log_success(filename)  # Логирование успешного сохранения

if __name__ == "__main__":
    main()
