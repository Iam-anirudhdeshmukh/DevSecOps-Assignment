# Image Scanning with Snyk

## Overview

This document outlines the process of integrating Snyk container image scanning into the CI/CD pipeline for a Python application. The goal is to automatically identify vulnerabilities in Docker images during the build process using GitHub Actions.

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

- **Container Scanner:** [Snyk CLI](https://docs.snyk.io/)
- **Why Snyk:** Supports both OS-level and language-specific scans, integrates easily with GitHub Actions, exports standard formats like JSON and SARIF.

---

## Setup Instructions

1. **Ensure your project contains a valid Dockerfile.**

2. **Store the following GitHub secrets:**
   - `SNYK_TOKEN`: API token from [Snyk.io](https://app.snyk.io/account)

3. **Configure the GitHub Actions workflow** under `.github/workflows/imagescan.yml`.

---

## CI/CD Integration

The pipeline performs the following steps:

1. Checks out the repository
2. Builds the Docker image from the `Dockerfile`
3. Scans the image with Snyk
4. Generates:
   - `snyk-report.json`
   - `snyk-report.sarif`
5. Uploads both reports as GitHub Actions artifacts

---

## Vulnerability Report Artifacts

| File                | Format  | Description                                      |
|---------------------|---------|--------------------------------------------------|
| `snyk-report.json`  | JSON    | Machine-readable vulnerability report            |
| `snyk-report.sarif` | SARIF   | Compatible with GitHub Security dashboard        |

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
- Continuously monitor with `snyk monitor`

---

## References

- [Snyk Container Scanning Docs](https://docs.snyk.io/product/snyk-container)
- [Snyk GitHub Action](https://github.com/snyk/actions)
- [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
