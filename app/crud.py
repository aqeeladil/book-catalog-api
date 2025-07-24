from sqlalchemy.orm import Session
from . import models, schemas

def get_books(db: Session, skip: int = 0, limit: int = 10):
    """Retrieve all books from DB."""
    return db.query(models.Book).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    """Retrieve a book by its ID."""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(db: Session, book: schemas.BookCreate):
    """Add a new book to the DB."""
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book: schemas.BookUpdate):
    """Update book data."""
    # db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    for var, value in vars(book).items():
        if value is not None:
            setattr(db_book, var, value)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    """Delete a book by ID."""
    # db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book


