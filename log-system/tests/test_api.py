from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_log():
    response = client.post("/logs", json={
        "service": "test-service",
        "level": "error",
        "message": "test failure"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "test-service"


def test_get_logs():
    response = client.get("/logs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_high_severity_creates_bug():
    # create high severity log
    client.post("/logs", json={
        "service": "payment",
        "level": "error",
        "message": "critical failure"
    })

    # fetch bugs
    response = client.get("/bugs")

    assert response.status_code == 200
    bugs = response.json()

    assert isinstance(bugs, list)
    assert len(bugs) >= 1