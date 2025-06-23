import os

folders = [
    ".github/workflows",
    "src/test_app",
    "tests",
    "configs",
    "trivy-reports",
    "trivy-container-reports",
    "results",
]

files = [
    ".github/workflows/security.yml",
    "src/test_app/__init__.py",
    "src/test_app/main.py",
    "tests/test_main.py",
    "configs/bandit.yaml",
    "trivy-reports/trivy-results.json",
    "trivy-reports/trivy-report.txt",
    "trivy-container-reports/image-results.json",
    "trivy-container-reports/image-report.txt",
    "results/python.sarif",
    "gitleaks-results.json",
    "bandit-results.json",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "README.md",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    open(file, 'a').close()

print("Folder structure created successfully.")

