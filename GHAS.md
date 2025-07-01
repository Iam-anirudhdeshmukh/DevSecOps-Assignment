# GitHub Advanced Security (GHAS) – Implementation & Scan Report

## 📘 Repository Details

- **Repository**: DevSecOps-Assignment  
- **Owner**: @Iam-anirudhdeshmukh  
- **Primary Language**: Python  
- **Branch**: `main`

---

## ✅ Enabled GHAS Features

| Feature                      | Status   |
|-----------------------------|----------|
| Security Policy (`SECURITY.md`) | ✅ Enabled |
| Security Advisory           | ✅ Enabled |
| Private Vulnerability Reporting | ✅ Enabled |
| Dependabot Alerts           | ✅ Enabled |
| Code Scanning (CodeQL)      | ✅ Enabled |
| Secret Scanning             | ✅ Enabled |

---

## ⚙️ CI Configuration

### 1. `.github/workflows/codeql.yml`
- **Tool**: CodeQL (GitHub-native SAST)
- **Scope**: Python source code
- **Trigger**: On push to `main` and on pull requests
- **Goal**: Detect potential vulnerabilities (e.g., unsanitized input, command injection)

### 2. `.github/dependabot.yml`
- **Tool**: Dependabot
- **Monitored files**: `requirements.txt`
- **Package ecosystem**: `pip`
- **Security Alert Behavior**: Alerts enabled in Security tab, PRs are not auto-raised

---

## 🔍 Scan Results Summary

### 🧪 1. CodeQL Scan Findings

| Issue | File | Severity | Suggested Fix |
|-------|------|----------|----------------|
| Shell injection (unsanitized input to `os.system`) | `scripts/scan.py` | 🚨 Critical | Use `subprocess.run()` with validated arguments |
| Unsafe use of `eval()` | `main.py` | 🚨 Critical | Remove or replace with safe parsing logic |
| Insecure file access (no input validation) | `config_loader.py` | ⚠️ High | Sanitize and validate file paths |

---

### 📦 2. Dependency Vulnerabilities (Dependabot)

| Package | Current Version | Vulnerability | Severity | Suggested Fix |
|---------|------------------|---------------|----------|----------------|
| Flask   | 1.0              | CVE-2019-1010083 | 🔥 High | Upgrade to `Flask>=2.3.0` |
| PyYAML  | 5.1              | CVE-2020-14343 | 🔥 High | Upgrade to `PyYAML>=5.4` |

---

### 🔐 3. Secret Scanning Alerts

| Type | Location | Status | Recommendation |
|------|----------|--------|----------------|
| Hardcoded API Key | `config.py` | ❗ Found | Move to `.env` and load via `os.environ` |
| GitHub Token Pattern | `.env.backup` (committed) | ❗ Found | Revoke token and remove file from repo |

---

## 🧹 Fixes Applied

- ✅ Replaced `os.system()` with `subprocess.run()` using sanitized inputs
- ✅ Upgraded vulnerable dependencies as per Dependabot suggestions
- ✅ Removed `.env.backup` and revoked exposed GitHub token
- ✅ Added `.env` file to `.gitignore`
- ✅ Created `SECURITY.md` with responsible disclosure instructions

---

## 📸 Screenshots / Logs

> *Include these in the repo or attach to your assignment submission.*

- 🔐 Security tab overview  
- 📊 Code Scanning Alerts with details  
- 📦 Dependabot Alert screenshots  
- 🔍 Secret Scanning alerts

---

## 📝 Recommendations

- **Avoid hardcoding secrets** in source code; use GitHub Secrets or `.env` files excluded via `.gitignore`
- **Patch known CVEs** quickly by upgrading flagged dependencies
- **Use SAST tools** like CodeQL on all pull requests to block insecure code
- **Enable branch protection rules** that require passing CodeQL & secret scan checks before merging

---

## ✅ Conclusion

GitHub Advanced Security (GHAS) significantly improved the security visibility of this repository by detecting:

- Source code vulnerabilities
- Insecure third-party dependencies
- Hardcoded sensitive data

By integrating security scans directly into GitHub workflows, we ensure all future changes meet basic security standards before reaching production.

**Shift Left. Scan Early. Stay Secure.**

