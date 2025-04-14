import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Failed to retrieve weather data. Please check the city name and API key.")

if __name__ == "__main__":
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        print("API Key is not set in .env file.")
        exit(1)
    
    city = input("Enter the city name: ")
    get_weather(api_key, city)