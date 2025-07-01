# 🔐 Python Security Pipeline with GitHub Actions

This project implements a **Shift Left Security** pipeline to detect vulnerabilities, insecure code, secrets, and risky dependencies in a Python project — all during development, using GitHub Actions.

---

## ✅ When It Runs

The security pipeline runs automatically:

- On push to `main` or `security-pipeline` branches
- On pull request to the above branches
- Weekly every **Sunday at 00:00 UTC** (optional via cron)

---

## 🔍 Security Checks Implemented

| Check Type                 | Tool Used             | Purpose                                                            |
|----------------------------|------------------------|--------------------------------------------------------------------|
| Static Code Analysis       | CodeQL                 | Detect code-level issues like injection, deserialization flaws     |
| Dependency Scanning        | Trivy (Filesystem)     | Find CVEs in Python packages from `requirements.txt`               |
| Secure Code Linting        | Bandit                 | Flag insecure Python patterns (`eval`, `subprocess`, etc.)         |
| Secret Scanning            | Gitleaks               | Catch hardcoded secrets like passwords and API keys                |
| Docker Image Scanning      | Trivy (Image Scanner)  | Identify vulnerabilities in container image layers and libraries   |

---

## 🧪 1. Static Code Analysis (CodeQL)

- **Tool:** [GitHub CodeQL](https://github.com/github/codeql-action)
- **Language:** Python

CodeQL analyzes the Python codebase for security vulnerabilities like:
- Insecure crypto
- Command injection
- Unsafe YAML loading

📄 Output:
- SARIF report: `results/python.sarif`  
  (Visible in the GitHub **Security → Code scanning alerts** tab)

---

## 📦 2. Dependency Scanning (Trivy)

- **Tool:** [Trivy](https://github.com/aquasecurity/trivy)
- **Targets:** `requirements.txt` and installed packages

Trivy scans your codebase for known CVEs in Python dependencies.

📄 Output:
- JSON: `trivy-reports/deps.json`
- Table: `trivy-reports/deps.txt`

---

## 🧹 3. Secure Code Linting (Bandit)

- **Tool:** [Bandit](https://github.com/PyCQA/bandit)
- **Scope:** All Python files in the project

Bandit checks for dangerous patterns like:
- Use of `eval()`, `exec()`
- `subprocess` calls without sanitization
- Insecure use of `pickle`, `yaml.load`

📄 Output:
- `bandit-results.json`

---

## 🔑 4. Secret Scanning (Gitleaks)

- **Tool:** [Gitleaks](https://github.com/gitleaks/gitleaks)

Finds secrets such as:
- AWS keys
- Passwords
- OAuth tokens
- SSH keys

📄 Output:  
- `gitleaks-results.json`  
- Job summary in GitHub Actions UI

**Sample Result:**

| Rule ID     | Commit  | File               | Line | Author    |
|-------------|---------|--------------------|------|-----------|
| generic-key | a1b2c3d | `config.py`        | 42   | you       |

---

## 🐳 5. Docker Image Scanning (Optional)

- **Tool:** Trivy (Image mode)

Scans a Docker image built from your app for:
- OS-level CVEs (e.g., Ubuntu, Alpine)
- Python runtime/library vulnerabilities

📄 Output:
- `trivy-container-reports/image-results.json`
- `trivy-container-reports/image-report.txt`

---

## 📁 Artifacts Collected

After each CI run, GitHub Actions will upload these as artifacts:

- `bandit-results.json`
- `gitleaks-results.json`
- `trivy-reports/` (dependency scan)
- `trivy-container-reports/` (Docker image scan)
- `results/python.sarif` (CodeQL)

---

## 🧪 Run the Tools Locally

To test the security checks manually:

```bash
# Install Python packages
pip install -r requirements.txt

# Run Bandit
bandit -r . -f json -o bandit-results.json

# Run Trivy (file system)
trivy fs . --scanners vuln

# Build and scan Docker image
docker build -t my-python-app .
trivy image my-python-app

# Run Gitleaks
gitleaks detect --source=. --report-format=json --report-path=gitleaks-results.json
