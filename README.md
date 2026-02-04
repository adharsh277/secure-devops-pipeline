# 🔐 Secure DevSecOps Pipeline

## 📌 Overview

This project demonstrates a simple **DevSecOps CI pipeline** using GitHub Actions.
It automatically scans application code and Docker containers for security issues before allowing the build to succeed.

The goal is to show how security checks can be integrated early into the development workflow.

---

## ⚙️ Tech Stack

* FastAPI (sample application)
* Docker
* GitHub Actions (CI pipeline)
* Bandit (Python code security scan)
* Trivy (container vulnerability scan)

---

## 🚀 How It Works

1. Developer pushes code to GitHub.
2. GitHub Actions pipeline starts automatically.
3. Bandit scans the Python source code.
4. Docker image is built.
5. Trivy scans the container image.
6. Pipeline passes only if no **CRITICAL** vulnerabilities are found.

---

## 📂 Project Structure

```
secure-devops-pipeline
│
├── app/
│   └── main.py
├── Dockerfile
├── requirements.txt
└── .github/workflows/devsecops.yml
```

---

## 🎯 Purpose

This project shows how automated security checks can prevent insecure code and vulnerable containers from progressing through CI pipelines.

It focuses on **DevSecOps practices**, not application complexity.

---

## ▶️ Run Locally (Codespaces or Docker)

```
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

or

```
docker build -t secure-fastapi .
docker run -p 8000:8000 secure-fastapi
```
