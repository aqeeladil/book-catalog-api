import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_book():
    # Creates a book before each test that uses this fixture
    response = client.post("/books/", json={
        "title": "Test Book",
        "author": "Tester",
        "published_year": 2023,
        "summary": "Fixture book"
    })
    assert response.status_code == 200
    return response.json()

def test_create_and_read_book(create_book):
    book_id = create_book["id"]

    # Read the created book
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Tester"

def test_update_book(create_book):
    book_id = create_book["id"]

    response = client.put(f"/books/{book_id}", json={"title": "Updated Title"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"

def test_delete_book(create_book):
    book_id = create_book["id"]

    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200

    # Confirm deletion
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 404
