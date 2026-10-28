from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Total & Average" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_calculation():
    client = app.test_client()
    response = client.post("/calculate", json={"marks": [80, 90, 70]})
    assert response.status_code == 200
    assert response.json["total"] == 240
    assert response.json["average"] == 80.0
