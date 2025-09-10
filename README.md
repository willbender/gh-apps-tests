# Weather Service API

A Python webservice that provides weather information for cities using the Open-Meteo API.

## Features

- **City Weather Lookup**: Get current temperature for any city by name
- **Automatic Geocoding**: Converts city names to coordinates using Nominatim
- **Open-Meteo Integration**: Fetches weather data from the free Open-Meteo API
- **REST API**: FastAPI-based web service with automatic documentation
- **Error Handling**: Comprehensive error handling for invalid cities and API failures

## API Endpoints

- `GET /` - API information and available endpoints
- `GET /weather/{city_name}` - Get current temperature for a city
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)

## Installation

1. Make sure you have Python 3.7+ installed
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server

Option 1 - Development mode (with auto-reload):

```bash
python run_server.py
```

Option 2 - Simple mode:

```bash
python start_server.py
```

The server will start on `http://localhost:8000`

### API Examples

- Get weather for London: `http://localhost:8000/weather/London`
- Get weather for New York: `http://localhost:8000/weather/New York`
- Get weather for Tokyo: `http://localhost:8000/weather/Tokyo`

### Example Response

**Success Response:**

```json
{
  "city": "London",
  "result": "15 Celsius now in London"
}
```

**Error Response:**

```json
{
  "detail": "Error getting weather for 'InvalidCity': City 'InvalidCity' not found"
}
```

### Testing

Option 1 - Direct functionality test (no server needed):

```bash
python test_direct.py
```

Option 2 - Full API test (requires server to be running):

```bash
python test_service.py
```

Option 3 - Simple client usage:

```bash
python client.py London
python client.py "New York"
python client.py Tokyo
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **Requests**: HTTP library for API calls
- **Geopy**: Geocoding library for converting city names to coordinates

## API Documentation

Once the server is running, visit `http://localhost:8000/docs` for interactive API documentation.

## How It Works

1. **City Input**: User provides a city name via the API endpoint
2. **Geocoding**: The service uses Nominatim (OpenStreetMap) to convert the city name to latitude/longitude coordinates
3. **Weather API Call**: Using the coordinates, the service calls the Open-Meteo API to get current weather data
4. **Response Formatting**: The temperature is formatted as "{temperature} Celsius now in {city}"
5. **Error Handling**: If the city is not found or the weather data is unavailable, an appropriate error message is returned

## Example Usage from Command Line

```bash
# Using curl
curl http://localhost:8000/weather/London

# Using PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/weather/London"
```

Repository to contain some tests about gh apps
