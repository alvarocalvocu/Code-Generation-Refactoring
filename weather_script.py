# Fetch weather data from OpenWeatherMap API

import requests

def get_weather(city_name, api_key):
    """
    Fetches current weather data for a given city from OpenWeatherMap API.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    print("Request URL:", response.url)  # Depuración
    print("Response:", response.text)    # Depuración
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def display_weather(data, city):
    """
    Processes and displays weather information.
    """
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"Weather in {city}:")
    print(f"  Condition: {weather_desc.capitalize()}")
    print(f"  Temperature: {temp}°C")
    print(f"  Humidity: {humidity}%")

if __name__ == "__main__":
    # api_key = input("Enter your OpenWeatherMap API key: ")
    api_key = "8e5a69bfdd4456bd1d817dfb52e76f3c"  # Solo para pruebas locales, no subir a repositorio público
    city = input("Enter city name: ")
    data = get_weather(city, api_key)
    if data:
        display_weather(data, city)