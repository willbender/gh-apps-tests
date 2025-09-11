#!/bin/bash
# Startup script for the weather service

# Change to the project root directory
cd "$(dirname "$0")/.."

# Run the weather service from the src directory
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --log-level info
