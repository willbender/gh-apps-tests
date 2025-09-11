#!/usr/bin/env python3
"""
Simple startup script for the weather service
"""
import uvicorn

if __name__ == "__main__":
    print("Starting Weather Service...")
    print("API will be available at: http://localhost:8000")
    print("API documentation at: http://localhost:8000/docs")
    print("Example usage: http://localhost:8000/weather/London")
    print("\nPress Ctrl+C to stop the server")
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info"
    )
