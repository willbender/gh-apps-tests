# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.25.x  | :white_check_mark: |
| 1.24.x  | :white_check_mark: |
| < 1.24  | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please report it to us through:

1. **GitHub Security Advisories** (preferred): Go to the Security tab and click "Report a vulnerability"
2. **Email**: [security@weatherservice.com](mailto:security@weatherservice.com)

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

## Security Measures

### Automated Security Scanning

Our CI/CD pipeline includes comprehensive security scanning:

- **Container Image Scanning**: Trivy scans every Docker image for known vulnerabilities
- **Dependency Scanning**: Python dependencies are analyzed for security issues
- **SARIF Integration**: Results are uploaded to GitHub's Security tab for monitoring
- **Vulnerability Reports**: HTML reports are attached to each release

### Security Updates

- Security patches are prioritized and released as soon as possible
- Critical vulnerabilities trigger immediate patch releases
- All releases include updated vulnerability reports

### Base Image Security

- We use the latest Python Docker images with security patches
- Base images are regularly updated to address system-level vulnerabilities
- Multi-stage builds minimize attack surface

### Best Practices

- Non-root user execution in containers
- Minimal package installation
- Regular dependency updates
- Comprehensive test coverage

## Vulnerability Response Process

1. **Detection**: Automated scanning identifies vulnerabilities
2. **Assessment**: Security team evaluates impact and priority
3. **Patching**: Fixes are developed and tested
4. **Release**: Security updates are deployed immediately
5. **Communication**: Users are notified of security updates

## Security Configuration

For secure deployment:

```yaml
# docker-compose.yml security settings
security_opt:
  - no-new-privileges:true
read_only: true
tmpfs:
  - /tmp
  - /var/tmp
```

## Contact

For security-related questions or concerns:
- GitHub Issues: [Security label](https://github.com/willbender/simple-weather-app/issues?q=label%3Asecurity)
- Security Team: [security@weatherservice.com](mailto:security@weatherservice.com)