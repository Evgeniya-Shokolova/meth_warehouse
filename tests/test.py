from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Пять минут": "полёт нормальный"}
