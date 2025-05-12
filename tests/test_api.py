from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "API online",
        "docs": "Acesse /docs ou /redoc"
    }

def test_analysis_endpoint():
    test_data = {"data": "exemplo"}
    response = client.post("/api/analyze", json=test_data)
    assert response.status_code == 200
    assert "result" in response.json()