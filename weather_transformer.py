import pandas as pd
import logging

class WeatherTransformer:
    def to_dataframe(self, raw_data: list[dict]) -> pd.DataFrame:
        logging.info("Transforming raw data into DataFrame")
        df = pd.DataFrame(raw_data)
        df["temperature_F"] = df["temperature"] * 9/5 + 32
        return df