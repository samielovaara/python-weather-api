# Self-Hosted GitHub Runner Example

This project demonstrates the use of python libraries, RestAPI, unittest, and pylint. It is also used as a showcase for containerised self-hosted actions runner. 

https://github.com/samielovaara/github-runner 

https://github.com/samielovaara/python-weather-api/actions

## Features

- **Pylint**: Checks code quality standards.
- **Unittest**: Facilitates unit testing for the Python script.
- **Library Imports**: Utilizes external Python libraries:
  - `geopy`: For geocoding city names to coordinates.
  - `requests`: For making REST API calls.
- **REST API Integration**: Fetches weather data using the OpenWeatherMap API.

## Prerequisites

- Python 3.8 or later.
- A valid OpenWeatherMap API key.
- Libraries listed in `requirements.txt` (installable via pip).

## Setup

1. Clone this repository:

   ```bash
   git clone git@github.com:samielovaara/python-weather-api.git
   cd python-weather-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the `WEATHER_API_KEY` environment variable with your OpenWeatherMap API key:

   ```bash
   export WEATHER_API_KEY="your_api_key"
   ```

4. Run the script to get weather data for a city (default is Helsinki):

   ```bash
   python main.py --city <City_Name>
   ```

## Usage

The script provides weather details such as temperature, wind speed, and cloud coverage for a given city. If rain data is available, it will also be displayed.

### Command-Line Arguments

- `--city`: Specify the name of the city. Defaults to Helsinki if not provided.

Example:

```bash
python main.py --city "New York"
```

## Testing

```bash
python3 -m unittest src/test_main.py
```

