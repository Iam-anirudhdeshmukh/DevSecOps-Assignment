# 🔍 Python Project - SCA with Snyk + SBOM (GitHub Actions)

## 1. 🎯 Overview

This setup performs **Software Composition Analysis (SCA)** for Python projects using:

- **Snyk** for vulnerability scanning  
- **Syft** for SBOM (Software Bill of Materials) generation  
- **Grype** for scanning SBOMs against known vulnerabilities  

All steps are fully automated via **GitHub Actions**.

---

## 2. 🧰 Tools Used

| Tool    | Purpose                                | Why It's Used                                    |
|---------|---------------------------------------|-------------------------------------------------|
| Snyk    | Vulnerability scanning (CLI + HTML)   | Detects known CVEs in dependencies              |
| Syft    | Generates SBOM in CycloneDX JSON format | Standards-compliant, machine-readable inventory |
| Grype   | CVE scanning from SBOM                | Lightweight and SBOM-native                      |
| Node.js | Required for running Snyk CLI         | Snyk CLI runs via Node                           |

---

## 3. ⚙️ GitHub Actions Workflow

### Trigger Conditions:

- On push to `main` or `sca-assignment`  
- On pull requests to `main` or `sca-assignment`  

### YAML Workflow

```yaml
name: Python Snyk Scan + SBOM Analysis

on:
  push:
    branches: [main, sca-assignment]
  pull_request:
    branches: [main, sca-assignment]

jobs:
  snyk-sca-sbom-python:
    name: Snyk + SBOM Scan (Python)
    runs-on: ubuntu-latest
    continue-on-error: true

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Set up Node.js (for Snyk CLI)
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install Snyk CLI and snyk-to-html
        run: |
          npm install -g snyk snyk-to-html

      - name: Install Syft & Grype
        run: |
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
          curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
          syft version && grype version

      - name: Set up Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Authenticate with Snyk
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        run: snyk auth $SNYK_TOKEN

      - name: Run Snyk Test and Generate Reports
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        run: |
          mkdir -p snyk-reports
          snyk test --all-projects --json-file-output=snyk-reports/snyk-report.json || true
          snyk test --all-projects --json | snyk-to-html -o snyk-reports/snyk-report.html || true

      - name: Monitor Project in Snyk
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        run: snyk monitor --all-projects || true

      - name: Generate SBOM with Syft (CycloneDX JSON)
        run: syft dir:. -o cyclonedx-json > sbom.json

      - name: Scan SBOM with Grype
        run: grype sbom.json || true

      - name: Upload Snyk Reports as Artifacts
        uses: actions/upload-artifact@v4
        with:
          name: snyk-reports
          path: snyk-reports/

      - name: Upload SBOM as Artifact
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json
---
---

## 4. 📂 Output Artifacts

| File               | Description                                  |
|--------------------|----------------------------------------------|
| `snyk-report.json` | JSON output of vulnerability scan            |
| `snyk-report.html` | Human-readable HTML report                     |
| `sbom.json`        | CycloneDX-formatted SBOM for your Python project |

---

## 5. ✅ Benefits

- Early detection of known security issues in dependencies  
- Compliance-ready SBOM generation (CycloneDX format)  
- Easy integration with CI/CD via GitHub Actions  
- Does not block PRs due to `continue-on-error: true`  
- Can be extended to support Docker images and other ecosystems  

---

## 6. 📌 Requirements

- A valid `requirements.txt` file in the repository root  
- A configured GitHub secret: `SNYK_TOKEN`  

---

## 7. 📖 Reference Links

- [Snyk CLI Documentation](https://docs.snyk.io/cli)  
- [Anchore Syft](https://github.com/anchore/syft)  
- [Anchore Grype](https://github.com/anchore/grype)  
- [CycloneDX Specification](https://cyclonedx.org/specification/)  
- [Snyk GitHub Actions Docs](https://github.com/snyk/actions)  

---

## 8. 🎉 Conclusion

This pipeline equips Python developers with:

- 🔍 Full visibility into dependency vulnerabilities  
- 🛡️ Continuous monitoring and alerting via Snyk  
- 📄 SBOM support for regulatory and vendor compliance  
- ⚙️ Seamless GitHub-native CI/CD integration  
