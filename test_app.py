from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Grade" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_calculation_with_grade():
    client = app.test_client()
    response = client.post("/calculate", json={"marks": [85, 95, 90]})
    assert response.status_code == 200
    assert response.json["total"] == 270
    assert response.json["average"] == 90.0
    assert response.json["grade"] == "S"
