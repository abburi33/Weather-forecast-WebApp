import os
import requests

API_key = os.getenv("WEATHER_API")


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    # 8 weather entries per day
    nr_days = 8 * forecast_days
    filtered_data = data["list"][:nr_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
