from fastapi import FastAPI, HTTPException
import requests
from geopy.geocoders import Nominatim
from typing import Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Weather Service", description="Get weather information for cities using Open-Meteo API")

class WeatherService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="weather-service")
        self.open_meteo_base_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_coordinates(self, city_name: str) -> tuple:
        """Convert city name to coordinates (latitude, longitude)"""
        try:
            location = self.geolocator.geocode(city_name)
            if location:
                return location.latitude, location.longitude
            else:
                raise ValueError(f"City '{city_name}' not found")
        except Exception as e:
            logger.error(f"Error getting coordinates for {city_name}: {str(e)}")
            raise ValueError(f"Error finding coordinates for city '{city_name}': {str(e)}")
    
    def get_weather(self, latitude: float, longitude: float) -> float:
        """Get current temperature from Open-Meteo API"""
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current_weather": "true",
                "temperature_unit": "celsius"
            }
            
            response = requests.get(self.open_meteo_base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            current_weather = data.get("current_weather", {})
            temperature = current_weather.get("temperature")
            
            if temperature is None:
                raise ValueError("Temperature data not available")
            
            return temperature
        except requests.RequestException as e:
            logger.error(f"Error calling Open-Meteo API: {str(e)}")
            raise ValueError(f"Error fetching weather data: {str(e)}")
        except Exception as e:
            logger.error(f"Error processing weather data: {str(e)}")
            raise ValueError(f"Error processing weather data: {str(e)}")
    
    def get_city_temperature(self, city_name: str) -> str:
        """Get temperature for a city and return formatted string"""
        try:
            # Get coordinates
            latitude, longitude = self.get_coordinates(city_name)
            logger.info(f"Found coordinates for {city_name}: {latitude}, {longitude}")
            
            # Get weather
            temperature = self.get_weather(latitude, longitude)
            
            # Format response
            return f"{temperature:.0f} Celsius now in {city_name}"
        
        except Exception as e:
            error_message = f"Error getting weather for '{city_name}': {str(e)}"
            logger.error(error_message)
            return error_message

# Initialize weather service
weather_service = WeatherService()

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Weather Service API",
        "description": "Get weather information for cities",
        "endpoints": {
            "/weather/{city_name}": "Get current temperature for a city",
            "/docs": "API documentation"
        }
    }

@app.get("/weather/{city_name}")
async def get_weather(city_name: str) -> Dict[str, str]:
    """Get current temperature for a specified city"""
    try:
        result = weather_service.get_city_temperature(city_name)
        
        # Check if result is an error message
        if result.startswith("Error"):
            raise HTTPException(status_code=404, detail=result)
        
        return {
            "city": city_name,
            "result": result
        }
    
    except HTTPException:
        raise
    except Exception as e:
        error_message = f"Error getting weather for '{city_name}': {str(e)}"
        logger.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "weather-service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
