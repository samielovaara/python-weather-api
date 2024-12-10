import os
import unittest
from unittest.mock import patch
import requests


from main import to_celcius, weather_in

class TestCalculations(unittest.TestCase):

    def test_to_celcius(self):
        conversion = to_celcius(1)
        self.assertAlmostEqual(conversion, -272.15)


class TestWeatherIn(unittest.TestCase):
    @patch("requests.get")  # Mock the requests.get method
    def test_weather_in_success(self, mock_get):
        # Arrange
        lat, lon = 60.1695, 24.9354  # Helsinki coordinates
        fake_key = "test_key"
        os.environ["WEATHER_API_KEY"] = fake_key  # Set a fake API key

        # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.return_value = None  # No exception
        mock_response.json.return_value = {"weather": "test_weather"}
        mock_get.return_value = mock_response

        # Act
        result = weather_in(lat, lon, fake_key)

        # Assert
        expected_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={fake_key}"
        )
        mock_get.assert_called_once_with(expected_url)  # Verify the URL
        self.assertEqual(result, {"weather": "test_weather"})  # Verify the response
    
    @patch("requests.get")  # Mock the requests.get method
    def test_weather_in_fail(self, mock_get):
        # Arrange
        lat, lon = 60.1695, 24.9354  # Helsinki coordinates
        fake_key = "test_key"
        os.environ["WEATHER_API_KEY"] = fake_key  # Set a fake API key

        # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Test HTTP error")
        mock_get.return_value = mock_response

        # Act & Assert
        with self.assertRaises(requests.exceptions.HTTPError) as context:
            weather_in(lat, lon, fake_key)
        self.assertIn("Test HTTP error", str(context.exception))