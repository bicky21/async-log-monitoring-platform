# Async Log Monitoring Platform

## Overview

This project implements a backend system for real-time log ingestion, processing, and monitoring. Logs are accepted through an API, stored immediately, and processed asynchronously to classify severity and trigger follow-up actions such as alerts and bug creation.

The system is designed with a non-blocking architecture to ensure responsiveness under load, while maintaining clear separation between request handling and background processing.

---

## Key Features

* REST API for log ingestion and retrieval
* Asynchronous processing using a queue-based architecture
* Automatic severity classification of logs
* Bug generation for high-severity events
* Real-time metrics exposure via Prometheus
* Grafana dashboards for monitoring and analysis
* Load simulation scripts for stress testing
* CI pipeline with automated testing (pytest)
* Docker-ready structure (optional deployment)

---

## Architecture

```
Client
  │
  ▼
FastAPI (API Layer)
  │
  ▼
Redis Queue
  │
  ▼
Worker Process
  │
  ▼
Database (SQLite / PostgreSQL)
  │
  ▼
Metrics → Prometheus → Grafana
```

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Redis (Memurai on Windows)
* RQ (Queue system)
* Prometheus
* Grafana
* Pytest
* GitHub Actions

---

## Project Structure

```
app/
  api/
  core/
  models/
  schemas/
  services/
scripts/
tests/
worker.py
prometheus.yml
docker-compose.yml
```

---

## Getting Started

### 1. Run API

```
uvicorn app.main:app --reload
```

Access:

* API Docs: http://127.0.0.1:8000/docs
* Metrics: http://127.0.0.1:8000/metrics

---

### 2. Start Worker

```
python worker.py
```

---

### 3. Run Load Simulation

```
python scripts/stress_test.py
```

---

### 4. Run Tests

```
pytest -v
```

---

## Monitoring

The application exposes metrics at `/metrics`. These are collected by Prometheus and visualized in Grafana dashboards.

Typical metrics monitored:

* Request rate
* Endpoint usage
* High severity log rate
* Traffic spikes

---

## Design Decisions

* **Asynchronous processing**: avoids blocking API requests
* **Queue-based architecture**: separates ingestion from processing
* **Worker model**: allows scaling independently of API
* **Metrics integration**: enables observability and performance analysis

---

## Known Limitations

* SQLite is not suitable for high concurrency
* RQ uses a simplified worker model on Windows
* Background processing is single-node (not distributed)

---

## Future Improvements

* Replace SQLite with PostgreSQL
* Introduce distributed workers
* Add retry and failure handling for jobs
* Implement alert notifications (email / webhook)
* Add authentication and access control

---

## Summary

This project demonstrates how to build a scalable backend system by decoupling request handling from processing, adding observability, and validating behavior under load.
