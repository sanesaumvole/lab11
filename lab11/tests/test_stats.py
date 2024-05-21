from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_stats():
    client.get("/version/")
    client.get("/posts/")
    client.post("/posts/", json={"id": 4, "title": "Fourth Post", "content": "Content of the fourth post"})
    client.put("/posts/2", json={"id": 2, "title": "Updated Second Post", "content": "Updated content"})
    client.delete("/posts/2")

    response = client.get("/stats/")
    assert response.status_code == 200
    stats = response.json()
    assert stats["GET"]["version"] == 1
    assert stats["GET"]["posts"] == 1
    assert stats["POST"]["posts"] == 1
    assert stats["PUT"]["posts"] == 1
    assert stats["DELETE"]["posts"] == 1
