# ASSIGNMENT 8: DAST Integration (Python)

---

## 1. Objective  
Integrate a Dynamic Application Security Testing (DAST) tool using **OWASP ZAP** in GitHub Actions to scan a vulnerable Python application and detect runtime security issues.

---

## 2. Repository Setup  
- **Repository Name**: DevSecOps-Assignment  
- **Branches**: main, owaspzap-assignment  
- **CI File**: `.github/workflows/zap.yml`  
- **Application**: Python Flask application with common security flaws:  
  - Hardcoded secrets  
  - SQL injection  
  - XSS via template injection  
  - Open file reads  
  - Vulnerable libraries in `requirements.txt`

---

## 3. Proof of Concept  
The working DAST integration is documented in `README-owaspzap.md`.

**PoC Components**:  
- Vulnerable Flask app runs locally on `http://127.0.0.1:5000`  
- GitHub Actions workflow starts the app and runs ZAP Full Scan  
- ZAP artifacts (`report_html.html`, `report_json.json`, `zap.out`) are uploaded for analysis  
- Screenshots/logs captured from local ZAP GUI runs and CI job outputs

---

## 4. CI/CD Workflow  
- **CI Config File**: `.github/workflows/zap.yml`  

The pipeline:  
- Starts the Flask application inside the CI runner using `nohup`  
- Triggers a ZAP Full Scan using official `zap-full-scan@v0.12.0` action  
- Uses `cmd_options: -a -z "-config connection.ssl_cert_validation=false"` for deeper active scan  
- Uploads scan results as artifacts  

**Triggers on:**  
- Push to `owaspzap-assignment`  
- Pull requests to `owaspzap-assignment`  
- Manual workflow dispatch

---

## 5. Vulnerability Scan Results  

| Vulnerability Type | Route/Context        | Severity | Description                       |
|--------------------|----------------------|----------|---------------------------------|
| SQL Injection      | `/login`             | High     | Raw SQL queries using user inputs |
| XSS                | `/xss?name=<script>` | Medium   | Reflected unsanitized input in HTML |
| Insecure Headers   | Global               | Medium   | Missing `X-Frame-Options`, `CSP` |
| Insecure Cookies   | N/A                  | Low      | `HttpOnly`/`Secure` flags not set |
| Information Leak   | `/`                  | Low      | Server details exposed in headers |

**Reports:**  
- `zap-report.html` — human-readable full scan report  
- `zap-report.json` — machine-readable results  
- `zap.out` — console logs of scan execution  

_All reports available as CI artifacts on workflow run._

---

## 6. Recommendations  
- **Fix SQL Injection:** Use parameterized queries (`sqlite3` or `SQLAlchemy`)  
- **Mitigate XSS:** Sanitize inputs and escape outputs in templates  
- **Set Security Headers:** Use `Flask-Talisman` or manual headers  
- **Secure Cookies:** Add `HttpOnly=True`, `Secure=True`, and `SameSite` flags  
- **Limit Information Exposure:** Remove `Server` and `X-Powered-By` headers  

---

## 7. Artifacts  

| File                | Description                                |
|---------------------|--------------------------------------------|
| `zap.yml`           | CI config running ZAP Full Scan in GitHub Actions |
| `zap-report.html`   | Full ZAP scan report (HTML)                |
| `zap-report.json`   | ZAP results in JSON format                  |
| `zap.out`           | CLI scan output and logs                    |
| `app.py`            | Python Flask web app                        |
| `requirements.txt`  | Python dependencies (intentionally vulnerable) |
| `README-owaspzap.md`| Setup instructions, screenshots, and findings |

---

## 8. Benefits  
- Black-box testing (no source code required)  
- Detects real-time, runtime issues like SQLi and XSS  
- Integrated directly into GitHub Actions for CI automation  
- ZAP is free, open-source, and actively maintained  
- Scan results are easily auditable and stored as artifacts  

---

## 9. Status  

| Component           | Status             |
|---------------------|--------------------|
| GitHub Actions setup| ✅ Completed       |
| Flask app launch    | ✅ Local in CI     |
| ZAP full scan       | ✅ Working         |
| Report artifacts    | ✅ Uploaded        |
| Authenticated scan  | ⚠️ Not configured (future scope) |

---

## 10. Conclusion  
The OWASP ZAP full scan integration with GitHub Actions offers powerful runtime security testing for Python web apps without requiring Docker Compose. This setup supports continuous vulnerability detection, aligning with modern DevSecOps best practices.
