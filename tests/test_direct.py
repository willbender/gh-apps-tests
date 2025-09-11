#!/usr/bin/env python3
"""
Direct test of the weather service functionality
"""
from src.main import WeatherService

def test_weather_functionality():
    """Test the weather service functionality directly"""
    weather_service = WeatherService()
    
    # Test cities
    test_cities = [
        "London",
        "New York",
        "Tokyo",
        "Paris",
        "Berlin",
        "InvalidCity123"  # This should fail
    ]
    
    print("Testing Weather Service Functionality...")
    print("=" * 60)
    
    for city in test_cities:
        print(f"\nTesting city: {city}")
        print("-" * 30)
        
        try:
            result = weather_service.get_city_temperature(city)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_weather_functionality()
