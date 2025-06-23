# 🛡️ Shift Left Security in CI/CD Pipeline (Python)

This documentation explains how we implemented a **security-first CI/CD pipeline** using **GitHub Actions**. It helps catch vulnerabilities early—before they reach production.

---

## 🔍 1. Why Shift Left?

Security should start from the **first line of code**, not just at deployment. By shifting security left, we identify issues during development rather than in production.

### 🎯 Goals:
- Prevent vulnerabilities from reaching the `main` branch
- Detect secrets, dependency issues, and insecure code during pull requests
- Provide fast, automated feedback to developers

---

## ⚙️ 2. Tools & Pipeline Setup

We used **GitHub Actions** for its tight integration with GitHub, flexible configuration, and excellent ecosystem.

### 🔧 Tools Used

| Check Type                    | Tool                      | Purpose                                                  |
|------------------------------|---------------------------|----------------------------------------------------------|
| Static Code Analysis (SAST)  | CodeQL                    | Detect Python code vulnerabilities (e.g., injection)     |
| Dependency Scanning          | Trivy (Filesystem mode)   | Identify known CVEs in Python packages                   |
| Secure Linting               | Bandit                    | Catch insecure Python code patterns                      |
| Secret Scanning              | Gitleaks                  | Detect hardcoded secrets (API keys, tokens)              |
| Docker Image Scanning        | Trivy (Image scan)        | Scan container images for OS/library vulnerabilities     |

---

### 🧪 3. Pipeline Triggers

The security pipeline runs automatically:

- ✅ On push to `main` or `security-pipeline`
- ✅ On pull request to those branches
- ✅ Weekly on Sunday at 00:00 UTC (via cron)

📸 *Example pipeline run (GitHub Actions):*  
![GitHub Actions Screenshot](<Sucessful job.png>)

---

## ✅ 4. Benefits & Fixes

### 💡 Key Benefits
- **Immediate Feedback:** Security issues caught early
- **Less Manual Work:** Fully automated and repeatable
- **Better Code Quality:** Encourages secure development habits

### 🛠️ Common Issues & Fixes

| Problem                         | Fix                                                       |
|--------------------------------|------------------------------------------------------------|
| `jq` parsing issue in Gitleaks | Cleaned JSON and improved Markdown summary parsing         |
| Bandit false positives          | Customized Bandit config for relevant rules                |
| Trivy output verbosity          | Added both table and JSON reports for clarity              |
| Hard-to-read logs               | Used GitHub’s `GITHUB_STEP_SUMMARY` for better readability |

### ⏱️ Pipeline Duration
- ⌛ Adds **1.5–2.5 minutes** to pipeline — worth the trade-off for added security

---

## 📊 5. What Gets Reported

After each run, these results are generated:

- 🔍 **CodeQL** — Python code-level issues in `.sarif` format
- 🐍 **Bandit** — Python linting report in JSON
- 📦 **Trivy** — Dependency and container CVEs in JSON + table format
- 🔑 **Gitleaks** — Secrets detected with metadata

📸 *Example: Gitleaks Report Summary (Markdown in GitHub UI)*  
![Gitleaks Summary Screenshot](<Gitleaks summary.png>)  
📦 *Artifacts from a pipeline run:*  
![Artifacts Screenshot](Artifcats.png)

---

## 📁 6. Repository Structure

| File / Folder                    | Description                                        |
|----------------------------------|----------------------------------------------------|
| `.github/workflows/security.yml` | GitHub Actions pipeline configuration              |
| `bandit-results.json`            | Secure linting output for Python                   |
| `gitleaks-results.json`          | Detected secrets report                            |
| `trivy-reports/`                 | Trivy reports for dependency scanning              |
| `trivy-container-reports/`       | Trivy reports for Docker image scanning            |
| `results/python.sarif`           | CodeQL output for code-level findings              |
| `README.md`                      | Documentation and implementation overview          |

---

## ✅ 7. Conclusion

By integrating security checks early in our development process:

- 🛡️ We catch vulnerabilities before merge
- 🧪 We scan code, dependencies, secrets, and containers automatically
- 🔄 We improve the overall security and quality of our Python project

> **Shift left. Stay secure. 🔐**
