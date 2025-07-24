from sqlalchemy import Column, Integer, String
from .database import Base

class Book(Base):
    """
    Represents a book record in the database.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    published_year = Column(Integer, nullable=False)
    summary = Column(String, nullable=True)