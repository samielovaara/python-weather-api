# pylint: disable=missing-function-docstring

'''Hakee säätiedot openweathermapista '''

import os
import sys
import argparse
from geopy.geocoders import Nominatim
import requests

def arg_parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True, default="Helsinki", help="give a city")
    args = parser.parse_args(args)
    return args

def main(args):
    lat, lon = get_coordinates(args.city)
    weather_in(lat, lon)

def get_coordinates(city: str)->tuple:
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="saminsaaappi")

    # Get location information
    location = geolocator.geocode(city)

    #get lon lat
    return location.latitude, location.longitude

def weather_in(lat, lon):
    # api key
    key = os.environ.get("WEATHER_API_KEY")

    # url
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

    # response url
    response = requests.get(url)

    # response to json string format
    #nice_data = json.dumps(response.json(), indent=4)

    api_data = response.json()

    # print some data
    print_info(api_data)


def print_info(data):
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
    except:
        print("ei sademäärää saatavilla")

    #print(json.dumps(data, indent=4))

def to_celcius(temperature):
    celsius = temperature - 273.15
    celsius = round(celsius, 1)
    return celsius

if __name__ == "__main__":
    main(arg_parse(sys.argv[1:]))
