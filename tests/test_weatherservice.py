#!/usr/bin/env python3
"""
Unit tests for the weather service using pytest
"""
import pytest
from unittest.mock import Mock, patch
from src.main import WeatherService
import requests


@pytest.fixture
def weather_service():
    """Create a WeatherService instance for testing"""
    return WeatherService()


class TestWeatherService:
    """Test cases for the WeatherService class"""

    def test_init(self):
        """Test WeatherService initialization"""
        service = WeatherService()
        assert service.geolocator is not None
        assert service.open_meteo_base_url == "https://api.open-meteo.com/v1/forecast"

    @patch('src.main.Nominatim')
    def test_get_coordinates_success(self, mock_nominatim, weather_service):
        """Test successful coordinate retrieval"""
        # Mock location object
        mock_location = Mock()
        mock_location.latitude = 51.5074
        mock_location.longitude = -0.1278
        
        # Mock geolocator
        mock_geolocator = Mock()
        mock_geolocator.geocode.return_value = mock_location
        mock_nominatim.return_value = mock_geolocator
        
        # Create fresh service with mocked geolocator
        service = WeatherService()
        lat, lon = service.get_coordinates("London")
        
        assert abs(lat - 51.5074) < 0.0001
        assert abs(lon - (-0.1278)) < 0.0001

    @patch('src.main.Nominatim')
    def test_get_coordinates_city_not_found(self, mock_nominatim, weather_service):
        """Test coordinate retrieval for non-existent city"""
        # Mock geolocator
        mock_geolocator = Mock()
        mock_geolocator.geocode.return_value = None
        mock_nominatim.return_value = mock_geolocator
        
        # Create fresh service with mocked geolocator
        service = WeatherService()
        
        with pytest.raises(ValueError, match="City 'NonExistentCity' not found"):
            service.get_coordinates("NonExistentCity")

    @patch('src.main.requests.get')
    def test_get_weather_success(self, mock_get, weather_service):
        """Test successful weather data retrieval"""
        # Mock successful API response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "current_weather": {
                "temperature": 15.2
            }
        }
        mock_get.return_value = mock_response
        
        temperature = weather_service.get_weather(51.5074, -0.1278)
        
        assert abs(temperature - 15.2) < 0.01
        mock_get.assert_called_once()

    @patch('src.main.requests.get')
    def test_get_weather_no_temperature_data(self, mock_get, weather_service):
        """Test weather retrieval when temperature data is missing"""
        # Mock API response without temperature
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "current_weather": {}
        }
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="Temperature data not available"):
            weather_service.get_weather(51.5074, -0.1278)

    @patch('src.main.requests.get')
    def test_get_weather_api_error(self, mock_get, weather_service):
        """Test weather retrieval when API returns an error"""
        # Mock API error
        mock_get.side_effect = requests.exceptions.RequestException("API Error")
        
        with pytest.raises(ValueError, match="Error fetching weather data"):
            weather_service.get_weather(51.5074, -0.1278)

    @patch.object(WeatherService, 'get_coordinates')
    @patch.object(WeatherService, 'get_weather')
    def test_get_city_temperature_success(self, mock_get_weather, mock_get_coordinates, weather_service):
        """Test successful city temperature retrieval"""
        # Mock the methods
        mock_get_coordinates.return_value = (51.5074, -0.1278)
        mock_get_weather.return_value = 15.2
        
        result = weather_service.get_city_temperature("London")
        
        expected = "15 Celsius now in London"
        
        assert result == expected
        mock_get_coordinates.assert_called_once_with("London")
        mock_get_weather.assert_called_once_with(51.5074, -0.1278)

    @patch.object(WeatherService, 'get_coordinates')
    def test_get_city_temperature_coordinate_error(self, mock_get_coordinates, weather_service):
        """Test city temperature retrieval when coordinates cannot be found"""
        # Mock coordinate error
        mock_get_coordinates.side_effect = ValueError("City not found")
        
        result = weather_service.get_city_temperature("NonExistentCity")
        assert "Error getting weather for 'NonExistentCity'" in result
        assert "City not found" in result

    @patch.object(WeatherService, 'get_weather')
    @patch.object(WeatherService, 'get_coordinates')
    def test_get_city_temperature_weather_error(self, mock_get_coordinates, mock_get_weather, weather_service):
        """Test city temperature retrieval when weather API fails"""
        # Mock successful coordinates but weather error
        mock_get_coordinates.return_value = (51.5074, -0.1278)
        mock_get_weather.side_effect = ValueError("Weather API error")
        
        result = weather_service.get_city_temperature("London")
        assert "Error getting weather for 'London'" in result
        assert "Weather API error" in result


if __name__ == "__main__":
    pytest.main([__file__])
