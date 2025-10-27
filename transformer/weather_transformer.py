import pandas as pd
import logging


class WeatherTransformer:
    """
    Класс для преобразования "сырых" данных о погоде в удобный формат

    Методы:
        - to_dataframe: преобразует список словарей с данными о погоде в pandas DataFrame,
          добавляя дополнительные вычисленные столбцы (например, температуру в Фаренгейтах)
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)  # Инициализация логгера

    def to_dataframe(self, raw_data: list[dict]) -> pd.DataFrame:
        """
        Преобразует список словарей с погодой в DataFrame и добавляет столбец с температурой

        Args:
            raw_data (list[dict]): Список словарей с данными о погоде. Каждый словарь должен
                                   содержать ключ 'temperature' (температура в Цельсиях)

        Returns:
            pd.DataFrame: DataFrame с исходными данными и дополнительным столбцом 'temperature_F'
        """
        # Логирование начала преобразования
        self.logger.info("Начинаю преобразование данных о погоде в DataFrame.")

        # Создание DataFrame из списка словарей
        df = pd.DataFrame(raw_data)

        # Добавление столбца с температурой в Фаренгейтах
        df["temperature_F"] = df["temperature"] * 9 / 5 + 32

        # Логирование завершения преобразования
        self.logger.info("Данные успешно преобразованы в DataFrame.")

        return df
