import logging
from config import CITIES
from helper.TimestampHelper import Helpers
from src.api_client import WeatherAPIClient
from src.weather_transformer import WeatherTransformer
from src.weather_record import CsvRecord

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    api = WeatherAPIClient()
    transformer = WeatherTransformer()
    record = CsvRecord()
    raw = api.get_all_cities(CITIES)
    df = transformer.to_dataframe(raw)
    filename = f"weather_data_{Helpers.Timestamper.SetDateTimeNow}.csv"

    record.save(df, filename)

if __name__ == "__main__":
    main()
