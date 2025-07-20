# Image Scanning with Trivy

## Overview

This document outlines the process of integrating **Trivy** container image scanning into the CI/CD pipeline for a Python application. The goal is to automatically identify vulnerabilities in Docker images during the build process using GitHub Actions.

---

## Repository Structure

- **Repository Name:** DevSecOps-Assignment
- **Branch:** `imagescan-assignment`
- **Application:** Python Flask app with intentional vulnerabilities
- **Key Files:**
  - `Dockerfile`
  - `requirements.txt`
  - `src/test_app/main.py`
  - `.github/workflows/imagescan.yml`

---

## Tool Used

- **Container Scanner:** [Trivy by Aqua Security](https://github.com/aquasecurity/trivy)
- **Why Trivy:** Open-source, supports both OS and language-level vulnerability scanning, lightweight, supports local and CI/CD usage, exports standard formats like JSON and SARIF.

---

## Setup Instructions

1. **Ensure your project contains a valid Dockerfile.**

2. **No authentication required** for public image scanning or basic usage. For advanced integrations (like GitHub Security Dashboard), you may configure GitHub SARIF uploads.

3. **Configure the GitHub Actions workflow** under `.github/workflows/imagescan.yml`.

---

## CI/CD Integration

The pipeline performs the following steps:

1. Checks out the repository
2. Builds the Docker image from the `Dockerfile`
3. Scans the image with Trivy
4. Generates:
   - `trivy-report.json`
   - `trivy-report.sarif`
5. Uploads both reports as GitHub Actions artifacts

---

## Vulnerability Report Artifacts

| File                | Format  | Description                                      |
|---------------------|---------|--------------------------------------------------|
| `trivy-report.json` | JSON    | Machine-readable vulnerability report            |
| `trivy-report.sarif`| SARIF   | Compatible with GitHub Security dashboard        |

---

## Sample Findings Summary

| Severity  | Count | Example                              |
|-----------|-------|--------------------------------------|
| Critical  | 1     | OpenSSL vulnerable version            |
| High      | 3     | Outdated `urllib3` in dependencies    |
| Medium    | 5     | Use of legacy image base              |
| Low       | 8     | General security warnings             |

---

## Recommendations

- Use secure base images like `python:3.13-slim` or `python:3.11-alpine`
- Remove unnecessary packages and clear APT cache
- Keep `requirements.txt` dependencies up to date
- Continuously scan images in CI and pre-deployment stages using Trivy

---

## References

- [Trivy GitHub Repository](https://github.com/aquasecurity/trivy)
- [Trivy Docs](https://aquasecurity.github.io/trivy/)
- [Trivy GitHub Action](https://github.com/aquasecurity/trivy-action)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
