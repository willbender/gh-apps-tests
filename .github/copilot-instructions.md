# GitHub Copilot Instructions for Weather Service API

## Project Overview
This is a Python web service that provides weather information for cities using the Open-Meteo API. The service performs automatic geocoding to convert city names to coordinates and returns current temperature data via a REST API.

## Code Style Guidelines

### Python Standards
- Follow PEP 8 style guide strictly
- Use type hints for all function parameters and return values
- Include comprehensive docstrings for all public functions and classes
- Prefer explicit over implicit code
- Use meaningful variable and function names

### FastAPI Patterns
- Use dependency injection for shared services
- Implement proper HTTP status codes (200, 404, 500, etc.)
- Include response models using Pydantic
- Add comprehensive error handling with try/catch blocks
- Use async/await for I/O operations when possible

### Error Handling
- Always handle API failures gracefully
- Return meaningful error messages in JSON format
- Use appropriate HTTP status codes
- Log errors for debugging purposes
- Validate input parameters

## Architecture Guidelines

### API Design
- Follow RESTful principles
- Use descriptive endpoint names
- Include proper request/response documentation
- Implement health check endpoints
- Provide OpenAPI/Swagger documentation

### External Services
- **Weather Data**: Use Open-Meteo API (https://api.open-meteo.com)
- **Geocoding**: Use Nominatim via geopy library
- **HTTP Requests**: Prefer `requests` library for external API calls
- **Web Framework**: Use FastAPI for all web endpoints

### Data Flow
1. Receive city name from client
2. Geocode city to coordinates using Nominatim
3. Fetch weather data from Open-Meteo API using coordinates
4. Parse and return temperature data in JSON format

## Dependencies and Libraries
- **FastAPI**: Web framework for API endpoints
- **Uvicorn**: ASGI server for development and production
- **Requests**: HTTP client for external API calls
- **Geopy**: Geocoding library for city-to-coordinates conversion

## Testing Patterns
- Write unit tests for all business logic
- Mock external API calls in tests
- Test error scenarios and edge cases
- Include integration tests for complete workflows
- Test with various city names and formats

## Common Code Patterns

### Function Structure
```python
async def function_name(param: Type) -> ReturnType:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When this exception occurs
    """
    try:
        # Function implementation
        return result
    except SpecificException as e:
        # Handle specific errors
        raise HTTPException(status_code=400, detail="Error message")
```

### API Endpoint Structure
```python
@router.get("/endpoint/{param}")
async def endpoint_name(param: str) -> ResponseModel:
    """Endpoint description."""
    # Implementation
```

## Security Considerations
- Validate all input parameters
- Sanitize user inputs to prevent injection attacks
- Rate limit API endpoints to prevent abuse
- Don't expose internal error details to clients
- Use environment variables for configuration

## Performance Guidelines
- Cache geocoding results when possible
- Use async operations for I/O bound tasks
- Implement request timeouts for external API calls
- Consider pagination for large datasets
- Monitor API response times

## Naming Conventions
- Functions: `snake_case`
- Variables: `snake_case` 
- Constants: `UPPER_SNAKE_CASE`
- Classes: `PascalCase`
- API endpoints: `kebab-case` or `snake_case`

## Example Response Formats
```json
{
  "city": "London",
  "temperature": 15.2,
  "unit": "celsius",
  "timestamp": "2025-09-10T10:30:00Z"
}
```

## Common Utilities Needed
- Input validation functions
- Error response formatters
- Logging utilities
- Configuration management
- Health check implementations

## Documentation
- API documentation using OpenAPI/Swagger
- Check that README.md file remains consistent with code changes
- Don't generate other documentation files
- Maintain the diagrams in README.md up to date