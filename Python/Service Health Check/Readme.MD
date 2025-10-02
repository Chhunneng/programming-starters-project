# 🔍 Service Health Check (Python)

A simple Python script to check the health of a web service (HTTP endpoint).  
Perfect for DevOps beginners who want to learn about monitoring, logging, and exit codes in automation.

---

## 🚀 Features
- Checks if a given URL is reachable and returns HTTP 200
- Logs results to `health_check.log`
- Exits with:
  - `0` → Service is healthy
  - `1` → Service is unhealthy or unreachable
- Useful in CI/CD pipelines, cron jobs, or container health checks

---

## 📦 Requirements
- Python 3.7+
- `requests` library

Install dependencies:
```bash
pip install requests

---

## 🛠 Usage
Run the script with a URL:
python health_check.py https://example.com

