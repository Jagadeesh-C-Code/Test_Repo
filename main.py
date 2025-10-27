# main.py
import requests

def get_weather(city):
    api_key = "your_api_key_here"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp'] - 273.15:.2f}°C")
    else:
        print("City not found!")

get_weather("London")
