# 🛡️ Shift Left Security in CI/CD Pipeline

## 📘 Overview

This project implements **Shift Left Security** by integrating automated security checks into the CI/CD pipeline using **GitHub Actions**. Security testing is executed during development (on PRs and commits) to ensure vulnerabilities are caught **before** reaching production.

---

## 🧰 Security Tools Implemented

| Check Type                         | Tool Used                        | Description                                                                 |
|-----------------------------------|----------------------------------|-----------------------------------------------------------------------------|
| Static Application Security Testing (SAST) | [CodeQL](https://codeql.github.com/)       | Analyzes code for vulnerabilities like SQL Injection, XSS, etc.             |
| Dependency Scanning               | [Trivy](https://github.com/aquasecurity/trivy) | Scans for known vulnerabilities (CVEs) in package dependencies              |
| Code Linting with Security Rules  | ESLint + eslint-plugin-security | Detects insecure code patterns and enforces best practices                  |
| Secret Scanning                   | [Gitleaks](https://github.com/gitleaks/gitleaks) | Finds hardcoded secrets like API keys and credentials                      |
| Container Image Scanning          | Trivy (Image Mode)               | Scans Docker images for OS-level and application-level CVEs                |

---

## ⚙️ Configuration Summary

The pipeline is defined in:

```bash
.github/workflows/security.yml

--

Trigger Conditions:
✅ On push to main

✅ On pull request to main or security-pipeline

✅ On a weekly schedule: 0 0 * * 0 (every Sunday at midnight UTC)

Jobs Included:


| Job               | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `codeql-analysis` | Scans application code for vulnerabilities using GitHub CodeQL  |
| `dependency-scan` | Uses Trivy to identify CVEs in package dependencies (e.g., NPM) |
| `eslint-linting`  | Lints JavaScript files using ESLint and security plugin         |
| `secret-scan`     | Runs Gitleaks to find hardcoded credentials                     |
| `container-scan`  | Builds and scans Docker image using Trivy                       |

🧠 Rationale for Tool Selection

| Tool     | Why It Was Chosen                                                       |
| -------- | ----------------------------------------------------------------------- |
| CodeQL   | Built-in GitHub tool with wide language support and deep query engine   |
| Trivy    | Fast and comprehensive for both dependencies and containers             |
| ESLint   | Integrates easily with JS codebases and helps enforce secure code style |
| Gitleaks | Battle-tested secret scanner that runs on commits, branches, and files  |
