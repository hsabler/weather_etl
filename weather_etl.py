import requests
import pandas as pd

cities = {
    "London": [51.5072, -0.1276],
    "Berlin": [52.5200, 13.4050],
    "Paris": [48.8566, 2.3522],
    "New York": [40.7128, -74.0060]
}

weather_data = []

for city, (lat, lon) in cities.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    current = data["current_weather"]

    weather_data.append({
        "city": city,
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "time": current["time"]
    })

df = pd.DataFrame(weather_data)
df["temperature_F"] = df["temperature"] * 9/5 + 32

df.to_csv("weather_data.csv", index=False)

print("✅ Данные сохранены в файл weather_data.csv")
print(df)
