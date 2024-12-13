# pylint: disable=missing-function-docstring
'''Get weather data for a location '''

import os
import sys
import argparse
from geopy.geocoders import Nominatim
import requests


def arg_parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", default="Helsinki", help="give a city")
    args = parser.parse_args(args)
    return args


def main(args):
    lat, lon = get_coordinates(args.city)
    key = os.environ.get("WEATHER_API_KEY")
    weather_data = get_weather_data(lat, lon, key)
    print_weather_data(weather_data)


def get_coordinates(city: str)->tuple:
    geolocator = Nominatim(user_agent="saminsaaappi")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude


def get_weather_data(lat, lon, key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def print_weather_data(data):
    print(data["name"])
    temperature = to_celcius(data["main"]["temp"])
    print("Temperature: ", temperature)
    print("Wind speed: ", data["wind"]["speed"])
    print("Cloud coverage: ", data["clouds"]["all"])

    try:
        print("Expected rain: ", data["rain"]["1h"])
    except KeyError:
        print("Rain data not available.")


def to_celcius(temperature):
    celsius = temperature - 273.15
    celsius = round(celsius, 2)
    return celsius


if __name__ == "__main__":
    main(arg_parse(sys.argv[1:]))
