# pylint: disable=missing-function-docstring

'''Hakee säätiedot openweathermapista '''

import os
import sys
import argparse
from geopy.geocoders import Nominatim
import requests
#import json


def arg_parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", default="Helsinki", help="give a city")
    args = parser.parse_args(args)
    return args


def main(args):
    lat, lon = get_coordinates(args.city)
    key = os.environ.get("WEATHER_API_KEY")
    weather_data = weather_in(lat, lon, key)
    print_weather_data(weather_data)


def get_coordinates(city: str)->tuple:
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="saminsaaappi")

    # Get location information
    location = geolocator.geocode(city)

    #get lon lat
    return location.latitude, location.longitude


def weather_in(lat, lon, key):
    # get weather info from url
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def print_weather_data(data):
    # Annettu kaupunki
    print(data["name"])

    # Annetun kaupungin lämpötila
    temperature = to_celcius(data["main"]["temp"])
    print("lämpötila: ", temperature)

    # Annetun kaupungin tuulennopeus
    print("tuulen nopeus: ", data["wind"]["speed"])

    # Annetun kaupungin pilvisyys
    print("kaupungin pilvisyys: ", data["clouds"]["all"])

    # Annetun kaupungin odotettu sademäärä
    try:
        print("odotettu sademäärä: ", data["rain"]["1h"])
    except KeyError as e:
        print(f"KeyError: {e}")

    # jos haluaa tulostaa koko datan, printtaa:
    #print(json.dumps(data, indent=4))


def to_celcius(temperature):
    celsius = temperature - 273.15
    celsius = round(celsius, 2)
    return celsius


if __name__ == "__main__":
    main(arg_parse(sys.argv[1:]))
