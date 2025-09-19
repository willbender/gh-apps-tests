# Multi-stage build for Weather Service with nginx

# Stage 1: Build the Python application
FROM python:3.12-alpine AS python-app

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/main.py .
COPY src/run_server.py .

# Create non-root user for security
RUN adduser -D -s /bin/sh app && chown -R app:app /app
USER app

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Command to run the application
CMD ["python", "-c", "import uvicorn; from main import app; uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info')"]

# Stage 2: nginx reverse proxy
FROM nginx:alpine AS nginx-proxy

# Remove default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy nginx configuration
COPY docker/nginx.conf /etc/nginx/conf.d/

# Expose port 80
EXPOSE 80

# Stage 3: Final multi-service container
FROM python:3.12-slim

# Add security and maintenance labels
LABEL maintainer="Weather Service Team <team@weatherservice.com>"
LABEL org.opencontainers.image.title="Simple Weather App"
LABEL org.opencontainers.image.description="A Python web service for weather information"
LABEL org.opencontainers.image.version="1.25.0"
LABEL org.opencontainers.image.source="https://github.com/willbender/simple-weather-app"
LABEL org.opencontainers.image.licenses="MIT"
LABEL security.scan="trivy"

# Install nginx and supervisor to manage multiple processes
RUN apt-get update && apt-get install -y \
    gcc \
    nginx \
    supervisor \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/main.py .
COPY src/run_server.py .

# Copy nginx configuration
COPY docker/nginx.conf /etc/nginx/sites-available/default

# Copy supervisor configuration  
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create non-root user for the app and set up nginx configuration
RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app && \
    rm -f /etc/nginx/sites-enabled/default && \
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/ && \
    mkdir -p /var/log/nginx /var/lib/nginx /var/log/supervisor /run && \
    chown -R www-data:www-data /var/log/nginx /var/lib/nginx && \
    chmod 755 /var/log/nginx

# Expose port 80 (nginx)
EXPOSE 80

# Use supervisor to run both nginx and the Python app
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
