import pandas as pd

class CsvRecord:
    """
        Класс для сохранения данных о погоде в CSV-файл

        Методы:
            - save: сохраняет pandas DataFrame в CSV с указанным именем файла
        """
    def save(self, df: pd.DataFrame, file_path: str):
        """
               Сохраняет DataFrame в CSV-файл

               Args:
                   df (pd.DataFrame): Таблица с данными о погоде или любыми другими данными
                   file_path (str): Путь и имя файла для сохранения (например, 'weather_data.csv')

               Returns:
                   None
               """
        df.to_csv(file_path, index=False)