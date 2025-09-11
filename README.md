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

### Option 1: Docker (Recommended)

The easiest way to run the Weather Service is using Docker with nginx as a reverse proxy:

```bash
# Build the Docker image
docker build -t weather-service:latest .

# Run the container
docker run -p 80:80 weather-service:latest
```

Or use docker-compose for easier management:

```bash
# Start the service
docker-compose up -d

# Stop the service
docker-compose down
```

The service will be available at `http://localhost` (port 80).

### Option 2: Local Development

1. Make sure you have Python 3.7+ installed
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Server

#### Docker Deployment

After building the Docker image:

```bash
# Using Docker directly
docker run -p 80:80 weather-service:latest

# Using docker-compose
docker-compose up -d
```

The server will start on `http://localhost` (port 80).

#### Local Development

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

#### Docker Deployment (port 80)

- Get weather for London: `http://localhost/weather/London`
- Get weather for New York: `http://localhost/weather/New York`
- Get weather for Tokyo: `http://localhost/weather/Tokyo`
- Health check: `http://localhost/health`
- API documentation: `http://localhost/docs`

#### Local Development (port 8000)

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

### Docker (port 80)

```bash
# Using curl
curl http://localhost/weather/London

# Using PowerShell
Invoke-RestMethod -Uri "http://localhost/weather/London"
```

### Local Python (port 8000)

```bash
# Using curl
curl http://localhost:8000/weather/London

# Using PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/weather/London"
```

## Architecture

The Weather Service API follows a layered architecture with clear separation of concerns:

```mermaid
graph TD
  A[Client Request] --> B[FastAPI Router]
  B --> C[Weather Service Layer]
  C --> D[Geocoding Service]
  C --> E[Weather API Client]
  
  D --> F[Nominatim API<br/>OpenStreetMap]
  E --> G[Open-Meteo API]
  
  F --> H[Coordinates Response]
  G --> I[Weather Data Response]
  
  H --> C
  I --> C
  C --> J[Response Formatter]
  J --> K[JSON Response]
  K --> B
  B --> L[Client Response]
  
  style A fill:#e1f5fe
  style L fill:#e8f5e8
  style F fill:#fff3e0
  style G fill:#fff3e0
  style C fill:#f3e5f5
```

### Component Overview

- **FastAPI Router**: Handles HTTP requests and routes them to appropriate handlers
- **Weather Service Layer**: Core business logic that orchestrates the weather lookup process  
- **Geocoding Service**: Converts city names to latitude/longitude coordinates using Nominatim
- **Weather API Client**: Fetches current weather data from Open-Meteo API
- **Response Formatter**: Formats the weather data into user-friendly JSON responses

### Data Flow

1. Client sends GET request to `/weather/{city_name}`
2. FastAPI routes the request to the weather service
3. Service calls geocoding to get coordinates for the city
4. Service uses coordinates to fetch weather data from Open-Meteo
5. Service formats the response and returns it to the client
6. Error handling occurs at each step with appropriate HTTP status codes
