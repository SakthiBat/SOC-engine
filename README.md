# Sigma Detection Engine

A lightweight SOC-style Sigma Detection Engine built with Python.  
This project scans system logs against Sigma-like detection rules and generates alerts for suspicious activities.

---

## Features

- Read and parse system logs
- Detect suspicious events using Sigma rules
- Rule-based threat detection
- JSON-based alert generation
- Email alert support
- Easy-to-add custom Sigma rules
- Logging and report generation
- Beginner-friendly SOC project

---

# Project Structure

```bash
sigma-engine/
│
├── main.py
├── requirements.txt
├── README.md
├── config.py
│
├── logs/
│   ├── sample.log
│   └── detections.log
│
├── rules/
│   ├── failed_login.yml
│   ├── powershell_encoded.yml
│   └── multiple_failed_logins.yml
│
├── engine/
│   ├── parser.py
│   ├── detector.py
│   ├── rule_loader.py
│   └── alert.py
│
├── reports/
│   └── alerts.json
│
└── utils/
    └── helper.py
