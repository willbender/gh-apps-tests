#!/usr/bin/env python3
"""
Simple client to demonstrate the weather service
"""
import requests
import sys

def get_weather(city_name):
    """Get weather for a city"""
    try:
        url = f"http://localhost:8000/weather/{city_name}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data['result']
        else:
            error_data = response.json()
            return f"Error: {error_data.get('detail', 'Unknown error')}"
    
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to weather service. Make sure it's running on http://localhost:8000"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <city_name>")
        print("Example: python client.py London")
        return
    
    city_name = sys.argv[1]
    result = get_weather(city_name)
    print(result)

if __name__ == "__main__":
    main()
