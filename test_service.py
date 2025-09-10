#!/usr/bin/env python3
"""
Test script for the weather service
"""
import requests
import time

def test_weather_service():
    """Test the weather service with various cities"""
    base_url = "http://localhost:8000"
    
    # Test cities
    test_cities = [
        "London",
        "New York",
        "Tokyo",
        "Paris",
        "Berlin",
        "NonExistentCity123"  # This should fail
    ]
    
    print("Testing Weather Service...")
    print("=" * 50)
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"Root endpoint: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
        return
    
    # Test weather endpoints
    for city in test_cities:
        try:
            print(f"Testing city: {city}")
            response = requests.get(f"{base_url}/weather/{city}")
            
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Success: {data['result']}")
            else:
                print(f"✗ Error ({response.status_code}): {response.json().get('detail', 'Unknown error')}")
            
            print("-" * 30)
            time.sleep(1)  # Be nice to the APIs
            
        except Exception as e:
            print(f"✗ Error testing {city}: {e}")
            print("-" * 30)

if __name__ == "__main__":
    print("Make sure the weather service is running on http://localhost:8000")
    print("You can start it with: python run_server.py")
    print()
    
    input("Press Enter to start testing...")
    test_weather_service()
