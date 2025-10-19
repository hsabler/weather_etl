import pandas as pd
import logging

class CsvRecord:
    def save(self, df: pd.DataFrame, file_path: str):
        df.to_csv(file_path, index=False)
        logging.info(f"Data saved to {file_path}")