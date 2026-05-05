# Asynchronous Log Processing & Monitoring System

## Overview

This project implements a backend system for real-time log ingestion, processing, and monitoring.
It is designed with a non-blocking architecture where logs are stored immediately and processed asynchronously for severity classification and alerting.

---

## Features

* REST API for log ingestion and retrieval
* Asynchronous background processing
* Severity classification engine
* Automatic bug generation for high-severity logs
* CLI-based log injection
* Prometheus metrics integration
* Grafana dashboards for monitoring
* Dockerized deployment
* CI pipeline with GitHub Actions
* Automated testing with pytest

---

## Architecture

Client → FastAPI → Database
            ↓
      Background Processing
            ↓
Log Analyzer → Bug System → Alerts
            ↓
Prometheus → Grafana

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Prometheus
* Grafana
* Docker
* GitHub Actions
* Pytest

---

## Project Structure

```
app/
  api/
  core/
  models/
  schemas/
  services/
tests/
Dockerfile
docker-compose.yml
prometheus.yml
```

---

## Setup (Local)

```bash
uvicorn app.main:app --reload
```

Access:

* API Docs: http://127.0.0.1:8000/docs
* Metrics: http://127.0.0.1:8000/metrics

---

## Docker Setup

```bash
docker-compose up --build
```

Services:

* API: http://localhost:8000
* Prometheus: http://localhost:9090
* Grafana: http://localhost:3000

---

## Running Tests

```bash
pytest -v
```

---

## Example API Endpoints

* `POST /logs`
* `GET /logs`
* `GET /analytics`
* `GET /bugs`
* `PUT /bugs/{id}`
* `GET /health`

---

## Monitoring

The system exposes metrics at `/metrics` which are collected by Prometheus and visualized in Grafana dashboards.

---

## Future Improvements

* Replace SQLite with PostgreSQL
* Introduce message queue (Redis + Celery)
* Add authentication and user management
* Implement alerting via email or external services

---

## License

MIT License
