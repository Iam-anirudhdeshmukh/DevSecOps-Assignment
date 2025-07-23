# GitLab Security Assignment PoC

## Repository Setup

- **Repository**: DevSecOps-Assignment
- **Branches**: main, gitlab-assignment
- **CI Config**: gitlab-assignment.yaml
- **Application**: Vulnerable Python app with hardcoded secrets and outdated dependencies

---

## Security Features Configured

- SAST enabled via GitLab native template
- Secret Detection enabled and running
- Dependency Scanning enabled
- Secret Push Protection enabled but currently not blocking secrets (needs fix)
- Role-Based Access Control configured with minimal privileges
- Project organized in GitLab Groups/Subgroups
- Security Dashboards used to monitor scan results

---

## Pipeline Execution

- Pipelines trigger on push and merge requests to `gitlab-assignment` branch
- Security scans execute in stages:
  - SAST
  - Secret Detection
  - Dependency Scanning

---

## Scan Results Summary

- **SAST**: Detected hardcoded passwords and use of insecure functions
- **Secrets**: API keys found in source code
- **Dependencies**: Multiple vulnerabilities in `requirements.txt` packages

---

## Issues

- Secret Push Protection enabled but does not currently block commits with secrets
- Recommended to configure server-side hooks or push rules to fix

---

## Recommendations

- Organize repos with Groups/Subgroups for inherited security policies
- Assign least privilege roles
- Use reusable CI templates for consistency
- Enable security approvals on MRs
- Upgrade to GitLab Premium for advanced features like DAST and fuzzing

---

## Artifacts

- `gitlab-assignment.yaml`: Pipeline config file
- CI job logs and JSON reports available in pipeline jobs
- Screenshots saved in `/docs/screenshots/`

---

## Conclusion

GitLab’s integrated security tools enable early detection and mitigation of vulnerabilities, simplifying DevSecOps workflows. This setup proves a secure foundation despite minor issues with secret push protection.

