# Weather ETL Project 🌤️

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Data%20Analysis-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Requests](https://img.shields.io/badge/API%20Integration-Requests-FF6C37?style=for-the-badge)
![ETL Pipeline](https://img.shields.io/badge/ETL-Pipeline-blueviolet?style=for-the-badge)
![Open Meteo](https://img.shields.io/badge/API-Open%20Meteo-0099E5?style=for-the-badge)


Проект для извлечения, обработки и сохранения данных о текущей погоде для нескольких городов с использованием Python.

## Этот проект демонстрирует базовую ETL-пайплайн:  

1. **Extract** — получаем данные о погоде из публичного API [Open-Meteo](https://open-meteo.com/).  
2. **Transform** — обрабатываем данные с помощью `pandas` (добавляем температуру в °F).  
3. **Load** — сохраняем результат в CSV-файл.


## Используемые технологии

- Python 3.14  
- Библиотеки: `requests`, `pandas`  
- CSV-файл для хранения данных  


## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/hsabler/weather_etl.git
   cd weather_etl

2. Создайте и активируйте виртуальное окружение (опционально):

    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Запустите скрипт:
    ```bash
    python weather_etl.py

После выполнения появится файл weather_data.csv с актуальными данными о погоде.

👩‍💻 Автор

Anna Sabler
📍 GitHub: [@hsabler](https://github.com/hsabler)

⭐️ Если проект вам понравился — поставьте звёздочку на GitHub!
