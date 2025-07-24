from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to provide DB session in each request (Dependency injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Async GET /books/
@app.get("/books/", response_model=list[schemas.Book])
async def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List all books."""
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


# ✅ GET /books/{id}
@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Get book by ID."""
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# ✅ POST /books/
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Create a new book."""
    return crud.create_book(db=db, book=book)


# ✅ PUT /books/{id}
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    """Update a book by ID."""
    db_book = crud.update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# ✅ DELETE /books/{id}
@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
