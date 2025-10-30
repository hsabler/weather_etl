import pandas as pd
import logging
import os

class CsvRecord:
    """
    Класс для сохранения данных о погоде в CSV-файл

    Методы:
        - save: сохраняет pandas DataFrame в CSV с указанным именем файла
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)  # Инициализация логгера

    def save(self, df: pd.DataFrame, file_path: str):
        """
        Сохраняет DataFrame в CSV-файл

        Args:
            df (pd.DataFrame): Таблица с данными о погоде или любыми другими данными
            file_path (str): Путь и имя файла для сохранения (например, 'weather_data.csv')

        Returns:
            None
        """
        # Папка для сохранения данных
        data_folder = "data"

        # Формируем полный путь для сохранения файла в папке 'data'
        full_file_path = os.path.join(data_folder, file_path)

        try:
            self.logger.info(f"Попытка сохранить данные в файл: {full_file_path}")
            df.to_csv(full_file_path, index=False)  # Сохраняем данные в файл
            self.logger.info(f"Данные успешно сохранены в файл: {full_file_path}")
        except Exception as e:
            self.logger.error(f"Ошибка при сохранении данных в файл {full_file_path}: {e}")
