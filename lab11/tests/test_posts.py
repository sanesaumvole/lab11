# tests/test_posts.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Очікуємо один пост, оскільки тестова база даних містить лише один пост

def test_update_post():
    # Спочатку створіть пост для оновлення
    response = client.post("/posts/", json={"id": 1, "title": "First Post", "content": "Content of the first post"})
    assert response.status_code == 200
    updated_post = {"id": 1, "title": "Updated First Post", "content": "Updated content"}
    response = client.put("/posts/1", json=updated_post)
    assert response.status_code == 200

def test_delete_post():
    # Спочатку створіть пост для видалення
    response = client.post("/posts/", json={"id": 1, "title": "First Post", "content": "Content of the first post"})
    assert response.status_code == 200
    response = client.delete("/posts/1")
    assert response.status_code == 200
