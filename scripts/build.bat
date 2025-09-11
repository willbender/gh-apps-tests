@echo off
REM Build and run the Weather Service Docker container

echo Building Weather Service Docker image...
cd /d "%~dp0\.."
docker build -f docker/Dockerfile -t weather-service:latest .

if %ERRORLEVEL% neq 0 (
    echo Build failed!
    exit /b %ERRORLEVEL%
)

echo Build completed successfully!
echo.
echo To run the container:
echo   docker run -p 80:80 weather-service:latest
echo.
echo Or use docker-compose:
echo   cd docker ^&^& docker-compose up -d
echo.
echo The service will be available at:
echo   - API: http://localhost/
echo   - Health check: http://localhost/health
echo   - API docs: http://localhost/docs
echo   - Example: http://localhost/weather/London
