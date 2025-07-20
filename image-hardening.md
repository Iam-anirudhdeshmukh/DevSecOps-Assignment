# Image Hardening with Docker Best Practices

## Overview

This document outlines the process of hardening Docker container images for a Python web application. The goal is to reduce the attack surface, enforce least privilege, and follow secure image-building practices using multi-stage builds, non-root users, and minimal base images.

---

## Repository Structure

- **Repository Name:** DevSecOps-Assignment  
- **Branch:** `imagehardening-assignment`  
- **Application:** Python Flask app with intentional vulnerabilities  
- **Key Files:**
  - `Dockerfile` (hardened)
  - `requirements.txt`
  - `src/test_app/main.py`
  - `.github/workflows/image-hardening.yaml`

---

## Security Techniques Used

- **Minimal Base Image:** `python:3.11-alpine`  
- **Multi-stage Builds:** Isolate build-time dependencies from runtime  
- **Non-root User:** UID 1001, GID 1001 (`appuser`)  
- **File Permissions:** Restricted access (`chmod -R 750`)  
- **Layer Minimization:** Combined `RUN` steps  
- **COPY Instead of ADD:** Avoided security risks from remote file fetch  
- **No Hardcoded Secrets:** Uses environment variables instead  
- **Root Filesystem (Optional):** Recommend using `--read-only` during runtime  
- **Linux Capabilities:** Can run with `--cap-drop=ALL`

---

## Setup Instructions

1. Ensure your project includes a secure and valid Dockerfile.
2. Use the provided `image-hardening.yaml` GitHub Actions workflow to build and validate the hardened image.
3. Test the image locally or via CI to ensure it runs as a non-root user and enforces file restrictions.

---

## CI/CD Integration

The GitHub Actions workflow performs the following:

1. Checks out code
2. Builds hardened Docker image
3. Verifies container runs as non-root
4. Optionally pushes the image to Docker Hub

---

## Hardened Dockerfile Summary

```dockerfile
FROM python:3.11-alpine AS build
RUN apk add --no-cache build-base libffi-dev openssl-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM python:3.11-alpine
RUN addgroup -g 1001 appgroup && adduser -u 1001 -G appgroup -D appuser
WORKDIR /app
COPY --from=build /app /app
RUN chown -R appuser:appgroup /app && chmod -R 750 /app
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
