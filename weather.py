from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()

def get_current_weather(city="Tangail"):
  requests_url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv("API_KEY")}&units=imperial'

  weather_data=requests.get(requests_url).json()
  return weather_data
if __name__ == '__main__':
  print("\n***Get Currentr Weather Conditions***\n")
  city=input('\nPlease enter a city name:')
  if not bool (city.strip()):
    city="Tangail"
  weather_data=get_current_weather()
  print("\n")
  pprint(weather_data)
