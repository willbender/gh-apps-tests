# Project Structure

This project has been organized into a clean directory structure:

```
simple-weather-app/
├── src/                    # Main application code
│   ├── __init__.py        # Package initialization
│   ├── main.py           # FastAPI application and WeatherService
│   ├── client.py         # Client for testing the API
│   ├── run_server.py     # Server runner script
│   └── start_server.py   # Server startup script
├── tests/                 # Test files
│   ├── __init__.py       # Test package initialization
│   ├── test_direct.py    # Direct API tests
│   └── test_service.py   # Service integration tests
├── docker/               # Docker configuration
│   ├── Dockerfile        # Docker build instructions
│   ├── docker-compose.yml # Docker Compose configuration
│   ├── nginx.conf        # Nginx reverse proxy configuration
│   └── supervisord.conf  # Supervisor process manager configuration
├── scripts/              # Build and utility scripts
│   ├── build.sh         # Linux/macOS build script
│   ├── build.bat        # Windows build script
│   ├── start.sh         # Linux/macOS startup script
│   └── start.bat        # Windows startup script
├── pyproject.toml       # Python project configuration
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── LICENSE             # License file
```

## How to Use

### Running the Application

#### Using Python directly:
```bash
# From project root
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000

# Or use the startup scripts:
# Linux/macOS:
./scripts/start.sh

# Windows:
scripts\start.bat
```

#### Using Docker:
```bash
# Build the image
./scripts/build.sh        # Linux/macOS
scripts\build.bat         # Windows

# Or manually:
docker build -f docker/Dockerfile -t weather-service:latest .

# Run with docker-compose
cd docker && docker-compose up -d
```

### Running Tests

```bash
# From project root
pytest tests/

# Or run specific test files
pytest tests/test_direct.py
pytest tests/test_service.py
```

### Development

The project uses a `src/` layout which is a Python packaging best practice. This structure:

- Keeps source code separate from tests and configuration
- Makes packaging and distribution easier
- Prevents accidental imports of source code during testing
- Provides a cleaner project organization

All Docker configurations are in the `docker/` directory, and build scripts are in `scripts/` for easy maintenance and organization.
