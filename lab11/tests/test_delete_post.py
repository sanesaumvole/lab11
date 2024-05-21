from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_delete_post():
    # Виконати дії для створення поста, який потім буде видалений
    # Наприклад, додати пост у базу даних або видалити існуючий пост
    # Викликати метод видалення поста через клієнт API
    response = client.delete("/posts/1")  # Припущення: пост з id=1 існує і його можна видалити
    # Перевірка, чи була успішно видалена
    assert response.status_code == 200
    # Перевірка, чи повернуті дані відповідають очікуваним
    assert response.json() == {"id": 1, "title": "First Post", "content": "Content of the first post"}
