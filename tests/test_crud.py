import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, schemas, crud
from app.database import Base

# Setup test database
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_books.db"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    yield db
    db.close()
    os.remove("test_books.db")

@pytest.fixture
def created_book(db):
    book_in = schemas.BookCreate(title="Fixture Book", author="Tester", published_year=2023)
    book = crud.create_book(db, book_in)
    return book

def test_create_book(db):
    book_in = schemas.BookCreate(title="UnitTest", author="Tester", published_year=2022)
    book = crud.create_book(db, book_in)
    assert book.title == "UnitTest"
    assert book.author == "Tester"
    assert book.published_year == 2022

def test_get_book(db, created_book):
    book = crud.get_book(db, created_book.id)
    assert book is not None
    assert book.title == "Fixture Book"

def test_update_book(db, created_book):
    book_update = schemas.BookUpdate(title="Updated Title")
    updated = crud.update_book(db, created_book.id, book_update)
    assert updated.title == "Updated Title"

def test_delete_book(db, created_book):
    deleted = crud.delete_book(db, created_book.id)
    assert deleted.id == created_book.id
    book = crud.get_book(db, created_book.id)
    assert book is None
