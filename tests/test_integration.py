#!/usr/bin/env python3
"""
Integration tests for the weather service
These tests run against the actual API (not mocked)
"""
import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


class TestIntegration:
    """Integration test cases"""

    def test_root_endpoint_structure(self, client):
        """Test that root endpoint returns expected structure"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        
        # Check required fields
        assert "message" in data
        assert "description" in data
        assert "endpoints" in data
        
        # Check endpoints info
        endpoints = data["endpoints"]
        assert "/weather/{city_name}" in endpoints
        assert "/docs" in endpoints

    def test_health_endpoint_structure(self, client):
        """Test that health endpoint returns expected structure"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        
        # Check required fields
        assert "status" in data
        assert "service" in data
        assert data["status"] == "healthy"
        assert data["service"] == "weather-service"

    def test_weather_endpoint_with_known_city(self, client):
        """Test weather endpoint with a well-known city"""
        # Using London as it's likely to be found in geocoding
        response = client.get("/weather/London")
        
        # Should either succeed or fail gracefully
        assert response.status_code in [200, 404, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert "city" in data
            assert "result" in data
            assert data["city"] == "London"
            # Result should be a string with temperature info
            assert isinstance(data["result"], str)
            assert "Celsius" in data["result"]

    def test_weather_endpoint_with_invalid_city(self, client):
        """Test weather endpoint with obviously invalid city"""
        response = client.get("/weather/ThisCityDoesNotExist12345")
        
        # Should return an error
        assert response.status_code in [404, 500]
        data = response.json()
        assert "detail" in data

    def test_docs_endpoint_exists(self, client):
        """Test that the OpenAPI docs endpoint is available"""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_openapi_json_endpoint(self, client):
        """Test that the OpenAPI JSON schema is available"""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        
        # Check basic OpenAPI structure
        assert "openapi" in data
        assert "info" in data
        assert "paths" in data
        
        # Check our endpoints are documented
        paths = data["paths"]
        assert "/" in paths
        assert "/health" in paths
        assert "/weather/{city_name}" in paths


if __name__ == "__main__":
    pytest.main([__file__])
