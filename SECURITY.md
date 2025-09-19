# Security Policy

## Supported Versions

We actively maintain security for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.21.x  | :white_check_mark: |
| 1.20.x  | :white_check_mark: |
| < 1.20  | :x:                |

## Security Features

### Container Security

- **Base Image**: Uses Python 3.12-slim (latest LTS) for security patches
- **Multi-stage Builds**: Reduces final image size and attack surface
- **Non-root User**: Application runs as unprivileged user
- **Package Cleanup**: Removes build dependencies and caches to minimize vulnerabilities
- **Updated Components**: nginx 1.26-alpine and latest Python packages

### Automated Security Scanning

- **Trivy Integration**: Comprehensive vulnerability scanning on every build
- **Fail-Fast Security**: Builds automatically fail on CRITICAL or HIGH vulnerabilities
- **SARIF Reports**: Security findings integrated into GitHub Security tab
- **Release Scanning**: Additional security verification on release builds

### CI/CD Security

- **Dependency Scanning**: Python packages analyzed for known vulnerabilities  
- **Container Scanning**: Docker images scanned before publication
- **Automated Updates**: Security patches applied through CI/CD pipeline
- **Artifact Security**: Vulnerability reports stored for audit trails

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Email security concerns to: [security@weatherservice.com]
3. Include detailed steps to reproduce the vulnerability
4. Provide any relevant logs or evidence

### Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial Assessment**: Within 1 week
- **Fix Development**: Depends on severity (Critical: 24-48 hours, High: 1 week)
- **Release**: Security patches released as soon as testing is complete

### Disclosure Policy

- We follow responsible disclosure practices
- Security advisories published after fixes are deployed
- Credit given to reporters (unless anonymity requested)

## Security Best Practices

### For Users

- Always use the latest released version
- Monitor security advisories and update promptly
- Use official images from `ghcr.io/willbender/simple-weather-app`
- Review vulnerability scan reports in GitHub Security tab

### For Developers

- All dependencies must pass security scans
- Follow secure coding practices per project guidelines
- Run local security tests before submitting PRs
- Keep development dependencies updated

## Security Monitoring

- Automated daily security scans via GitHub Actions
- Dependency vulnerability tracking with Dependabot
- Container vulnerability monitoring with Trivy
- Manual security reviews for major releases

## Compliance

This project follows:

- OWASP security guidelines for web applications
- Docker security best practices
- Python security recommendations
- Container security standards (CIS Benchmarks)

---

Last updated: January 2025