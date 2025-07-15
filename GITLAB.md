# 🔐 GitLab DevSecOps Security Assignment

## 📘 Overview

This project demonstrates the use of **GitLab as a DevSecOps platform** by leveraging its built-in security capabilities such as **SAST**, **Secret Detection**, and **Secret Push Protection**. The goal is to integrate security early in the development pipeline, ensuring vulnerabilities are identified and resolved before production deployment.

---

## 🎯 Objective

- Understand GitLab's native security tools and configurations.
- Perform Proof of Concepts (PoCs) for:
  - Static Application Security Testing (SAST)
  - Secret Detection
  - Secret Push Protection
- Document findings with screenshots, configurations, and recommendations.

---

## 📁 Repository Structure

- **Group:** `anirudhdeshmukh-group`
- **Repository Name:** `gitlab_assignment`
- **Branches Used:** `main`, `gitlab-assignment`
- **Application:** Sample Python app with intentional security flaws (e.g., hardcoded secrets, vulnerable libraries).
- **Author:** Anirudh Deshmukh

---

## 🔧 GitLab as a DevSecOps Platform

GitLab offers a unified DevSecOps experience with all key SDLC tools — source control, CI/CD, security scanning, and monitoring — available in a single interface. This tight integration accelerates secure software delivery and simplifies DevOps workflows.

### 🚀 Key Security Features

| Feature                | Purpose                                                       |
|------------------------|---------------------------------------------------------------|
| **SAST**               | Scan code for static vulnerabilities (e.g., SQLi, XSS).       |
| **DAST**               | Test live applications for runtime security issues.           |
| **Secret Detection**   | Identify exposed credentials, API keys, and tokens.           |
| **Dependency Scanning**| Detect vulnerable packages in dependency files.               |
| **Container Scanning** | Identify CVEs in Docker images.                               |
| **Fuzz Testing**       | Find bugs using random or malformed input.                    |
| **License Compliance** | Detect use of restricted or vulnerable licenses.              |

---

## ⚙️ CI/CD Integration

Security scanners are easily added using `.gitlab-ci.yml`.  
Example configuration:

```yaml
include:
  - template: Security/SAST.gitlab-ci.yml
  - template: Security/Secret-Detection.gitlab-ci.yml

stages:
  - test
  - secret-detection

sast:
  stage: test

secret_detection:
  stage: secret-detection
