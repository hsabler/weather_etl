import os
import pandas as pd


class CsvRecord:
    """
    Класс для сохранения данных о погоде в CSV-файл.

    Методы:
        - save: сохраняет pandas DataFrame в CSV с указанным именем файла
    """

    def save(self, df: pd.DataFrame, file_name: str):
        """
        Сохраняет DataFrame в CSV-файл в папке 'data'.

        Args:
            df (pd.DataFrame): Таблица с данными о погоде или любыми другими данными
            file_name (str): Имя файла для сохранения (например, 'weather_data.csv')

        Returns:
            None
        """
        # Путь к папке 'data'
        data_dir = 'data'

        # Полный путь для сохранения файла
        file_path = os.path.join(data_dir, file_name)

        # Сохраняем DataFrame в CSV
        df.to_csv(file_path, index=False)
