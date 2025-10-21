import pandas as pd

class WeatherTransformer:
    """
        Класс для преобразования "сырых" данных о погоде в удобный формат

        Методы:
            - to_dataframe: преобразует список словарей с данными о погоде в pandas DataFrame,
              добавляя дополнительные вычисленные столбцы (например, температуру в Фаренгейтах)
        """
    def to_dataframe(self, raw_data: list[dict]) -> pd.DataFrame:
        """
               Преобразует список словарей с погодой в DataFrame и добавляет столбец с температурой

               Args:
                   raw_data (list[dict]): Список словарей с данными о погоде. Каждый словарь должен
                                          содержать ключ 'temperature' (температура в Цельсиях)

               Returns:
                   pd.DataFrame: DataFrame с исходными данными и дополнительным столбцом 'temperature_F'
               """
        # Создание DataFrame из списка словарей
        df = pd.DataFrame(raw_data)
        # Добавление столбца с температурой в Фаренгейтах
        df["temperature_F"] = df["temperature"] * 9/5 + 32
        return df