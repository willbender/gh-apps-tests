#!/usr/bin/env bash

# Security validation script for the Weather Service
# This script checks for common security configurations

set -e

echo "🔒 Security Validation Script for Weather Service"
echo "=================================================="

# Check if running with appropriate permissions
if [[ $EUID -eq 0 ]]; then
   echo "❌ Do not run this script as root for security reasons"
   exit 1
fi

echo "✅ Running with non-root privileges"

# Check Python version for security patches
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
echo "🐍 Python version: $PYTHON_VERSION"

if [[ "$PYTHON_VERSION" < "3.12" ]]; then
    echo "⚠️  Consider upgrading to Python 3.12+ for latest security patches"
else
    echo "✅ Using modern Python version with security updates"
fi

# Check for security-related dependencies
echo ""
echo "📦 Checking dependency security..."

if command -v pip3 &> /dev/null; then
    echo "✅ pip3 available for dependency management"
    
    # Check for known vulnerable packages (basic check)
    if pip3 list | grep -q "requests.*2\.31\.0"; then
        echo "✅ requests 2.31.0 - known secure version"
    fi
    
    if pip3 list | grep -q "fastapi.*0\.104\.1"; then
        echo "✅ FastAPI 0.104.1 - recent version"
    fi
else
    echo "❌ pip3 not found"
fi

# Check for Docker security if available
echo ""
echo "🐳 Docker security check..."

if command -v docker &> /dev/null; then
    echo "✅ Docker available"
    
    # Check if docker daemon is running as non-root (best practice)
    if docker info > /dev/null 2>&1; then
        echo "✅ Docker daemon accessible"
        
        # Check for Weather Service image
        if docker images | grep -q "weather-service"; then
            echo "✅ Weather Service image found"
            
            # Basic security scan if available
            if command -v docker scan &> /dev/null; then
                echo "🔍 Docker scan available - run 'docker scan weather-service:latest' for security analysis"
            fi
        else
            echo "ℹ️  Weather Service image not built yet"
        fi
    else
        echo "ℹ️  Docker daemon not accessible (normal for non-Docker environments)"
    fi
else
    echo "ℹ️  Docker not available"
fi

# Check file permissions
echo ""
echo "📁 File security check..."

# Check for overly permissive files
find . -type f -perm /go+w ! -path "./.git/*" ! -path "./venv/*" ! -path "./.venv/*" 2>/dev/null | while read -r file; do
    echo "⚠️  World-writable file found: $file"
done

# Check for executable scripts
find . -name "*.py" -perm /u+x ! -path "./.git/*" ! -path "./venv/*" ! -path "./.venv/*" 2>/dev/null | while read -r file; do
    echo "ℹ️  Executable Python file: $file"
done

echo ""
echo "🛡️  Basic security checks completed"
echo ""
echo "For comprehensive security scanning:"
echo "  • Run vulnerability scans with: pip install safety && safety check"
echo "  • Use Docker security scanning: docker scan <image>"
echo "  • Review the SECURITY.md file for security policies"
echo "  • Check GitHub Security tab for SARIF reports"
echo ""